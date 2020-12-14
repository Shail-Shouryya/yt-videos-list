import os

from test_shared                          import run_tests_for, determine_path_slash
formatted_pip = 'pip' if determine_path_slash() == '\\' else 'pip'
os.system(f'{formatted_pip} install .')


from yt_videos_list.download.windows_info import get_drive_letter
from yt_videos_list.download.user_os_info import determine_user_os



def remove_dependencies():
    if determine_user_os() == 'windows':
        drive = get_drive_letter()
        geckodriver_path  = rf'{drive}:\Windows\geckodriver.exe'
        operadriver_path  = rf'{drive}:\Windows\operadriver.exe'
        chromedriver_path = rf'{drive}:\Windows\chromedriver.exe'
        bravedriver_path  = rf'{drive}:\Windows\bravedriver.exe'
        msedgedriver_path = rf'{drive}:\Windows\msedgedriver.exe'
    else:
        geckodriver_path  = r'/usr/local/bin/geckodriver'
        operadriver_path  = r'/usr/local/bin/operadriver'
        chromedriver_path = r'/usr/local/bin/chromedriver'
        bravedriver_path  = r'/usr/local/bin/bravedriver'
        msedgedriver_path = r'/usr/local/bin/msedgedriver'
    if os.path.exists(geckodriver_path):  os.remove(geckodriver_path)
    if os.path.exists(operadriver_path):  os.remove(operadriver_path)
    if os.path.exists(chromedriver_path): os.remove(chromedriver_path)
    if os.path.exists(bravedriver_path):  os.remove(bravedriver_path)
    if os.path.exists(msedgedriver_path): os.remove(msedgedriver_path)


def main():
    remove_dependencies()
    browsers   = ['firefox', 'opera', 'chrome', 'brave']
    run_tests_for(browsers)


# add these later
# lc_firefox.headless = True
# lc_opera.headless = True
# lc_safari.headless = True
# lc_chrome.headless = True


if __name__ == '__main__':
    main()
