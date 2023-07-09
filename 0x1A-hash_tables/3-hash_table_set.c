#include "hash_tables.h"

/**
 * hash_table_set - adds an element to the hash table.
 * @ht: hash table you want to add or update the key/value to
 * @key: the key. can not be an empty string
 * @value: value associated with the key. must be duplicated.
 * can be an empty string
 * Return: 1 if it succeeded, 0 otherwise
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
unsigned long int index;
hash_node_t *element, *temp;
if (ht == NULL || key == NULL || key[0] == '\0' || value == NULL)
return (0);
element = malloc(sizeof(hash_node_t));
if (element == NULL)
return (0);
element->key = malloc(strlen(key) + 1);
if (element->key == NULL)
{
free(element);
return (0);
}
strcpy(element->key, key);
element->value = malloc(strlen(value) + 1);
if (element->value == NULL)
{
free(element->key);
free(element);
return (0);
}
strcpy(element->value, value);
element->next = NULL;
index = key_index((const unsigned char *)key, ht->size);
if (ht->array[index] == NULL)
{
ht->array[index] = element;
return (1);
}
temp = ht->array[index];
while (temp)
{
if (strcmp(temp->key, key) == 0)
{
strcpy(temp->value, value);
free(element->key);
free(element->value);
free(element);
return (1);
}
temp = temp->next;
}
element->next = ht->array[index];
ht->array[index] = element;
return (1);
}
