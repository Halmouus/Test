#!/usr/bin/python3
with open("my_file_0.txt", 'r') as f:
    lines = f.readlines()  # Read all lines into a list

modified_lines = []
for line in lines:
    modified_lines.append(line)
    if "empty" in line:
        modified_lines.append("Checkpoint")

with open("my_file_0.txt", 'w') as f:
    f.writelines(modified_lines)  # Write the modified lines back to the file


