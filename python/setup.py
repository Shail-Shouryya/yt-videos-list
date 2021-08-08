# https://pypi.org/classifiers/
# https://test.pypi.org/pypi?%3Aaction=list_classifiers
# https://github.com/pypa/sampleproject/blob/master/setup.py
# https://packaging.python.org/guides/distributing-packages-using-setuptools/
from setuptools import setup, find_packages


with open('README.md', mode='r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name                          = 'yt_videos_list',
    version                       = '0.6.0',
    description                   = 'YouTube bot to make a YouTube videos list (including all video titles and URLs uploaded by a channel) with end-to-end web scraping - no API tokens required. 🌟 Star this repo if you found it useful! 🌟',
    long_description              = long_description,
    long_description_content_type = 'text/markdown',
    url                           = 'https://github.com/slow-but-steady/yt-videos-list/tree/main/python',
    author                        = 'slow-but-steady',
    author_email                  = 'yt.videos.list@gmail.com',
    license                       = 'Apache License 2.0',


    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Free for non-commercial use',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Database :: Front-Ends',
        'Topic :: Home Automation',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Multimedia :: Video',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    keywords='YouTube videos URL scraping automation Selenium csv txt macos windows linux',


    # http://code.nabla.net/doc/setuptools/api/setuptools/setuptools.find_packages.html
    # https://stackoverflow.com/questions/51286928/what-is-where-argument-for-in-setuptools-find-packages
    packages=find_packages(exclude=['*dev*']),
    # packages=find_namespace_packages(include=['ship']),
    # package_dir={'':'src'},


    python_requires  = '>=3.6.*, <4',
    install_requires = [ # Optional
        'selenium>=3.141.0, <4',
        'save_thread_result==0.0.7'
    ],
    # https://packaging.python.org/discussions/install-requires-vs-requirements/


    # If there are data files included in your packages that need to be installed, specify them here.
    # If using Python 2.6 or earlier, then these have to be included in MANIFEST.in as well.
    package_data = {  # Optional
        # 'sample': ['package_data.dat'],
    },
    # Although 'package_data' is the preferred approach, in some case you may need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional


    # To provide executable scripts, use entry points in preference to the "scripts" keyword.
    # Entry points provide cross-platform support and allow `pip` to create the appropriate form of executable for the target platform.
    # For example, the following would provide a command called `yt_videos_list` which executes the code in the module `__main__` from this package when invoked directly from the command line:
    # entry_points={  # Optional
    #    'console_scripts': [
    #        'yt_videos_list=yt_videos_list:__main__',
    #    ],
    # },


    project_urls = {
        'Bug Reports':  'https://github.com/slow-but-steady/yt-videos-list/issues',
        'PyPi Funding': 'https://donate.pypi.org',
        'Source':       'https://github.com/slow-but-steady/yt-videos-list/tree/main/python'
    },
)
