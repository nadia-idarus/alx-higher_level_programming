#include <stdlib.h>
#include <stdio.h>

#define INITIAL_CAPACITY 10

/* Define the structure for a hash node */
typedef struct hash_node {
    char *key;
    char *value;
    struct hash_node *next;
} hash_node_t;

/* Define the structure for the hash table */
typedef struct hash_table {
    unsigned long int size;
    hash_node_t **array;
} hash_table_t;

/* Hash function to calculate the index for a given key */
unsigned long int hash_function(const char *key, unsigned long int size) {
    unsigned long int hash = 0;
    int c;
    
    while ((c = *key++)) {
        hash = c + (hash << 6) + (hash << 16) - hash;
    }
    
    return hash % size;
}

/* Function to create a new hash table */
hash_table_t *hash_table_create(unsigned long int size) {
    hash_table_t *new_table;
    unsigned long int i;

    /* Allocate memory for the table structure */
    new_table = (hash_table_t *)malloc(sizeof(hash_table_t));
    if (new_table == NULL) {
        return NULL;  /* Memory allocation failed */
    }

    /* Allocate memory for the array of hash nodes */
    new_table->array = (hash_node_t **)malloc(sizeof(hash_node_t *) * size);
    if (new_table->array == NULL) {
        free(new_table);
        return NULL;  /* Memory allocation failed */
    }

    /* Initialize the array with NULL pointers */
    for (i = 0; i < size; i++) {
        new_table->array[i] = NULL;
    }

    new_table->size = size;  /* Set the size of the hash table */

    return new_table;
}

int main() {
    unsigned long int size = INITIAL_CAPACITY;
    hash_table_t *my_hash_table = hash_table_create(size);

    if (my_hash_table != NULL) {
        printf("Hash table created successfully!\n");
    } else {
        printf("Error creating hash table.\n");
    }

    return 0;
}

