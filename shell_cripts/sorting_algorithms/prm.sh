#!/bin/bash

# Function to display the confirmation prompt
confirm_prompt() {
    read -p "Current directory is not sorting_algorithms. Are you sure you want to run the script? (y/n): " answer
    case "$answer" in
        [Yy]* ) ;;
        [Nn]* ) echo "script stopped"; exit ;;
        * ) echo "Please type 'y' to continue or 'n' to abort."; confirm_prompt ;;
    esac
}

# Check if the current directory name is "sorting_algorithms"
if [ "$(basename "$(pwd)")" != "sorting_algorithms" ]; then
    confirm_prompt
fi

# Rest of your script goes here
# ...

# For example, you can list the files in the current directory
ls
