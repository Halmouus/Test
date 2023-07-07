#include "hash_tables.h"

/**
 * hash_table_print - prints  a hash table
 * @ht: hash table
 */
void hash_table_print(const hash_table_t *ht)
{
    unsigned long int index = 0;
    int count = 0;
    if (ht == NULL)
        return;
    printf("{");
    for (index = 0; index < ht->size; index++)
    {
        if (ht->array[index])
        {
           if (count)
           {
               printf(", ");
           }
            printf("'%s': '%s'", ht->array[index]->key, ht->array[index]->value);
            count++;
        }
                
    }
    printf("}\n");
    
}