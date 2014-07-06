chiastic
========

This short script is designed to detect basic chiastic sentence structures (A, B, B, A) in plain text files. Usage:

<b>python chiastic.py ['-s' for single mode, '-b' for bulk mode] [word limit as integer] [file to search (single mode only)]</b>

To specify words to ignore, create a list called 'ignore.txt' in the same directory as this script. To use in bulk mode, create a list of target files called 'targets.txt' (when running in bulk mode, Chiastic will only output scores).
