import functools
import csv
import re
from .custom_logger import log, log_extraction_information
from .scroller      import store_already_written_videos
def time_writer_function(writer_function):
    @functools.wraps(writer_function)
    def wrapper_timer(*args, **kwargs):
        log_extraction_information(writer_function.__name__, writer_function, args, kwargs)
    return wrapper_timer
@time_writer_function
def create_file(file_type, file_name, file_buffering, newline, csv_writer, timestamp, logging_locations, identifier, reverse_chronological, video_data):
    with open(f'temp_{file_name}_{timestamp}.{file_type}', mode='w', newline=newline, encoding='utf-8',  buffering=file_buffering) as temp_file:
        if file_type == 'csv':
            fieldnames = ['Video Number', 'Video Title', 'Video Duration', identifier, 'Watched', 'Watch again later', 'Notes']
            csv_writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            csv_writer.writeheader()
        create_writer(file_type, temp_file, csv_writer, logging_locations, identifier, video_data)
        total_videos = len(video_data)
    return file_name, total_videos, reverse_chronological, logging_locations
def create_writer(file_type, file, csv_writer, logging_locations, identifier, video_data):
    total_writes = 0
    for video_datum in video_data:
        video_number   = video_datum[0]
        video_title    = video_datum[1]
        video_duration = video_datum[2]
        video_url      = video_datum[3]
        entry(file_type, file, csv_writer, video_number, video_title, video_duration, video_url, identifier)
        total_writes  += 1
        if total_writes % 250 == 0:
            log(f'{total_writes} videos written to {file.name}...', logging_locations)
@time_writer_function
def update_file(file_type, file_name, file_buffering, newline, csv_writer, timestamp, logging_locations, identifier, reverse_chronological, video_data, visited_videos, video_id_only):
    if visited_videos is None: visited_videos = store_already_written_videos(file_name, file_type)
    visited_videos = format_visited_videos_for_id(visited_videos, video_id_only, logging_locations)
    with open(f'{file_name}.{file_type}', mode='r+', newline=newline, encoding='utf-8',  buffering=file_buffering) as old_file, open(f'temp_{file_name}_{timestamp}.{file_type}', mode='w+', newline=newline, encoding='utf-8',  buffering=file_buffering) as temp_file:
        if file_type == 'csv':
            number_of_existing_videos = int(max(re.findall('^(\d+)?,', old_file.read(), re.M), key=lambda i: int(i)))
            fieldnames                = ['Video Number', 'Video Title', 'Video Duration', identifier, 'Watched', 'Watch again later', 'Notes']
            csv_writer                = csv.DictWriter(temp_file, fieldnames=fieldnames)
            if reverse_chronological: csv_writer.writeheader()
        else:
            number_of_existing_videos = int(max(re.findall('^(?:### )?Video Number:\s*(\d+)', old_file.read(), re.M), key=lambda i: int(i)))
        new_videos = update_writer(file_type, temp_file, old_file, csv_writer, logging_locations, identifier, reverse_chronological, video_data, visited_videos, number_of_existing_videos)
    return file_name, new_videos, reverse_chronological, logging_locations
def format_visited_videos_for_id(visited_videos, video_id_only, logging_locations):
    if video_id_only is True:
        log('Updating set to keep only the video ID from the full video URL...', logging_locations)
        formatted_visited_videos = set()
        while visited_videos:
            full_url       = visited_videos.pop()
            video_id       = full_url.split('watch?v=')[1]
            formatted_visited_videos.add(video_id)
        log('Finished formatting the video IDs in the set...\n', logging_locations)
        visited_videos = formatted_visited_videos
    return visited_videos
def update_writer(file_type, new_file, old_file, csv_writer, logging_locations, identifier, reverse_chronological, video_data, visited_videos, number_of_existing_videos):
    new_videos   = find_number_of_new_videos(video_data, visited_videos)
    if reverse_chronological is True:
        video_number = number_of_existing_videos + new_videos
        incrementer  = -1
    else:
        video_number = number_of_existing_videos + 1
        incrementer  = 1
    total_writes = 0
    for video_datum in video_data:
        video_title    = video_datum[1]
        video_duration = video_datum[2]
        video_url      = video_datum[3]
        if video_url in visited_videos:
            continue
        entry(file_type, new_file, csv_writer, video_number, video_title, video_duration, video_url, identifier)
        video_number += incrementer
        total_writes += 1
        if total_writes % 250 == 0:
            log(f'{total_writes} new videos written to {new_file.name}...', logging_locations)
    if reverse_chronological:
        old_file.seek(0)
        if file_type == 'csv': old_file.readline()
        for line in old_file:  new_file.write(line)
    else:
        new_file.seek(0)
        for line in new_file: old_file.write(line)
    return new_videos
def find_number_of_new_videos(video_data, visited_videos):
    visited_on_page = {video[3] for video in video_data}
    return len(visited_on_page.difference(visited_videos))
def entry(file_type, file_object, csv_writer, video_number, video_title, video_duration, video_url, identifier):
    if file_type == 'csv': write_csv (csv_writer,  video_number, video_title, video_duration, video_url, identifier)
    else:                  write_text(file_object, video_number, video_title, video_duration, video_url, identifier, file_type)
def write_text(file, video_number, video_title, video_duration, video_url, identifier, file_type):
    newline  = '\n'
    markdown = file_type == 'md'
    def ljust(text):
        if markdown:
            prefix  = '### '
            padding = 24
        else:
            prefix  = ''
            padding = 19
        return f'{prefix}{text}'.ljust(padding)
    if markdown:
        file.write(f'## {video_title}{newline}')
        file.write(f'{ljust("Video Number:")  }{video_number}{newline}')
    else:
        file.write(f'{ljust("Video Number:")}{video_number}{newline}')
        file.write(f'{ljust("Video Title:")}{video_title}{newline}')
    file.write(f'{ljust("Video Duration:")}{video_duration}{newline}')
    file.write(f'{ljust(identifier + ":")}{video_url}{newline}')
    file.write(f'{ljust("Watched:")}{newline}')
    file.write(f'{ljust("Watch again later:")}{newline}')
    file.write(f'{ljust("Notes:")}{newline}')
    file.write('*'*75 + newline)
    if markdown: file.write('\n')
def write_csv(writer, video_number, video_title, video_duration, video_url, identifier):
    writer.writerow(
        {
            'Video Number':      f'{video_number}',
            'Video Title':       f'{video_title}',
            'Video Duration':    f'{video_duration}',
            identifier:          f'{video_url}',
            'Watched':           '',
            'Watch again later': '',
            'Notes':              ''
        }
    )
