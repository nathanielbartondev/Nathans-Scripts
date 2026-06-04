# Thought capture (thcap) takes a sentence or phrase that's on the user's mind and
# appends it to a text file for later review. Great for addressing distracting thoughts
# while you work!
# 
# For convenient use, it is recommended that you add an alias for this script to your
# system. For instance, on a Linux system, you could alias "thcap" to this script in
# your .bashrc file.

# grants access to command-line args
import sys
import os

# The "bucket" file where all stray thoughts are collected
bucket_path = os.path.join("/home", "nathan", "Documents", "thought-bucket.txt")
sub_cmd = sys.argv[1]

if sub_cmd == "help":
    print("""
    Usage: thcap [SUB-COMMAND]

    SUB-COMMANDS
    help        Displays this help and exits.
    dump        "Dumps" the thought bucket to stdout, displaying its contents.

    Any other argument that is not a reserved sub-command will be treated as a
    stray thought, and will thus be added to the thought-bucket file.
          """)
elif sub_cmd == "dump":
    bucket = open(bucket_path, "r")
    thoughts = bucket.read()
    bucket.close()
    print(thoughts)
else:
    bucket = open(bucket_path, "a")
    bucket.write(sub_cmd + "\n")
    bucket.close()
