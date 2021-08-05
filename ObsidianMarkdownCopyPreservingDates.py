# Btach Change Obsidian Markdown Notes preseving dates
# Script to change any Obsidian Notes whilest preserving the creation and modification dates

# works on Mac OS. Uses the shell touch command under the covers

import os
import datetime
import time
import calendar
from subprocess import call


# ---------------------------------------------
# Set the paths for the input and output folder
# ---------------------------------------------
VAULT_PATH = "YOUR INPUT FOLDER"  # Input folder
OUTPUT_VAULT_PATH = "YOUR OUTPUT FOLDER"  # Output Folder

# ------------------------------------
# Set the files that should be ignored
# ------------------------------------

special_notes = [
    ".DS_Store",
    ".obsidian",
]


lines = []
actions = []

def modify_obsidian_markdown_notes(filepath):

    # return the names of the files in the directory data as a list
    list_of_files = os.listdir(filepath)

    for file in list_of_files:

        # if not markdown file skip it
        if not file.endswith('.md'):
            continue

        # ignore special notes
        if file in special_notes:
            continue

        # grab created and modified dates
        stat = os.stat(filepath+file)
        print stat.st_birthtime
        modifieddate = time.strftime(
            "%Y-%m-%d", time.gmtime(os.path.getmtime("{}".format(filepath+file))))
        modifieddatefortouch = time.strftime(
            "%Y%m%d%H%M", time.gmtime(os.path.getmtime("{}".format(filepath+file))))
        createddate = time.strftime(
            "%Y-%m-%d", time.gmtime(stat.st_birthtime))
        createddatefortouch = time.strftime(
            "%Y%m%d%H%M", time.gmtime(stat.st_birthtime))

        file_link = file.replace(".md", "")
        
        updated_file = ""
        
        f = open(filepath+file, "r")

        # modify markdown file line by line
        lines = f.readlines()
        for line in lines:
            line = line[:-1]


            found = False

            if line.find("#done") > 1:
                found = True

            if found:

                # copy the original line
                newline = line
                
                #----------------------------------------------------------------
                # make changes to newline HERE
                #----------------------------------------------------------------
                
                updated_file += newline+'\n'
            else:
                updated_file += line+'\n'

        f.close()

        result = open(OUTPUT_VAULT_PATH+file, "w")
        result.write(updated_file)
        result.close()

        # Fix created and modified dates
        command = 'touch -t ' + createddatefortouch + \
            ' ' + '"'+OUTPUT_VAULT_PATH+file_link+'.md"'.replace("'", "")
        call(command, shell=True)
        command = 'touch -mt ' + modifieddatefortouch + \
            ' ' + '"'+OUTPUT_VAULT_PATH+file_link+'.md"'
        call(command, shell=True)


########################## MAIN ENTRY POINT #################
modify_obsidian_markdown_notes(VAULT_PATH)
