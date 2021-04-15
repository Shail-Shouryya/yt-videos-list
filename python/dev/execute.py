import sys
import time
import traceback
import contextlib

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support   import expected_conditions as EC

from . import program
from .download.selenium_webdriver_dependencies import download_all
from .download.windows_info                    import get_drive_letter
from .download.user_os_info                    import determine_user_os
from .notifications                            import Common, ModuleMessage, ScriptMessage
from .custom_logger                            import log


def logic(url, file_name, log_silently, txt, csv, markdown, reverse_chronological, headless, scroll_pause_time, user_driver, execution_type):
    common_message = Common()
    module_message = ModuleMessage()
    script_message = ScriptMessage()


    def verify_writing_to_at_least_one_file():
        if txt is False and csv is False and markdown is False:
            print(common_message.not_writing_to_any_files)
            print(module_message.not_writing_to_any_files_hint) if execution_type == 'module' else print(script_message.not_writing_to_any_files_hint)
            sys.exit() # the files already exist and the user doesn't want to overwrite either of them


    def process_url():
        try:
            channel_info = url.split('youtube.com/')[1]
            channel_type = channel_info.split('/')[0]
            channel      = channel_info.split('/')[1]
        except IndexError as error_message:
            common_message.display_url_error(error_message)
            traceback.print_exc()
            sys.exit()
        base_url     = 'https://www.youtube.com'
        videos       = 'videos'
        return f'{base_url}/{channel_type}/{channel}/{videos}'


    def check_driver():
        nonlocal user_driver
        if user_driver is None:
            print(module_message.running_default_driver) if execution_type == 'module' else print(script_message.running_default_driver)
            print(module_message.show_driver_options)    if execution_type == 'module' else print(script_message.show_driver_options)
            user_driver = 'firefox'
        if   'firefox' in user_driver: return webdriver.Firefox
        elif 'opera'   in user_driver: return webdriver.Opera
        elif 'chrome'  in user_driver: return webdriver.Chrome
        elif 'brave'   in user_driver: return configure_bravedriver
        elif 'edge'    in user_driver: return configure_edgedriver
        elif 'safari'  in user_driver: return configure_safaridriver
        else:
            print(common_message.invalid_driver)
            sys.exit()


    def open_user_driver():
        if headless is False:
            return seleniumdriver()
        else: # headless is True
            if   user_driver == 'firefox': return set_up_headless_firefoxdriver()
            elif user_driver == 'opera':   return set_up_headless_operadriver()
            elif user_driver == 'safari':  return set_up_headless_safaridriver()
            elif user_driver == 'chrome':  return set_up_headless_chromedriver()
            elif user_driver == 'brave':   return set_up_headless_bravedriver()
            elif user_driver == 'edge':    return set_up_headless_edgedriver()


    def set_up_headless_firefoxdriver():
        options = selenium.webdriver.firefox.options.Options()
        options.headless = True
        return seleniumdriver(options=options)

    def set_up_headless_operadriver():
        # Opera driver MRO: WebDriver -> OperaDriver -> selenium.webdriver.chrome.webdriver.WebDriver -> selenium.webdriver.remote.webdriver.WebDriver -> builtins.object
        # options = selenium.webdriver.chrome.options.Options()
        # options.headless = True
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        print(common_message.unsupported_opera_headless)
        return seleniumdriver(options=options)

    def set_up_headless_safaridriver():
        print(common_message.unsupported_safari_headless)
        return seleniumdriver()

    def set_up_headless_chromedriver():
        # options = selenium.webdriver.chrome.options.Options()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        return seleniumdriver(chrome_options=options)

    def set_up_headless_bravedriver():
        print(common_message.unsupported_brave_headless)
        return configure_bravedriver()

    def set_up_headless_edgedriver():
        print(common_message.unsupported_edge_headless)
        return configure_edgedriver()


    def configure_bravedriver():
        options = webdriver.ChromeOptions()
        if user_os == 'windows':
            drive  = get_drive_letter()
            options.binary_location = rf'{drive}:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
            executable_path         = rf'{drive}:\Windows\bravedriver.exe'
        else:
            options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
            executable_path         = '/usr/local/bin/bravedriver'
        # options.headless = True
        return webdriver.Chrome(options=options, executable_path=executable_path)

    def configure_edgedriver():
        # options = selenium.webdriver.remote.webdriver.WebDriver()
        if user_os == 'windows':
            drive  = get_drive_letter()
            # options.binary_location = rf'{drive}:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
            executable_path         = rf'{drive}:\Windows\msedgedriver.exe'
        else:
            # options.binary_location = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'
            executable_path         = '/usr/local/bin/msedgedriver'
            print(common_message.unsupported_edge)
            print(module_message.show_driver_options)
            sys.exit()
        # options.headless = True
        return webdriver.Edge(executable_path=executable_path)

    def configure_safaridriver():
        if user_os != 'macos':
            common_message.display_dependency_setup_instructions('safari', user_os)
            sys.exit()
        return webdriver.Safari()


    def show_user_how_to_set_up_selenium():
        if user_driver != 'safari':
            common_message.tell_user_to_download_driver(user_driver)
        common_message.display_dependency_setup_instructions(user_driver, user_os)


    def handle_opening_webdriver_exception(error_message):
        # selenium.common.exceptions.WebDriverException: Message: 'BROWSERdriver' executable needs to be in PATH. Please see https://................
        # for some reason this also catches selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of BROWSERDriver only supports BROWSER version ##
        nonlocal driver
        common_message.display_selenium_dependency_error(error_message)
        try:
            download_all()
            driver = open_user_driver()
        except selenium.common.exceptions.WebDriverException as same_error_message_again: # could not download the correct Selenium driver based on the user's OS and specified driver
            common_message.display_selenium_dependency_update_error(same_error_message_again)
            traceback.print_exc()
            show_user_how_to_set_up_selenium()
            common_message.display_unable_to_update_driver_automatically(user_driver)
            sys.exit()


    def run_scraper():
        with driver:
            driver.get(url)
            driver.set_window_size(780, 800)
            driver.set_window_position(0, 0)
            wait = selenium.webdriver.support.ui.WebDriverWait(driver, 9)
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, '//yt-formatted-string[@class="style-scope ytd-channel-name"]')))
            except selenium.common.exceptions.TimeoutException as error_message:
                common_message.display_selenium_unable_to_load_elements_error(error_message)
                traceback.print_exc()
                sys.exit()
            file_name = determine_file_name()
            with yield_logger(file_name) as logging_locations:
                log( '>' * 50 + 'STARTING PROGRAM' + '<' * 50, logging_locations)
                log(f'Now scraping {url} using the {user_driver}driver:', logging_locations)
                program.determine_action(url, driver, scroll_pause_time, reverse_chronological, file_name, txt, csv, markdown, logging_locations)
                program_end = time.perf_counter()
                total_time  = program_end - program_start
                log(f'This program took {total_time} seconds to complete.', logging_locations)
                log( '>' * 50 + 'PROGRAM COMPLETE' + '<' * 50, logging_locations)
        return file_name


    def determine_file_name():
        if file_name is not None:
            return file_name.strip('.csv').strip('.txt').strip('.md')
        else:
            channel_name = driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-channel-name"]').text.replace(' ', '')
            suffix       = 'reverse_chronological_videos_list' if reverse_chronological else 'chronological_videos_list'
            return f'{channel_name}_{suffix}'


    @contextlib.contextmanager
    def yield_logger(file_name):
        log_file = f'{file_name}.log'
        with open (log_file, 'a', encoding='utf-8') as output_location:
            if log_silently is True: yield (output_location,)
            else:                    yield (output_location, sys.stdout)


    verify_writing_to_at_least_one_file()
    user_os             = determine_user_os()
    url                 = process_url()
    seleniumdriver      = check_driver()
    program_start       = time.perf_counter()
    try:
        driver = open_user_driver()
    except selenium.common.exceptions.WebDriverException as error_message:
        handle_opening_webdriver_exception(error_message)
    return run_scraper()
