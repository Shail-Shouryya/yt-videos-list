## Best Practices
#### [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/) - [Chris Beams](https://chris.beams.io/); Aug 30, 2014
  - Keep in mind:
    - [This](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
    - [has](https://www.git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#_commit_guidelines)
    - [all](https://github.com/torvalds/subsurface-for-dirk/blob/master/README.md#contributing)
    - [been](http://who-t.blogspot.co.at/2009/12/on-commit-messages.html)
    - [said](https://github.com/erlang/otp/wiki/writing-good-commit-messages)
    - [before](https://github.com/spring-projects/spring-framework/blob/30bce7/CONTRIBUTING.md#format-commit-messages).
  1. Separate subject from body with a blank line
  2. Limit the subject line to 50 characters
  3. Capitalize the subject line
  4. Do not end the subject line with a period
  5. Use the imperative mood in the subject line
    - **A properly formed Git commit subject line should always be able to complete the following sentence**:
    - If applied, this commit will ***your subject line here***
    - For example:
      - If applied, this commit will ***refactor subsystem X for readability***
      - If applied, this commit will ***update getting started documentation***
      - If applied, this commit will ***remove deprecated methods***
      - If applied, this commit will ***release version 1.0.0***
      - If applied, this commit will ***merge pull request #123 from user/branch***
    - Notice how this doesn’t work for the other non-imperative forms:
      - If applied, this commit will ***fixed bug with Y***
      - If applied, this commit will ***changing behavior of X***
      - If applied, this commit will ***more fixes for broken stuff***
      - If applied, this commit will ***sweet new API methods***
  6. Wrap the body at 72 characters
  7. Use the body to explain what and why vs. how

## References
- [Difference between webdriver.firefox.marionette & webdriver.gecko.driver](https://stackoverflow.com/questions/43272919/difference-between-webdriver-firefox-marionette-webdriver-gecko-driver) - Stack Overflow
- [What are the benefits of using Marionette FirefoxDriver instead of the old Selenium FirefoxDriver for a Selenium tester?](https://stackoverflow.com/questions/38916650/what-are-the-benefits-of-using-marionette-firefoxdriver-instead-of-the-old-selen/38917100#38917100) - Stack Overflow
- [selenium.common.exceptions.SessionNotCreatedException: Message: Unable to find a matching set of capabilities with GeckoDriver, Selenium and Firefox](https://stackoverflow.com/questions/52002958/selenium-common-exceptions-sessionnotcreatedexception-message-unable-to-find-a) - Stack Overflow

- Put check for `user_driver is None` first since you can't iterate over `None` as you can iterate over strings. This comes up in the check_driver() method in execute.py
  - `TypeError: argument of type 'NoneType' is not iterable`
- [selenium.common.exceptions](https://selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html)
- running as a module (as of commit 2dbc5a15ab83a79aeeb884a106062ef2b1f52c76):
```
python3 -m yt_videos_list
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py:125: RuntimeWarning: 'yt_videos_list.__main__' found in sys.modules after import of package 'yt_videos_list', but prior to execution of 'yt_videos_list.__main__'; this may result in unpredictable behaviour
  warn(RuntimeWarning(msg))
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/yt_videos_list/__main__.py", line 103, in <module>
    main()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/yt_videos_list/__main__.py", line 100, in main
    script.create_list_for()
NameError: name 'script' is not defined
```

- [Python packaging: get Development Status from version string](https://stackoverflow.com/questions/24475318/python-packaging-get-development-status-from-version-string) - Stack Overflow
- [Build Your First pip Package](https://dzone.com/articles/executable-package-pip-install) - DZone: Big Data Zone, by Deepak Kumar; Sep. 19, 2018
  - build: build package information.
  - dist: Contains your .whl file. A WHL file is a package saved in the Wheel format, which is the standard built-package format used for Python distributions. You can directly install a .whl file using pip install some\_package.whl on your system
  - project.egg.info: An egg package contains compiled bytecode, package information, dependency links, and captures the info used by the setup.py test command when running tests.*
- [Python: Creating a pip installable package](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/) - Python for HPC: Community Materials, Stephen Hudson (Software Developer at Argonne)
- [Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.io/) - PyPA » Python Packaging User Guide »
- [An Overview of Packaging for Python](https://python-packaging-user-guide.readthedocs.io/overview/) - PyPA » Python Packaging User Guide »
- [setup.py](https://github.com/pypa/sampleproject/blob/master/setup.py) - [pypa/sampleproject](https://github.com/pypa/sampleproject) GitHub Repo
- *[Classifiers](https://pypi.org/classifiers/)*
- [raw classifiers in text](https://test.pypi.org/pypi?%3Aaction=list_classifiers)
- [install_requires vs requirements files](https://packaging.python.org/discussions/install-requires-vs-requirements/) - PyPA » Python Packaging User Guide » Discussions »
- [pip 19.3.dev0 documentation User Guide](https://pip.pypa.io/en/latest/user_guide/#requirements-files) - PyPA » pip 19.3.dev0 documentation »
- [PEP 440 -- Version Identification and Dependency Specification](https://www.python.org/dev/peps/pep-0440/) - Python>>> Python Developer's Guide>>> PEP Index>>> PEP 440 -- Version Identification and Dependency Specification
- [Python setuptools.find_packages() Examples](https://www.programcreek.com/python/example/10688/setuptools.find_packages) - programcreek
- [Building and Distributing Packages with Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html) - setuptools 41.2.0 documentation »
- [What is “where” argument for in setuptools.find_packages?](https://stackoverflow.com/questions/51286928/what-is-where-argument-for-in-setuptools-find-packages) - Stack Overflow
- [find_packages](http://code.nabla.net/doc/setuptools/api/setuptools/setuptools.find_packages.html) - setuptools
- [Licenses & Standards](https://opensource.org/licenses) - Open Source Initiative
  - Open source licenses are licenses that comply with the [Open Source Definition](https://opensource.org/osd) — in brief, they allow software to be freely used, modified, and shared. To be approved by the Open Source Initiative (also known as the OSI), a license must go through the [Open Source Initiative's license review process](https://opensource.org/approval).
- [ImportError: “unknown location”](https://forum.learncodethehardway.com/t/importerror-unknown-location/2034) - learncodethehardway
- [Traps for the Unwary in Python’s Import System](https://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html) - Docs » Python Concepts » Traps for the Unwary in Python’s Import System
  - READ THIS!
- [How to create a Python Package with __init__.py](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html) - Timothy Bramlett
- after reading the previous 2, read these
  - [ValueError: attempted relative import beyond top-level package](https://stackoverflow.com/questions/35166821/valueerror-attempted-relative-import-beyond-top-level-package) - Stack Overflow
  - [Relative imports for the billionth time](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912) - Stack Overflow
- [What is __init__.py for?](https://stackoverflow.com/questions/448271/what-is-init-py-for) - Stack Overflow
    - Files named __init__.py are used to mark directories on disk as Python package directories. If you have the files

    ```
    mydir/spam/__init__.py
    mydir/spam/module.py
    ```
    - and mydir is on your path, you can import the code in module.py as

    ``` import spam.module ```
    - or

    ```
    from spam import module
    ```
    - If you remove the __init__.py file, Python will no longer look for submodules inside that directory, so attempts to import the module will fail.

    - The __init__.py file is usually empty, but can be used to export selected portions of the package under more convenient name, hold convenience functions, etc. Given the example above, the contents of the init module can be accessed as

    ```
    import spam
    ```
    - based on [What is __init__.py used for?](https://effbot.org/pyfaq/what-is-init-py-used-for.htm) - effbot

```
Files named __init__.py are used to mark directories on disk as a Python package directories. If you have the files

mydir/spam/__init__.py
mydir/spam/module.py
and mydir is on your path, you can import the code in module.py as:

import spam.module
or

from spam import module
If you remove the __init__.py file, Python will no longer look for submodules inside that directory, so attempts to import the module will fail.

The __init__.py file is usually empty, but can be used to export selected portions of the package under more convenient names, hold convenience functions, etc. Given the example above, the contents of the __init__ module can be accessed as

import spam
```
- [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/) - PyPA » Python Packaging User Guide » Guides »

### closure scoping
- [Don't understand why UnboundLocalError occurs (closure) [duplicate]](https://stackoverflow.com/questions/9264763/dont-understand-why-unboundlocalerror-occurs-closure) - Stack Overflow
- [How do JavaScript closures work?](https://stackoverflow.com/questions/111102/how-do-javascript-closures-work) - Stack Overflow
- [Local (?) variable referenced before assignment [duplicate]](https://stackoverflow.com/questions/11904981/local-variable-referenced-before-assignment) - Stack Overflow
  - [Python 3: UnboundLocalError: local variable referenced before assignment [duplicate]](https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment) - Stack Overflow
  - [Assigning to variable from parent function: “Local variable referenced before assignment” [duplicate]](https://stackoverflow.com/questions/8934772/assigning-to-variable-from-parent-function-local-variable-referenced-before-as?noredirect=1&lq=1) - Stack Overflow
- [UnboundLocalError on local variable when reassigned after first use](https://stackoverflow.com/questions/370357/unboundlocalerror-on-local-variable-when-reassigned-after-first-use) - Stack Overflow
- [Don't understand why UnboundLocalError occurs (closure) [duplicate]](https://stackoverflow.com/questions/9264763/dont-understand-why-unboundlocalerror-occurs-closure) - Stack Overflow
  - Python doesn't have variable declarations, so it has to figure out the [scope](http://docs.python.org/3.3/tutorial/classes.html#python-scopes-and-namespaces) of variables itself. It does so by a simple rule: If there is an assignment to a variable inside a function, that variable is considered local.[1](http://docs.python.org/3.3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python) Thus, the line
  - `counter += 1`
  - implicitly makes `counter` local to `increment()`. Trying to execute this line, though, will try to read the value of the local variable `counter` before it is assigned, resulting in an `[UnboundLocalError](http://docs.python.org/3.3/library/exceptions.html#UnboundLocalError)`.[2](http://docs.python.org/3.3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value)
  - If `counter` is a global variable, the [global](http://docs.python.org/3.3/reference/simple_stmts.html#the-global-statement) keyword will help. If `increment()` is a local function and `counter` a local variable, you can use [nonlocal](http://docs.python.org/3.3/reference/simple_stmts.html#the-nonlocal-statement) in Python 3.x.
  - Sven Marnach answered Feb 13 '12 at 17:15
    - --> python 3 docs has a [faq page on why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value](https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value) via [unboundlocalerror-local-variable-l-referenced-before-assignment-python – here](http://stackoverflow.com/questions/21456739/unboundlocalerror-local-variable-l-referenced-before-assignment-python) May 4 '14 at 7:19
    - --> A note that caught me out, I had a variable declared at the top of the file that I can read inside a function without issue, however to write to a variable that I have declared at the top of the file, I had to use global. – mouckatron Feb 6 '18 at 14:35
    - --> A more in-depth explanation: [docs.python.org/3.3/reference/…](https://docs.python.org/3.3/reference/executionmodel.html#naming-and-binding). Not only can assignments bind names, so can imports, so you may also get UnboundLocalError from a statement that uses an unbounded imported name. Example: `def foo(): bar = deepcopy({'a':1}); from copy import deepcopy; return bar`, then `from copy import deepcopy; foo()`. The call succeeds if the local import `from copy import deepcopy` is removed. – Yibo Yang Jun 27 '18 at 16:00
<br>

  - You need to use the [global statement](http://docs.python.org/py3k/reference/simple_stmts.html#the-global-statement) so that you are modifying the global variable counter, instead of a local variable:
```shell
counter = 0

def increment():
  global counter
  counter += 1

increment()
```
  - If the enclosing scope that `counter` is defined in is not the global scope, on Python 3.x you could use the [nonlocal statement](http://docs.python.org/py3k/reference/simple_stmts.html#the-nonlocal-statement). In the same situation on Python 2.x you would have no way to reassign to the nonlocal name `counter`, so you would need to make `counter` mutable and modify it:
```shell
counter = [0]

def increment():
  counter[0] += 1

increment()
print counter[0]  # prints '1'
```
  - Andrew Clark answered Feb 13 '12 at 17:13
<br>

  - To answer the question in your subject line,* yes, there are closures in Python, except they only apply inside a function, and also (in Python 2.x) they are read-only; you can't re-bind the name to a different object (though if the object is mutable, you can modify its contents). In Python 3.x, you can use the [nonlocal](https://docs.python.org/3/reference/simple_stmts.html?highlight=nonlocal#nonlocal) keyword to modify a closure variable.
```shell
def incrementer():
    counter = 0
    def increment():
        nonlocal counter
        counter += 1
        return counter
    return increment

increment = incrementer()

increment()   # 1
increment()   # 2
```
  - The question origially asked about closures in Python.
  - kindall answered Feb 13 '12 at 17:21
<br>

  - The reason of why your code throws an `UnboundLocalError` is already well explained in other answers.
  - But it seems to me that you're trying to build something that works like [itertools.count()](http://docs.python.org/library/itertools.html#itertools.count).
  - So why don't you try it out, and see if it suits your case:
```python
>>> from itertools import count
>>> counter = count(0)
>>> counter
count(0)
>>> next(counter)
0
>>> counter
count(1)
>>> next(counter)
1
>>> counter
count(2)
```
  - Rik Poggi answered Feb 13 '12 at 17:31
<br>

  - Python has lexical scoping by default, which means that although an enclosed scope can access values in its enclosing scope, it cannot modify them (unless they're declared [global](http://docs.python.org/3.3/reference/simple_stmts.html#the-global-statement) with the global keyword).
  - A closure binds values in the enclosing environment to names in the local environment. The local environment can then use the bound value, and even reassign that name to something else, but it can't modify the binding in the enclosing environment.
  - In your case you are trying to treat `counter` as a local variable rather than a bound value. Note that this code, which binds the value of x assigned in the enclosing environment, works fine:
```shell
>>> x = 1

>>> def f():
>>>  return x

>>> f()
1
```
  - Chris Taylor answered Feb 13 '12 at 17:21
<br>

  - To modify a global variable inside a function, you must use the global keyword.
  - When you try to do this without the line
  - `global counter`
  - inside of the definition of increment, a local variable named counter is created so as to keep you from mucking up the counter variable that the whole program may depend on.
  - Note that you only need to use global when you are modifying the variable; you could read counter from within increment without the need for the global statement.
  - chucksmash answered Feb 13 '12 at 17:13
- [How to Do a Binary Search in Python](https://realpython.com/binary-search-python/) - [Real Python](https://realpython.com/), [Bartosz Zaczyński](https://realpython.com/binary-search-python/#author), Mar 16, 2020
- [Python Scope & the LEGB Rule: Resolving Names in Your Code](https://realpython.com/python-scope-legb-rule/) - [Real Python](https://realpython.com/), Leodanis Pozo Ramos;  Mar 18, 2020
  - [Discovering Unusual Python Scopes](https://realpython.com/python-scope-legb-rule/#discovering-unusual-python-scopes)
  - [Using Scope Related Built-In Functions](https://realpython.com/python-scope-legb-rule/#using-scope-related-built-in-functions)
    - `globals()`
    - `locals()`
    - `dir()`
    - `vars()`

### getattr()
- [Python getattr()](https://www.programiz.com/python-programming/methods/built-in/getattr) - [Programiz](https://www.programiz.com/): [Python Programming](https://www.programiz.com/python-programming) > [Methods](https://www.programiz.com/python-programming/methods) > [Built in](https://www.programiz.com/python-programming/methods/built-in)

### File seeking
- [Why can't I call read() twice on an open file?](https://stackoverflow.com/questions/3906137/why-cant-i-call-read-twice-on-an-open-file) - Stack Overflow
  - Calling `read()` reads through the entire file and leaves the read cursor at the end of the file (with nothing more to read). If you are looking to read a certain number of lines at a time you could use `readline()`, `readlines()` or iterate through lines with `for line in handle:`.
  - To answer your question directly, once a file has been read, with `read()` you can use `seek(0)` to return the read cursor to the start of the file (docs are [here](http://docs.python.org/2.4/lib/bltin-file-objects.html)). If you know the file isn't going to be too large, you can also save the `read()` output to a variable, using it in your `findall` expressions.
  - Ps. Dont forget to close the file after you are done with it ;)
<br>

  - Every open file has an associated position.
  - When you `read()` you read from that position. For example `read(10)` reads the first 10 bytes from a newly opened file, then another `read(10)` reads the next 10 bytes. `read()` without arguments reads all of the contents of the file, leaving the file position at the end of the file. Next time you call `read()` there is nothing to read.
  - You can use `seek` to move the file position. Or probably better in your case would be to do one `read()` and keep the result for both searches.
<br>

  - `read()` ***consumes***. So, you could ***reset*** the file, or ***seek*** to the start before re-reading. Or, if it suites your task, you can use `read(n)` to consume only `n` bytes.
- trying `open('somefile', '+')` when the `+` isn't preceeded with another value results in:
  - `ValueError: Must have exactly one of create/read/write/append mode and at most one plus`


### figuring out if a variable exists
- commit a756485b66e0c06831ff9b4b42a8b0cc36a38721
```python
'myVar' in vars()
'myVar' in vars(__builtins__)
'myVar' in locals()
'myVar' in globals()
hasattr(obj, 'attr_name')
```
- [Determine if variable is defined in Python [duplicate]](https://stackoverflow.com/questions/1592565/determine-if-variable-is-defined-in-python) - Stack Overflow
- [Easy way to check that a variable is defined in python? [duplicate]](https://stackoverflow.com/questions/750298/easy-way-to-check-that-a-variable-is-defined-in-python) - Stack Overflow
- [How do I check if a variable exists?](https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists) - Stack Overflow


### copying a file
- see commit bdba91c3fcd584e2fc1b49a3398a168637f17e3d
- [How do I copy a file in Python?](https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python) - Stack Overflow


|      Function      | Copies metadata | Copies permissions | Can use buffer | Destination may be directory |
|:------------------:|:---------------:|:------------------:|:--------------:|:----------------------------:|
|     shutil.copy    |        No       |         Yes        |       No       |              Yes             |
|   shutil.copyfile  |        No       |         No         |       No       |              No              |
|    shutil.copy2    |       Yes       |         Yes        |       No       |              Yes             |
| shutil.copyfileobj |        No       |         No         |       Yes      |              No              |


### renaming a pre-existing file (Windows problem)
- see commit edd2e21d612af1164afd52666b280d24bc8b21c0
  - FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'yt_videos_list_temp.txt' -> 'CoreySchafer_videos_list.txt'
- [Force Overwrite in Os.Rename](https://stackoverflow.com/questions/8107352/force-overwrite-in-os-rename) - Stack Overflow
  - Since Python 3.3, there is now a standard cross-platform solution, `os.replace`:
    - Rename the file or directory src to dst. If dst is a directory, `OSError` will be raised. If **dst exists and is a file, it will be replaced silently if the user has permission**. The operation may fail if src and dst are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).
    - **Availability: Unix, Windows.**
    - New in version 3.3.
    - However, contrary to the documentation, on Windows it's not guaranteed to be atomic (in Python 3.4.4). That's because [internally](https://hg.python.org/cpython/file/v3.4.4/Modules/posixmodule.c#l4289) it uses `[MoveFileEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365240%28v=vs.85%29.aspx)` on Windows, which doesn't make such a guarantee.
  - https://docs.python.org/3/library/os.html#os.replace
<br>

  - On unix systems `rename` overwrites the destination if exists (because the operation is guaranteed to be atomic).
<br>

  - On Unix, if dst exists and is a file, it will be replaced silently if the user has permission. The operation may fail on some Unix flavors if src and dst are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement). **On Windows, if dst already exists, OSError will be raised even if it is a file; there may be no way to implement an atomic rename when dst names an existing file**. http://docs.python.org/library/os.html#os.rename
- [Error [183] when using python os.rename](https://stackoverflow.com/questions/8990725/error-183-when-using-python-os-rename) - Stack Overflow
- [WindowsError: [Error 183] Cannot create a file when that file already exists #13](https://github.com/kfogel/OneTime/) - [kfogel/OneTime](https://github.com/kfogel/OneTime/issues/13)
- [os.Rename() Causing Issues on Windows #4510](https://github.com/certbot/certbot/issues/4510) - [certbot/certbot](https://github.com/certbot/certbot/)

### write problems on Windows
- see the following
  - commit 63cb9660887627aa3f28c3385d23d9d775977d23
  - commit fc278e3af1a944940996d2c5a164f8ed82184cf8
  - commit 1ed71c6ca78c59f5d1329fddaee5963a0f8828d9
- added
  - `with open('output.csv', 'w+', newline='', encoding='utf-8') as f:`
  - `with open('output.csv', 'r+', newline='', encoding='utf-8') as f:
- [CSV in Python adding an extra carriage return, on Windows](https://stackoverflow.com/questions/3191528/csv-in-python-adding-an-extra-carriage-return-on-windows/29116560#29116560)
  - interesting: "Note that if you use DictWriter, you will have a new line from the open function and a new line from the writerow function. You can use newline='' within the open function to remove the extra newline."
  - this would explain why setting `newline=''` in the `open` method worked:
    - "If `newline=''` is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on platforms that use `\r\n` linendings on write an extra `\r` will be added. It should always be safe to specify `newline=''`, **since the csv module does its own (universal) newline handling**."
  - another workaround:
  - You can introduce the `lineterminator='\n'` parameter in the csv writer command.
  - `writer = csv.writer(stream, delimiter=delimiter, quoting=csv.QUOTE_NONE, quotechar='',  lineterminator='\n')`

### locating things/operating system
- [When to use os.name, sys.platform, or platform.system?](https://stackoverflow.com/questions/4553129/when-to-use-os-name-sys-platform-or-platform-system) - Stack Overflow
- [How to retrieve a module's path?](https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path) - Stack Overflow

### truthy/falsy versus True and False
- [What is Truthy and Falsy? How is it different from True and False?](https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false) - Stack Overflow
