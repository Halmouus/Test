#!/bin/bash

# Basic prompter (still incomplete. Insert an additinal \n if input is \n)
prompter() {
    while true; do
        read -n 1 -p "$1" answer
        case "$answer" in
            [Yy] ) return 0 ;;
            [Nn] ) return 1 ;;
            * ) echo "" ;;
        esac
    done
}

# Checks if readme exists
readme_file=$(find . -maxdepth 1 \( -iname 'README.md' -o -iname 'README.txt' -o -iname 'readme' \) -type f -print -quit)

if [ -n "$readme_file" ]; then
    readme_file=$(basename "$readme_file")
    echo "A readme file ($readme_file) already exists in the current directory."

else
    # Create the readme
    if prompter "It appears the current directory doesn't have a README.md. Do you want to create one? (y/n): "; then
        # Create README.md and prompt for content (Incomplete and quite buggy with code command)
        echo -e "\nWrite the content of your README file:"
        read -r content
        echo "$content" > README.md
        echo "README.md created successfully!"
    else
        echo -e "\nREADME.md creation aborted."
    fi
fi
