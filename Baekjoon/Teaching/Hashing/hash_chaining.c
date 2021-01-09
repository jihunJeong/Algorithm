#include <stdio.h>
#include <iostream>
#define MAX_HASH 10
#define HASH_KEY(key) key%MAX_HASH
 
using namespace std;
 
typedef struct Node
{
    int id;
    Node* hashNext;
}Node;
 
Node* hashTable[MAX_HASH];
 
int main()
{
 
    return 0;
}


void  AddHashData(int key, Node* node)
{
    int hash_key = HASH_KEY(key);
    if (hashTable[hash_key] == NULL)
    {
        hashTable[hash_key] = node;
    }
    else
    {
        node->hashNext = hashTable[hash_key];
        hashTable[hash_key] = node;
    }
}


Node* FindHashData(int id)
{
    int hash_key = HASH_KEY(id);
    if (hashTable[hash_key] == NULL)
        return NULL;
 
    if (hashTable[hash_key]->id == id)
    {
        return hashTable[hash_key];
    }
    else
    {
        Node* node = hashTable[hash_key];
        while (node->hashNext)
        {
            if (node->hashNext->id == id)
            {
                return node->hashNext;
            }
            node = node->hashNext;
        }
    }
    return  NULL;
}

int main()
{
    int saveidx[101] = { 0, };
    for (int i = 0; i < 100; i++)
    {
        Node* node = (Node*)malloc(sizeof(Node));
        node->id = rand() % 1000;
        node->hashNext = NULL;
        AddHashData(node->id, node);
        saveidx[i] = node->id;
    }
    PrintAllHashData();
 
 
    for (int i = 0; i < 50 ; i++)
    {
        DelHashData(saveidx[i]);
    }
    PrintAllHashData();
 
    for (int i = 50; i < 100; i++)
    {
        DelHashData(saveidx[i]);
    }
    PrintAllHashData();
    return 0;
 
}