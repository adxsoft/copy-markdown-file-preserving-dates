# copy-markdown-file-preserving-dates

I created this script so that creation and modification dates would be preserved when I was copying markdown files from one Obsidian Vault (a folder of markdown notes) to another vault.

This python script will copy markdown files from folder A to folder B.

You can modify each markdown file by adding your own modification code as indicated in the comments of the script.

The updated file will be placed in folder B with the SAME creation and modification dates as the original markdown file in Folder A.

<i>Note. The script uses shell command and touch command under the covers so it runs on Mac OSX. It may work on Linux (as it has touch command) but will not work on Windows as far as I know.</i>
