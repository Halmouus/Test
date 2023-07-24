#!/bin/bash
# This basic script that does the boring part for you..

# Just a basic prompt to avoid a mess..
confirm_prompt() {
    while true; do
        read -r -n 1 -s -p "Current directory is not sorting_algorithms. Are you sure you want to run the script? (y/n): " answer
        case "$answer" in
            "" ) echo "" ;; 
            [Yy] ) break ;;
            [Nn] ) echo -e "\nscript stopped"; exit ;;
            * ) echo -e "\nPlease type 'y' to continue or 'n' to abort." ;;
        esac
    done
}


if [ "$(basename "$(pwd)")" != "sorting_algorithms" ]; then
    confirm_prompt
fi

# Create the files
touch README.md sort.h print_array.c print_list.c 0-bubble_sort.c 0-O 1-insertion_sort_list.c \
 1-O 2-selection_sort.c 2-O 3-quick_sort.c 3-O 100-shell_sort.c 101-cocktail_sort_list.c \
 101-O 102-counting_sort.c 102-O 103-merge_sort.c 103-O 104-heap_sort.c 104-O \
 105-radix_sort.c 106-bitonic_sort.c 106-O 107-quick_sort_hoare.c 107-O 1000-sort_deck.c \
 deck.h
echo "0x1B. C - Sorting algorithms & Big O" > README.md

# Display number of successfully created files 
c_files=$(ls *.c | wc -l)
h_files=$(ls *.h | wc -l)
readme_files=$(ls README.md | wc -l)

echo -e "\n$c_files C files created successfully"
echo "$h_files header files created successfully"
echo "$readme_files README.md created successfully"

# Write content to sort.h
cat > sort.h << EOL
#ifndef SORT_H
#define SORT_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - Doubly linked list node
 *
 * @n: Integer stored in the node
 * @prev: Pointer to the previous element of the list
 * @next: Pointer to the next element of the list
 */
typedef struct listint_s

{
    const int n;
    struct listint_s *prev;
    struct listint_s *next;
} listint_t;

void print_array(const int *array, size_t size);
void print_list(const listint_t *list);
void bubble_sort(int *array, size_t size);
void insertion_sort_list(listint_t **list);
void selection_sort(int *array, size_t size);
void quick_sort(int *array, size_t size);
void shell_sort(int *array, size_t size);
void cocktail_sort_list(listint_t **list);
void counting_sort(int *array, size_t size);
void merge_sort(int *array, size_t size);
void heap_sort(int *array, size_t size);
void radix_sort(int *array, size_t size);
void bitonic_sort(int *array, size_t size);
void quick_sort_hoare(int *array, size_t size);

#endif
EOL
echo "sort.h written successfully"

# Write content to C files
for file in $(ls *.c | grep -v 'print_array.c' | grep -v 'print_list.c'\
 | grep -v '1000-sort_deck.c'); do
    name="${file#*-}"
    name="${name%.c}"
    if echo "$name" | grep -q "list"; then
        prototype="void ${name}(listint_t **list)"
    cat > $file << EOL
#include "sort.h"

/**
 * ${name} - sorts a doubly linked list of integers.
 * @list: doubly-linked list of integers to sort
 */

${prototype} {

}
EOL
echo "${name}.c written successfully"
    else
        prototype="void ${name}(int *array, size_t size)"
    cat > $file << EOL
#include "sort.h"

/**
 * ${name} - sorts an array of integers.
 * @array: array of integers to sort.
 * @size: size of the array.
 */

${prototype} {

}
EOL
echo "${name}.c written successfully"
    fi
    
done

# Write content to print_array.c
cat > print_array.c << EOL
#include <stdlib.h>
#include <stdio.h>

/**
 * print_array - Prints an array of integers
 *
 * @array: The array to be printed
 * @size: Number of elements in @array
 */
void print_array(const int *array, size_t size)
{
    size_t i;

    i = 0;
    while (array && i < size)
    {
        if (i > 0)
            printf(", ");
        printf("%d", array[i]);
        ++i;
    }
    printf("\n");
}
EOL
echo "print_array.c written successfully"

# Write content to print_list.c
cat > print_list.c << EOL
#include <stdio.h>
#include "sort.h"

/**
 * print_list - Prints a list of integers
 *
 * @list: The list to be printed
 */
void print_list(const listint_t *list)
{
    int i;

    i = 0;
    while (list)
    {
        if (i > 0)
            printf(", ");
        printf("%d", list->n);
        ++i;
        list = list->next;
    }
    printf("\n");
}
EOL
echo "print_list.c written successfully"
