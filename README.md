# clean_folder
GoIT homework 7

### to install `clean-folder` package:

* clone this repository
* browse in terminal to folder which contain `setup.py`
* use `pip install .` or `pip install -e .` command in terminal


### for sorting folder use:

command `clean-folder folder_to_sort` or

`python3 -m clean_folder folder_to_sort` in terminal

after installing `clean-folder` package

if `folder_to_sort` is not given, current folder will be sorted

functions in `clean.py` recursively scans given 'folder' and:
* adds all directories' paths to `FOLDERS`
* adds files' paths to proper lists (`IMAGES`, `VIDEO`, `DOCS`, `MUSIC`, `ARCHIVES` or `MY_OTHER`)based on file extension
* adds all encountered extensions to `KNOWN_EXTENSIONS` or `UNKNOWN_EXTENSIONS` according to `REGISTERED_EXTENSIONS`
* sorts files in the given `folder_to_sort` according to the `REGISTERED_EXTENSIONS` in `clean_folder/clean.py`