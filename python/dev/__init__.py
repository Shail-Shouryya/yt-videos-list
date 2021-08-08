'''
YouTube bot to make a YouTube videos list (including all video titles and
URLs uploaded by a channel) with end-to-end web scraping - no API tokens required.
🌟 Star this repo if you found it useful! 🌟
https://github.com/slow-but-steady/yt-videos-list
'''

import sys
import time
import random

from save_thread_result import ThreadWithResult

from . import logic
from .custom_logger import log


__version__              = '0.6.0'
__author__               = 'slow-but-steady'
__email__                = 'yt.videos.list@gmail.com'
__development_status__   = '4 - Beta'
__intended_audience__    = 'Developers, Hobbyists'
__license__              = 'OSI Approved :: Apache License 2.0'
__ideal_python_version__ = 'Python 3.6+'
__source__               = 'https://github.com/slow-but-steady/yt-videos-list/tree/main/python'


print(f'=======> NOTE <=======\n\nYou are using yt_videos_list package version >= 0.6.0 (currently {__version__}).\nThere are some formatting changes to the output files as of release 0.6.0 that may **potentially** interfere with your workflow, so please review https://github.com/slow-but-steady/yt-videos-list/releases/tag/v.0.6.0 to see if you need to do anything.\nThanks!')


class ListCreator:
    '''
    The ListCreator class creates a ListCreator instance with no required arguments.
    Example usage:
        lc = ListCreator()


    #############################################################################################################

    If you ALREADY scraped a channel and the channel uploaded a new video, simply rerun this
    program on that channel and this package updates your files to include the newer video(s)!


    OPTIONAL: Specify the settings you want to use by substituing the desired values for the default arguments.
    An overview is given directly below this, but for a full working example scroll to the bottom.

    Options for the `driver` argument are
      * Firefox (default)
      * Opera
      * Safari (MacOS only)
      * Chrome
      * Brave
      * Edge (Windows only)
        -> driver='firefox'
        -> driver='opera'
        -> driver='safari'
        -> driver='chrome'
        -> driver='brave'
        -> driver='edge'

    Options for the `cookie_consent` argument are
      * False (default) - block all cookie options if prompted by YouTube (at consent.youtube.com)
      * True            - accept all cookie options if prompted by YouTube (also at consent.youtube.com)
          -> cookie_consent=False (default) OR cookie_consent=True

    Options for the file type arguments (`csv`, `txt`, `md`) are
      * True (default) - create a file for the specified type
      * False - does NOT create a file for the specified type
          -> txt=True  (default) OR txt=False
          -> csv=True  (default) OR csv=False
          ->  md=True  (default) OR  md=False

    Options for the `file_suffix` arguments are
      * True (default) - add a file suffix to the output file name
        * ChannelName_reverse_chronological_video{is_id}s_list.csv
        * ChannelName_chronological_video{is_id}s_list.csv
      * False - does NOT add a file suffix to the output file name
        * this means if a reverse chronological file and a chronological file
          is made for the same channel, they will have the same name!
        * ChannelName.csv (reverse chronological output file)
        * ChannelName.csv (chronological output file)
          -> file_suffix=True  (default) OR file_suffix=False

    Options for the `all_video_data_in_memory` argument are
      * False (default) - does not scrape the entire page
      * True            -          scrape the entire page (must ALSO set the `video_data_returned` attribute to True to return this data!)
          -> all_video_data_in_memory=False (default) OR all_video_data_in_memory=True

    Options for the `video_data_returned` argument are
      * False (default) - does not return video data collected from the current scrape job (returns dummy data instead: [[0, '', '', '']])
      * True            -          return video data collected from the current scrape job
        -> if `all_video_data_in_memory` attribute is set to False, the returned data MIGHT not be the full data, and video numbering MIGHT be incorrect
        -> set `all_video_data_in_memory` attribute to True to return ALL video data for channel (video number will then also ALWAYS be correct)
          -> video_data_returned=False (default) OR video_data_returned=True

    Options for the `video_id_only` argument are
      * False (default) - include      the full URL             to video: https://www.youtube.com/watch?v=ElevenChars
      * True            - include only the identifier parameter to video:                                 ElevenChars
          -> video_id_only=False (default) OR video_id_only=True

    Options for the `reverse_chronological` argument are
      * True (default) - write the files in order from most recent video to the oldest video
      * False          - write the files in order from oldest video to the most recent video
          -> reverse_chronological=True (default) OR reverse_chronological=False

    Options for the `headless` argument are
      * False (default) - run the driver with an open Selenium instance for viewing
      * True            - run the driver without an open Selenium instance for viewing (runs in "invisible" mode)
          -> headless=False (default) OR headless=True

    Options for the `scroll_pause_time` argument` are any float values greater than 0 (defaults to 0.8)
      * CAUTION: reducing this value too much will result in the program not capturing all the videos,
        so be careful! Experiment :)
      * The value you provide will be how long (in seconds) the program waits before
        trying to scroll the videos list page down for the channel you want to scrape.
      * For fast internet connections, you may want to reduce the value,
        and for slow connections you may want to increase the value.
          -> scroll_pause_time=0.8 (default)

    Options for the `verify_page_bottom_n_times` argument are any int values greater than 0 (defaults to 3)
      * NOTE: this argument is only used when CREATING a new file for a
              new channel, and is unused when UPDATING an existing file for an already scraped channel.
      * The value you provide will be how many times the program needs to verify it acually reached the
        bottom of the page before accepting it is the bottom of the page, and starting to write the information
        to the output file(s).
      * For channels that have uploaded THOUSANDS of videos, increase this value to
        a large number that you think should be sufficient to verify the program reached the bottom of the page.
      * To determine HOW large of a value you should provide, determine the length of time you'd like to wait
        before being reasonably sure that you reached the bottom of the page and it's not just YouTube's server
        trying to fetch the response from an old database entry, and divide the time you decided to wait by the
        scroll_pause_time argument.
          -> For example, if you want to wait 45 seconds and you set the scrioll_pause_time value to 1.0
            -> your_time / scroll_pause_time
            -> 45 / 1.0
            -> 45
            -> therefore: verify_page_bottom_n_times=45
          -> For channels with only a couple hundred videos (or less), the default value of verify_page_bottom_n_times=3
             **should** be sufficient.
      * See commit a68f8f62e5c343cbb0641125e271bb96cc4f0750 for more details.

    Options for the `file_buffering` argument are any int values greater than 0 (defaults to -1, which uses the default OS setting)
      * LEAVE THIS ALONE IF YOU'RE UNSURE!
      * Documentation:
        -> https://docs.python.org/3/library/functions.html#open
      * Deep dive:
        -> https://stackoverflow.com/questions/3167494/how-often-does-python-flush-to-a-file
        -> https://stackoverflow.com/questions/10019456/usage-of-sys-stdout-flush-method
          -> https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
          -> https://en.wikipedia.org/wiki/Data_buffer
          -> https://stackoverflow.com/questions/1450551/buffered-vs-unbuffered-io
        -> https://www.quora.com/What-does-flushing-files-or-Stdin-do-in-Python
        -> https://www.quora.com/Whats-the-difference-between-buffered-I-O-and-unbuffered-I-O
        -> https://stackoverflow.com/questions/8409050/unix-buffered-vs-unbuffered-i-o
        -> https://medium.com/@bramblexu/three-ways-to-close-buffer-for-stdout-stdin-stderr-in-python-8be694bd2737
        -> https://www.quora.com/In-C-what-does-buffering-I-O-or-buffered-I-O-mean

    #####################################################################################################

    WORKING EXAMPLES:

    Minimalist (ListCreator object creates a csv, txt, and md file in reverse chronological order -
    meaning the most recently uploaded videos are at the top of the file):

    lc = ListCreator()


    Minimalist but with a different driver:
    -> lc = ListCreator(driver='firefox') # default, argument not required
    -> lc = ListCreator(driver='opera')
    -> lc = ListCreator(driver='safari')
    -> lc = ListCreator(driver='chrome')
    -> lc = ListCreator(driver='brave')
    -> lc = ListCreator(driver='edge')


    Minimalist in headless ("invisible") mode (NOTE: currently only supported by firefox and chrome):
    -> lc = ListCreator(headless=True)                    # runs firefox in headless mode
    -> lc = ListCreator(driver='chrome', headless=True)   # runs chrome  in headless mode


    Minimalist with reverse chronological order (ListCreator object creates a csv, txt, and md file with
    oldest videos at the top of the file instead of the most recently uploaded videos at the top):
    -> lc = ListCreator(reverse_chronological=False)

    -----------------------------------------------------------------------------------------------------

    Minimalist with longer pauses (useful for slow internet) for channels with a couple hundred videos:
    -> lc = ListCreator(scroll_pause_time=1.2)

    Minimalist with shorter pauses (useful for fast internet) for channels with a couple hundred videos:
    -> lc = ListCreator(scroll_pause_time=0.7)

    -----------------------------------------------------------------------------------------------------

    Minimalist with longer pauses (useful for slow internet) for channels with THOUSANDS of videos:
    -> lc = ListCreator(scroll_pause_time=1.2, verify_page_bottom_n_times=40)

    Minimalist with shorter pauses (useful for fast internet) for channels with THOUSANDS of videos:
    -> lc = ListCreator(scroll_pause_time=0.7, verify_page_bottom_n_times=40)

    -----------------------------------------------------------------------------------------------------

    Only creating a csv file with everything else set to default:
    -> lc = ListCreator(txt=False, md=False)

    =====================================================
    | If you found this interesting or useful,          |
    | ** please consider STARRING this repo at **       |
    | https://github.com/slow-but-steady/yt-videos-list  |
    | so other people can more easily find and use this.|
    | Thank you!!                                       |
    =====================================================
    '''
    def __init__(self, txt=True, csv=True, md=True, file_suffix=True, all_video_data_in_memory=False, video_data_returned=False, video_id_only=False, reverse_chronological=True, headless=False, scroll_pause_time=0.8, driver=None, cookie_consent=False, verify_page_bottom_n_times=3, file_buffering=-1):
        '''
        Initializes an instance of ListCreator by setting the attributes of the instance to the provided arguments,
        and setting any attributes not provided as the default parameter value.
        '''
        self.txt                        = txt
        self.csv                        = csv
        self.markdown                   = md
        self.file_suffix                = file_suffix
        self.all_video_data_in_memory   = all_video_data_in_memory
        self.video_data_returned        = video_data_returned
        self.video_id_only              = video_id_only
        self.reverse_chronological      = reverse_chronological
        self.headless                   = headless
        self.scroll_pause_time          = scroll_pause_time
        self.driver                     = None if driver is None else driver.lower()
        self.cookie_consent             = cookie_consent
        self.verify_page_bottom_n_times = max(1, int(verify_page_bottom_n_times))
        self.file_buffering             = file_buffering
        all_video_data_in_memory_but_no_video_data_returned  = 'WARNING! You set the all_video_data_in_memory attribute to True but the video_data_returned attribute is False.\nThe program will scrape the ENTIRE channel (even if you have pre-existing files for the channel) BUT will not return the video_data as a return value.\n\nIf you want the video_data returned,                    set the video_data_returned attribute to True.\nIf you do not want to always scrape the entire channel, set the all_video_data_in_memory attribute to False.\n\n\n\n'
        not_all_video_data_in_memory_but_video_data_returned = 'WARNING! The all_video_data_in_memory attribute is False but you set the video_data_returned attribute to True.\nThe program will NOT scrape the ENTIRE channel if pre-existing files for the channel exist, BUT WILL return the video_data as a return value.\nIf pre-existing files for the channel do NOT exist, then the program WILL return video_data for the ENTIRE channel.\n\nIf you want the video_data for the ENTIRE channel ALWAYS returned, set the all_video_data_in_memory attribute to True.\nIf you do not want any video_data returned,                        set the video_data_returned      attribute to False.\n\n\n\n'
        video_data_returned_information                      = 'NOTE! The video_data_returned attribute is set to True, so the program will return the video information for all videos that LOAD when the program runs.\n\nIf you set the all_video_data_in_memory attribute to True: the program will ALWAYS return video_data for ALL videos uploaded to the channel.\nIf you set the all_video_data_in_memory attribute to False:\n  - the program will return video_data for the videos that LOAD for the channel IF pre-existing files for the channel DO exist (will not always include ALL videos uploaded to the channel)\n  - the program will return video_data for ALL videos uploaded to the channel IF pre-existing files for the channel DO NOT exist\n\n\n\n'
        if   self.all_video_data_in_memory is True  and self.video_data_returned is False: print(all_video_data_in_memory_but_no_video_data_returned)
        elif self.all_video_data_in_memory is False and self.video_data_returned is True:  print(not_all_video_data_in_memory_but_video_data_returned)
        if   self.video_data_returned is True:                                             print(video_data_returned_information)


    def __repr__(self):
        '''
        Returns an unambiguous representation of the current instance that can be used to recreate the same exact object.
        This is useful for internal use and making developer debugging easier.
        '''
        formatted_driver = f"'{self.driver}'" if self.driver else None
        return f'''{self.__class__.__name__}(txt={self.txt}, csv={self.csv}, md={self.markdown}, file_suffix={self.file_suffix}, all_video_data_in_memory={self.all_video_data_in_memory}, video_data_returned={self.video_data_returned}, video_id_only={self.video_id_only}, reverse_chronological={self.reverse_chronological}, headless={self.headless}, scroll_pause_time={self.scroll_pause_time}, driver={formatted_driver}, cookie_consent={self.cookie_consent}, verify_page_bottom_n_times={self.verify_page_bottom_n_times}, file_buffering={self.file_buffering})'''


    def __str__(self):
        '''
        Returns an easy to read representation of the current instance.
        This is useful for typical users to see the attributes of the current instance and is ideal for human consumption.
        '''
        return f'''
        {self.__class__.__name__}() object created with attributes
          txt                        = {self.txt}
          csv                        = {self.csv}
          md                         = {self.markdown}
          file_suffix                = {self.file_suffix}
          all_video_data_in_memory   = {self.all_video_data_in_memory}
          video_data_returned        = {self.video_data_returned}
          video_id_only              = {self.video_id_only}
          reverse_chronological      = {self.reverse_chronological}
          headless                   = {self.headless}
          scroll_pause_time          = {self.scroll_pause_time}
          driver                     = '{self.driver}'
          cookie_consent             = {self.cookie_consent}
          verify_page_bottom_n_times = {self.verify_page_bottom_n_times}
          file_buffering             = {self.file_buffering}

        To recreate object, use:
        >>> {self.__repr__()}
        '''


    def create_list_for(self, url=None, log_silently=False, file_name='auto'):
        '''
        The create_list_for() method creates a list using the arguments specified during instantiation of the ListCreator object.
        You need to specify just the url to the channel you want to scrape.

        Set `log_silently` to `True` to mute program logging to the console. The program will log the prgram status and any
        program information to only the log file for the channel being scraped (this is useful when scraping multiple channels at
        once with multi-threading). By default, the program logs to both the log file for the channel being scraped AND the console.

        You can also provide an optional file_name argument, but this is NOT recommended -
        the program finds the name of the channel automatically and if you rename the file,
        the file won't be automatically updated if the channel uploads a new video and you run this on that channel
        UNLESS you provide the same **exact** name every time you rerun this.

        The suggested arguments for the `file_name` argument are 'auto' or 'id'
          * 'auto': the program uses the name that shows up under the banner when you navigate to the channel's homepage (with spaces removed)
          * 'id': the program uses the identifier from the URL
            -> If the channel is Corey Schafer:
              * NOTE output file name stays the same regardles of `reverse_chronological` instance attribute value
                if `file_suffix` instance attribute is `False`
              * ALSO NOTE the .EXT used below in the example file names substitutes for the extension formats: .[txt|csv|md|log]

              * if you provide https://www.youtube.com/user/schafer5:                           the 'id' will be:  schafer5
                -> if the `file_suffix` instance attribute is set to `True`
                    -> and the `reverse_chronological` instance attribute is True,  the output file name will be:  schafer5_reverse_chronological_video{is_id}s_list.EXT
                    -> and the `reverse_chronological` instance attribute is False, the output file name will be:  schafer5_chronological_video{is_id}s_list.EXT
                -> if the `file_suffix` instance attribute is set to `False`
                    -> and the `reverse_chronological` instance attribute is True,  the output file name will be:  schafer5.EXT
                    -> and the `reverse_chronological` instance attribute is False, the output file name will be:  schafer5.EXT

              * if you provide https://www.youtube.com/c/Coreyms/:                              the 'id' will be:  Coreyms
                -> if the `file_suffix` instance attribute is set to `True`
                    -> and the `reverse_chronological` instance attribute is True,  the output file name will be:  Coreyms_reverse_chronological_video{is_id}s_list.EXT
                    -> and the `reverse_chronological` instance attribute is False, the output file name will be:  Coreyms_chronological_video{is_id}s_list.EXT
                -> if the `file_suffix` instance attribute is set to `False`
                    -> and the `reverse_chronological` instance attribute is True,  the output file name will be:  Coreyms.EXT
                    -> and the `reverse_chronological` instance attribute is False, the output file name will be:  Coreyms.EXT

              * if you provide https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g:        the 'id' will be:  UCCezIgC97PvUuR4_gbFUs5g
                -> if the `file_suffix` instance attribute is set to `True`
                    -> and the `reverse_chronological` instance attribute is True,  the output file name will be:  UCCezIgC97PvUuR4_gbFUs5g_reverse_chronological_video{is_id}s_list.EXT
                    -> and the `reverse_chronological` instance attribute is False, the output file name will be:  UCCezIgC97PvUuR4_gbFUs5g_chronological_video{is_id}s_list.EXT
                -> if the `file_suffix` instance attribute is set to `False`
                    -> and the `reverse_chronological` instance attribute is True,  the output file name will be:  UCCezIgC97PvUuR4_gbFUs5g.EXT
                    -> and the `reverse_chronological` instance attribute is False, the output file name will be:  UCCezIgC97PvUuR4_gbFUs5g.EXT

              * the channel name under the banner is 'Corey Schafer'                  so the 'auto' name will be: 'CoreySchafer'     (regardless of which URL format you provide)
                -> if the `file_suffix` instance attribute is set to `True`
                    -> and the `reverse_chronological` instance attribute is True,  the output file name will be:  CoreySchafer_reverse_chronological_video{is_id}s_list.EXT   (default)
                    -> and the `reverse_chronological` instance attribute is False, the output file name will be:  CoreySchafer_chronological_video{is_id}s_list.EXT
                -> if the `file_suffix` instance attribute is set to `False`
                    -> and the `reverse_chronological` instance attribute is True,  the output file name will be:  CoreySchafer.EXT
                    -> and the `reverse_chronological` instance attribute is False, the output file name will be:  CoreySchafer.EXT
        '''
        _execution_type     = 'module'
        instance_attributes = (self.txt, self.csv, self.markdown, self.file_suffix, self.all_video_data_in_memory, self.video_id_only, self.reverse_chronological, self.headless, self.scroll_pause_time, self.driver, self.cookie_consent, self.verify_page_bottom_n_times, self.file_buffering, self.__repr__())
        video_data, write_information = logic.execute(url, file_name, log_silently, *instance_attributes, _execution_type)
        if self.video_data_returned:
            return (video_data,    write_information)
        return ([[0, '', '', '']], write_information) # return dummy video_data


    def create_list_from(self, path_to_channel_urls_file, number_of_threads=4, min_sleep=1, max_sleep=5, after_n_channels_pause_for_s=(20, 10), log_subthread_status_silently=False, log_subthread_info_silently=False, file_name='auto'):
        '''
        The create_list_from() method creates a list using the arguments specified during instantiation of the ListCreator object.
        You need to specify just the path to the text file containing urls of all the channels
        you want to scrape as the `path_to_channel_urls_file` argument.
        NOTE that each url **should be placed on a new line!**

        Use the `file_name` argument to set how the program names the output files:
          -> file_name='auto' (default) OR file_name='id'
              >>> help(ListCreator.create_list_for)    # see detailed explanation about differences between 'auto' and 'id'


        Set `number_of_threads` argument to the maximum number of channels you want the program can scrape simultaneously.

        Use the following arguments to make the program appear less bot-like
        (this becomes more important as you try to scrape more and more channels at once):
            `min_sleep`
              * minimum amount of time (seconds) to sleep before starting a new subthread to scrape the next channel
              * accepts an `int` or `float`
                -> min_sleep=1 (default)
            `max_sleep`
              * maximum amount of time (seconds) to sleep before starting a new subthread to scrape the next channel
              * accepts an `int` or `float`
                -> max_sleep=5 (default)
            `after_n_channels_pause_for_s` -
              * amount of time to sleep after scraping n channels
              * accepts a tuple of `(int, int)` or a tuple of `(int, float)`
                -> after_n_channels_pause_for_s=(20, 10)

        Use the following arguments to mute terminal logging of subthread status:
            `log_subthread_status_silently`
              * mutes logging when a subthread starts, ends, and how long the subthread takes to execute
              * accepts a `boolean`
                -> log_subthread_status_silently=False (default) OR log_subthread_status_silently=True
        Use the following arguments to mute terminal logging of subthread information:
            `log_subthread_status_silently`
              * mutes logging which channel each subthread is scraping and which output file the subthread writes to
              * accepts a `boolean`
                -> log_subthread_info_silently=False (default) OR log_subthread_info_silently=True
        '''
        print(
          '''
          NOTE:
          You should have no problems if you're updating the files for a channel you've already scraped, but you **might**
          encounter some problems if you're scraping channels for the first time.
          Specifically:
            -> If a channel you're scraping has THOUSANDS of videos, the browser needs to load all the HTML elements
               corresponding to the uploaded videos in memory, so if you have MULTIPLE threads going and all channels
               being concurrently scraped have thousands of videos, your machine might run out of memory!
            -> If you know a channel you're scraping for the first time has THOUSANDS of uploaded videos, it would
               be better to first scrape that channel individually using the `create_list_for(url)` method to create
               the file for that channel, and then use this multi-threaded method to update the file for that channel
               along with files for other channels!
              -> ALSO keep in mind that having many applications running while using yt_videos_list might still cause the
                 program to terminate before reaching the end of the page if your machine's overall memory usage gets too high
                 (look up page faults and memory swap for more information).
            -> NOTE that updating files for channels you've already scraped shouldn't have this problem
               (unless the channel uploaded thousands of videos since the last time you scraped it),
               since the threading overhead and memory required to render a couple hundred HTML video elements
               will be relatively low.
              -> Also note the program stops scrolling when **creating** a new file when new elements can't be loaded in
                 `scroll_pause_time * 2` seconds since the last page scroll, BUT when **updating** an existing file, the
                 program only stops scrolling when it scrolls down to a video that already exists in the file - no matter
                 how long it takes the program to do so (so the program is not required to finding new videos in
                 less than `scroll_pause_time * 2` seconds).\n\n\n\n
          '''
        )
        invalid_file_name_exception = f'''The options for the file_name argument are 'auto' or 'id', but you provided: '{file_name}'\nPlease rerun this method using file_name='auto' or file_name='id'\n\nFor more details about the difference between 'auto' and 'id', run:\n    >>> help(ListCreator.create_list_for)\n\n\n\n'''
        if file_name not in ('auto', 'id'): raise ValueError(invalid_file_name_exception)
        multiplier = max(0, max_sleep - min_sleep)
        modulo, seconds = after_n_channels_pause_for_s
        with open(path_to_channel_urls_file, mode='r', encoding='utf-8',  buffering=self.file_buffering) as txt_file, open(path_to_channel_urls_file.split('.')[0] + '.log', mode='a', encoding='utf-8',  buffering=self.file_buffering) as log_file:
            start = time.time()
            if log_subthread_info_silently: logging_locations = (log_file,)
            else:                           logging_locations = (log_file, sys.stdout)
            ThreadWithResult.log_thread_status = not log_subthread_status_silently
            ThreadWithResult.log_files = [log_file]
            log( '>' * 50 + 'STARTING  MULTI-THREADED PROGRAM' + '<' * 50, logging_locations)
            log(f'Iterating through all urls in {path_to_channel_urls_file} and scraping number_of_threads={number_of_threads} channels concurrently...\n\n', logging_locations)
            count            = 0
            running_threads  = set()
            finished_threads = set()
            def remove_finished_threads():
                # can't remove dead threads from running_threads set directly because of the following exception:
                # RuntimeError: Set changed size during iteration
                for thread in running_threads:
                    if not thread.is_alive():
                        channel_name, file_name = thread.result[1]
                        if hasattr(thread, 'result'): log(f'{thread.name} finished writing information for the "{channel_name}" channel to the {file_name} file', logging_locations)
                        else:                         log(f'{thread.name} did NOT finish scraping. See terminal output above for potential exceptions!',          logging_locations) # # AttributeError: 'ThreadWithResult' object has no attribute 'result'
                        finished_threads.add(thread)
                for thread in finished_threads:
                    running_threads.remove(thread)
                finished_threads.clear()
            for url in txt_file:
                url           = url.strip()
                formatted_url = url.split('#')[0].strip()
                if formatted_url == '':
                    # this line is either empty or entirely a comment
                    continue
                while len(running_threads) >= number_of_threads and all(thread.is_alive() for thread in running_threads):
                    time.sleep(1) # wait 1 second before checking to see if a previously running thread completed
                remove_finished_threads()
                if count % modulo == 0 and count > 0:
                    log(f'Scraped {count} channels, so sleeping for {seconds} seconds to seem less bot-like....', logging_locations)
                    time.sleep(seconds)
                sleep_time = min_sleep + (random.random() * multiplier)
                log(f'Sleeping for {sleep_time} seconds before starting next subthread....', logging_locations)
                time.sleep(sleep_time)
                thread = ThreadWithResult(target=self.create_list_for, args=(formatted_url, True, file_name))
                thread.start()
                count += 1
                log(f'{thread.name} scraping channel {count:>7}: {url}', logging_locations)
                running_threads.add(thread)
            log(f'Iterated through all urls in {path_to_channel_urls_file}!', logging_locations)
            while len(running_threads) > 0:
                log(f'Still running {[thread.name for thread in running_threads]} ...', logging_locations)
                time.sleep(10)
                remove_finished_threads()
            end = time.time()
            log(f'Finished executing all threads. It took {end - start} seconds to scrape all urls in {path_to_channel_urls_file}', logging_locations)
            log( '>' * 50 + 'COMPLETED MULTI-THREADED PROGRAM' + '<' * 50, logging_locations)
