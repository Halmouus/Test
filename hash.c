#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

// Define the structure for each element in the hash table
typedef struct {
    int key;
    int value;
} Entry;

// Define the hash table
Entry hashtable[SIZE];

// Hash function to calculate the index for a given key
int hash(int key) {
    return key * SIZE + 12;
}

// Function to insert a key-value pair into the hash table
void insert(int key, int value) {
    int index = hash(key);
    printf("Inserting value: %d at index: %d of key: %d\n", value, index, key);
    hashtable[index].key = key;
    hashtable[index].value = value;
}

// Function to retrieve the value associated with a given key
int get(int key) {
    int index = hash(key);
    printf("Retreiving value of index: %d of key: %d\n", index, key);
    return hashtable[index].value;
}

void print_hash(Entry *hashtable) {
    int key = 0;
    
}
// Main function to test the hash table
int main() {
    // Insert some key-value pairs
    insert(1, 10);
    insert(2, 55);
    insert(10, 30);

    // Retrieve values using keys
    printf("%d\n", get(1));
    printf("%d\n", get(2));
    printf("%d\n", get(10));

    return 0;
}
