#include "hash_tables.h"

/**
 * hash_table_print - prints  a hash table
 * @ht: hash table
 */
void hash_table_print(const hash_table_t *ht)
{
hash_node_t *temp = NULL;
unsigned long int index = 0;
int count = 0;
if (ht == NULL)
return;
printf("{");
for (index = 0; index < ht->size; index++)
{
temp = ht->array[index];
while (temp)
{
if (count)
{
printf(", ");
}
printf("'%s': '%s'", temp->key, temp->value);
count++;
temp = temp->next;
}
}
printf("}\n");
}
