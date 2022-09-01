import os

from .               import selenium_linux, selenium_macos, selenium_windows
from .user_os_info   import determine_user_os
from ..notifications import Common


COMMON_MESSAGE = Common()
APPLICATION_NAME = {
    'macos': {
        # 'driver': 'browser_name'
        'firefox':  'Firefox',
        'opera':    'Opera',
        'chrome':   'Google Chrome',
        'brave':    'Brave Browser',
        'edge':     'Microsoft Edge'
    },
    'linux': {
        'firefox':  '',
        'opera':    '',
        'chrome':   ''
    },
    'windows': {
        'firefox':  'Mozilla Firefox',
        'opera':    'Opera',
        'chrome':   'Chrome',
        'brave':    'Brave-Browser',
        'edge':     'Edge'
    }
}


def download_specific_dependency(driver, user_os):
    selenium_user_os = globals()[f'selenium_{user_os}']
    browser          = APPLICATION_NAME[user_os][driver]
    if selenium_user_os.verify_browser_exists(browser):
        full_version_number = selenium_user_os.get_browser_version(browser)
        COMMON_MESSAGE.display_browser_found_information(browser, full_version_number)
        major_version = full_version_number.split('.')[0]
        execute_download_command(driver, user_os, major_version)
    else:
        COMMON_MESSAGE.display_browser_not_found_information(browser, user_os)

def download_all_dependencies(user_os):
    print(COMMON_MESSAGE.automated_driver_update)
    for driver in APPLICATION_NAME[user_os]:
        download_specific_dependency(driver, user_os)

