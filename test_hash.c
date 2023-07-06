#include <stdio.h>
#include <stdlib.h>

#define CAPACITY 50000 // Size of the HashTable.

unsigned long hash_function(char* str)
{
    unsigned long i = 0;

    for (int j = 0; str[j]; j++)
        i += str[j];

    return i % CAPACITY;
}

int main() {
    char str[10] = "gdgda";
    printf("index of %s : %ld\n", str, hash_function(str));
    
    return 0;
}