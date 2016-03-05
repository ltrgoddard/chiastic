#!/usr/bin/env python

# Chiastic
# by Louis Goddard <louisgoddard@gmail.com>

# This short script is designed to detect basic chiastic sentence structures (A, B, B, A) in
# plain text files. Usage: "python chiastic.py ['-s' for single mode, '-b' for bulk mode]
# [word limit as integer] [file to search (single mode only)]". To specify words to ignore,
# create a list called 'ignore.txt' in the same directory as this script. To use in bulk mode,
# create a list of target files called 'targets.txt' (when running in bulk mode, Chiastic will
# only output scores).


import sys
import re
import os.path
from string import punctuation
from operator import itemgetter

# Check mode

mode = str(sys.argv[1])

if mode == "-s" and sys.argv[3]:

    # If single mode, get target file, strip punctuation and convert to list

    file = open(str(sys.argv[3])).read().lower()
    words = re.sub("[^\w]", " ", file).split()

elif mode == "-b":

    # If bulk mode, get targets list

    targets = open("targets.txt").read().split()

else:

    sys.exit("Error! Invalid argument.")

# Get word limit from command line argument

limit = int(sys.argv[2])

# Check if an ignore list exists; if it does, read it, strip punctuation and convert to list

ignoreExists = os.path.isfile("ignore.txt")

if ignoreExists:

    list = open("ignore.txt").read().lower()
    ignore = re.sub("[^\w]", " ", list).split()

# Initialize main variables

check = 0
start = 0
end = 1
counter = 0
files = 1

if mode == "-b":

    files = len(targets)


# Start scanning target file

while counter < files:

    # If in bulk mode, get the next file in the list and strip and convert it
    
    if mode == "-b":

        file = open(str(targets[counter])).read().lower()
            words = re.sub("[^\w]", " ", file).split()

    while start < len(words):

        # Skip words in ignore list

        if ignoreExists and words[start] in ignore:

            start += 1
            end = start + 1

        else:

            while end < len(words) and end < start + limit:

                # Catch matches where the words is longer than two characters

                if words[start] == words[end] and len(words[start]) > 2:

                    # If the ignore list exists, check for sub-matches excluding ignore words

                    if ignoreExists:

                        stripped = [word for word in words[start+1:end] if word not in ignore]
                
                        if len(stripped) > len(set(stripped)):        
            
                            # If in single mode, output the results

                            if mode == "-s":
                                
                                print start,
                                print end,
                                print ":",
                                print words[start:end+1]

                            check += 1
                
                        else:

                            break
                
                    # If the ignore list doesn't exist, check for sub-matches anyway

                    else:

                        if len(words[start+1:end]) > len(set(words[start+1:end])):

                            # If in single mode, output the results

                            if mode == "-s":

                                print start,
                                print end,
                                print ":",
                                print words[start:end+1]

                            check += 1

                        else:

                            break

                    start += 1
                    break

                end += 1

        start += 1
        end = start + 1

    # Output the overall score(s), as long as neither 'length' nor 'check' is zero

    if mode == "-b":

        print targets[counter],
    
    if len(words) > 0 and check > 0:

        print len(words) / check

    else:

        print "No matches!"

    
    counter += 1
