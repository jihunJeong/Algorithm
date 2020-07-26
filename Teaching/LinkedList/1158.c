#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	struct Node* next;
	int data;
} Node;

Node* head;
Node* current;

void ninsert(int num) {
	Node* node = (Node*)malloc(sizeof(Node));
	node->data = num;
	node->next = head->next;
	head->next = node;
}

int ndelete(int k) {
	for (int i = 0; i < k - 1; i++) {
		current = current->next;
	}

	Node* node = (Node*)malloc(sizeof(Node));
	node = current->next;
	current->next = node->next;
	
	return node->data;
}

int main() {
	int n = 0, k = 0;
	scanf("%d %d", &n, &k);
	head = (Node*)malloc(sizeof(Node));
	Node* node1 = (Node*)malloc(sizeof(Node));
	
	head->next = node1;
	node1->data = n;
	node1->next = head;
	current = head;

	for (int i = n-1; i > 0; i--) {
		ninsert(i);
	}

	node1->next = head->next;
	if (k == 1) {
		current = node1;
	}
	printf("<");
	n = n - 1;
	while (n--) {
		printf("%d, ", ndelete(k));
	}

	printf("%d>\n", current->data);
}