def execute_download_command(driver, user_os, major_version):
    # indexed values in reverse order to avoid having to map every version to a different element every time a new driver/browser version comes out since all the values get shifted down by 2 with new additions to the top of the list
    row_in_list = {
        'firefox': {
            '111':-11,
            '110':-11,
            '109':-11,
            '108':-11,
            '107':-11,
            '106':-11,
            '105':-11,
            '104':-11,
            '103':-11,
            '102':-11,
            '101':-11,
            '100':-11,
            '99': -11,
            '98': -11,
            '97': -11,
            '96': -11,
            '95': -11,
            '94': -11,
            '93': -11,
            '92': -11,
            '91': -9,
            '90': -9,
            '89': -9,
            '88': -9,
            '87': -9,
            '86': -7,
            '85': -7,
            '84': -7,
            '83': -5,
            '82': -5,
            '81': -3,
            '80': -3,
            '79': -3,
            '78': -3,
            '77': -1,
            '76': -1,
            '75': -1,
            '74': -1,
            '73': -1,
            '72': -1,
            '71': -1,
            '70': -1,
            '69': -1,
            '68': -1,
            '67': -1,
            '66': -1,
            '65': -1,
            '64': -1,
            '63': -1,
            '62': -1,
            '61': -1,
            '60': -1,
        },
        'opera': {
            '111':-75,
            '110':-75,
            '109':-75,
            '108':-75,
            '107':-75,
            '106':-75,
            '105':-75,
            '104':-75,
            '103':-75,
            '102':-75,
            '101':-75,
            '100':-75,
            '99': -75,
            '98': -75,
            '97': -75,
            '96': -75,
            '95': -75,
            '94': -75,
            '93': -75,
            '92': -75,
            '91': -75,
            '90': -75,
            '89': -75,
            '88': -73,
            '87': -71, # there was no operadriver release specifically for Opera Stable 85 (chromium version 101)
            '86': -71, # there was no operadriver release specifically for Opera Stable 85 (chromium version 100)
            '85': -71,
            '84': -69,
            '83': -67,
            '82': -65,
            '81': -63,
            '80': -61,
            '79': -59,
            '78': -57,
            '77': -55,
            '76': -53,
            '75': -51,
            '74': -49,
            '73': -47,
            '72': -45,
            '71': -43,
            '70': -41,
            '69': -39,
            '68': -37,
            '67': -35,
            '66': -33,
            '65': -31,
            '64': -29,
            '63': -27,
            '62': -25,
            '61': -23, # there was no operadriver release specifically for Opera 61
            '60': -23,
            '59': -21, # there was no operadriver release specifically for Opera 59
            '58': -21,
            '57': -19,
            '56': -17,
            '55': -15,
            '54': -13,
            '53': -11,
            '52': -9,
            '51': -7, # there was no operadriver release specifically for Opera 51
            '50': -7,
            '49': -5,
            '48': -3,
            '47': -1, # there was no operadriver release specifically for Opera 47
            '46': -1
        },
        'chrome': {
            '111':-59,
            '110':-59,
            '109':-59,
            '108':-59,
            '107':-59,
            '106':-59,
            '105':-59,
            '104':-59,
            '103':-59,
            '102':-59,
            '101':-59,
            '100':-59,
            '99': -59,
            '98': -59,
            '97': -59,
            '96': -57,
            '95': -55,
            '94': -53,
            '93': -51,
            '92': -49,
            '91': -47,
            '90': -45,
            '89': -43,
            '88': -41,
            '87': -39,
            '86': -37,
            '85': -35,
            '84': -33,
            '83': -31,
            '82': -23, # there was no Google Chrome release for version 82, but just in case
            '81': -29,
            '80': -27,
            '79': -25,
            '78': -23,
            '77': -21,
            '76': -19,
            '75': -17,
            '74': -15,
            '73': -13,
            '72': -11,
            '71': -11,
            '70': -9,
            '69': -7,
            # '69': -5 # covered by release 2.44
            '68': -3,
            '67': -1
        },
        'brave': {
            '111':-51,
            '110':-51,
            '109':-51,
            '108':-51,
            '107':-51,
            '106':-51,
            '105':-51,
            '104':-51,
            '103':-51,
            '102':-49,
            '101':-47, # there was no operadriver release specifically for Opera Stable 85 (chromium version 101) - therefore no bravedriver v.101.#.####.## since bravedriver just uses the operadriver binary renamed as ** bravedriver **
            '100':-47, # there was no operadriver release specifically for Opera Stable 85 (chromium version 100) - therefore no bravedriver v.100.#.####.## since bravedriver just uses the operadriver binary renamed as ** bravedriver **
            '99': -47,
            '98': -45,
            '97': -43,
            '96': -41,
            '95': -39,
            '94': -37,
            '93': -35,
            '92': -33,
            '91': -31,
            '90': -29,
            '89': -27,
            '88': -25,
            '87': -23,
            '86': -21,
            '85': -19,
            '84': -17,
            '83': -15,
            '82': -13, # there was no Brave Browser release for version 82, but just in case
            '81': -13,
            '80': -11,
            '79': -9,
            '78': -7,
            '77': -5,
            '76': -3,
            '75': -1
        },
        'edge': {
            '111':-39,
            '110':-39,
            '109':-39,
            '108':-39,
            '107':-39,
            '106':-39,
            '105':-39,
            '104':-39,
            '103':-39,
            '102':-39,
            '101':-39,
            '100':-39,
            '99': -39,
            '98': -39,
            '97': -37,
            '96': -35,
            '95': -33,
            '94': -31,
            '93': -29,
            '92': -27,
            '91': -25,
            '90': -23,
            '89': -21,
            '88': -19,
            '87': -17,
            '86': -15,
            '85': -13,
            '84': -11,
            '83': -9,
            '82': -7,
            '81': -5,
            '80': -3,
            '79': -1
        }
    }
    row = row_in_list[driver][major_version]
    print(f'Now downloading the corresponding selenium driver for {driver} version {major_version} on {user_os}:')
    print(f'{COMMON_MESSAGE.driver_downloads_for_os[driver][user_os][row-1]} #')
    print(f'{COMMON_MESSAGE.driver_downloads_for_os[driver][user_os][row]}')
    os.system(COMMON_MESSAGE.driver_downloads_for_os[driver][user_os][row])

def download_all():
    user_os = determine_user_os()
    download_all_dependencies(user_os)
