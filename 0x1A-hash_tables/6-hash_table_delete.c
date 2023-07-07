#include "hash_tables.h"

/**
 * hash_table_delete - deletes a hash table
 * @ht: hash table to delete
 */
void hash_table_delete(hash_table_t *ht)
{
    unsigned long int index;
    hash_node_t *temp = NULL;
    if (ht == NULL)
        return;
    for (index = 0; index < ht->size; index++)
    {
        temp = ht->array[index];
        while(temp)
        {
            free(temp->key);
            free(temp->value);
            temp = temp->next;
        }
        free(ht->array[index]);
    }
    free(ht);
}