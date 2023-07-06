#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

struct Node {
    char name[20];
    int grade;
    struct Node* next;
};

struct Node* hashTable[MAX_SIZE];

int hash(char* name) {
    int sum = 0;
    for (int i = 0; name[i] != '\0'; i++) {
        sum += name[i];
    }
    return sum % MAX_SIZE;
}

void add_grade(char* name, int grade) {
    int index = hash(name);
    // Create a new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    strcpy(newNode->name, name);
    newNode->grade = grade;
    newNode->next = NULL;

    // Add the node to the linked list at the hash index
    if (hashTable[index] == NULL) {
        // First node in the list
        hashTable[index] = newNode;
    } else {
        // Traverse the list and append the node at the end
        struct Node* curr = hashTable[index];
        while (curr->next != NULL) {
            curr = curr->next;
            printf("Index = %d\n", index);
        }
        curr->next = newNode;
    }
}

int get_grade(char* name) {
    int index = hash(name);
    // Search for the name in the linked list at the hash index
    struct Node* curr = hashTable[index];
    while (curr != NULL) {
        if (strcmp(curr->name, name) == 0) {
            printf("Index = %d\n", index);
            return curr->grade;
        }
        curr = curr->next;
    }
    return -1; // Name not found
}

int main() {
    // Initialize the hash table
    for (int i = 0; i < MAX_SIZE; i++) {
        hashTable[i] = NULL;
    }

    add_grade("Bbo", 85);
    add_grade("Bob", 92);
    add_grade("Charlie", 78);

    printf("This grade: %d\n", get_grade("Bbo")); // Output: Bbo's grade: 85
    printf("This grade: %d\n", get_grade("Bbo")); // Output: Ale's grade: 85
    printf("This grade: %d\n", get_grade("Bob")); // Output: Ale's grade: 85
    printf("This grade: %d\n", get_grade("Bob")); // Output: Ale's grade: 85
    printf("This grade: %d\n", get_grade("Charlie")); // Output: Ale's grade: 85
    printf("This grade: %d\n", get_grade("Charlie")); // Output: Ale's grade: 85

    return 0;
}
