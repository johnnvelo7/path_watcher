# path_watcher
**CTF TOOL:** 
Monitor a directory for file creation and closing after writing events. It displays the contents of the file after it's written.
This is useful for CTF's where you need to dynamically analyse a malware especially if the malware is creating and deleting a file (flag.txt) in microseconds.

#TAKE NOTE: This program currently works for Linux OS at the moment, but I'll update this for windows too soon.

## HOW TO USE:

Install the required package (pyinotify):
```pip install pyinotify```
or 
```pip3 install pyinotify```

RUN the program
```python3 monitor.py -h``` for help
```python3 monitor.py``` to run normally

