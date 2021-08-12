import threading
import datetime
import time
import os
NEWLINE = '\n'
def log(message, logging_locations):
 thread_name = f'[{threading.current_thread().name}]'
 current_time = datetime.datetime.now().isoformat()
 utc_offset = time.strftime('%z')
 formatted_message = f'{current_time}{utc_offset} {thread_name:>12} {message}\n'
 for location in logging_locations:
  location.write(formatted_message)
def log_extraction_information(function, writer_function, args, kwargs):
 start_time = time.perf_counter()
 extension = args[0]
 timestamp = args[5]
 file_name, videos_written, reverse_chronological, logging_locations = writer_function(*args, **kwargs)
 if videos_written == 1: videos = 'video'
 else: videos = 'videos'
 end_time = time.perf_counter()
 total_time = end_time - start_time
 temp_file = f'temp_{file_name}_{timestamp}.{extension}'
 final_file = f'{file_name}.{extension}'
 padding = 39
 log('Finished writing to'.ljust(padding) + f'{temp_file}', logging_locations)
 if function == 'create_file': log(f'{videos_written} {videos} written to'.ljust(padding) + f'{temp_file}', logging_locations)
 if function == 'update_file': log(f'{videos_written} ***NEW*** {videos} written to'.ljust(padding) + f'{temp_file}', logging_locations)
 log('Closing'.ljust(padding) + f'{temp_file}', logging_locations)
 log(f'Successfully completed write, renaming {temp_file} to {final_file}', logging_locations)
 if function == 'update_file' and not reverse_chronological:
  os.remove(temp_file)
 else:
  os.replace(temp_file, final_file)
 log('Successfully renamed'.ljust(padding) + f'{temp_file} to {final_file}', logging_locations)
 if function == 'create_file': log(f'It took {total_time} seconds to write all {videos_written} {videos} to {final_file}{NEWLINE}', logging_locations)
 if function == 'update_file': log(f'It took {total_time} seconds to write the {videos_written} ***NEW*** {videos} to the pre-existing {final_file}{NEWLINE}', logging_locations)
