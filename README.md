# copy-markdown-file-preserving-dates

I created this script so that creation and modification dates would be preserved when I was copying markdown files from one Obsidian Vault (a folder of markdown notes) to another vault on Mac OSX.

This python script will copy markdown files from folder A to folder B on Mac OSX

You can modify each markdown file by adding your own modification code as indicated in the comments of the script.

The updated file will be placed in folder B with the SAME creation and modification dates as the original markdown file in Folder A.

<i>Note. The script uses shell command and touch command under the covers and it only runs on Mac OSX. 
  
Note. Windows and Linux will not run this script as Windows handles updating creation times completely differently and Linux does not have creation dates.
