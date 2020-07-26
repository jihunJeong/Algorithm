#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_QUEUE_SIZE 10002
int size;
typedef struct queue* Queue;
typedef struct queue {
	int* array;
	int rear;
	int front;
}queue;

Queue CreateQueue();
void Enqueue(int num, Queue q);
int Dequeue(Queue q);

int main() {
	int n = 0;
	size = 0;
	scanf("%d", &n);
	Queue q = CreateQueue();

	while (n--) {
		char input[15];
		scanf("%s", input);
		if (!strcmp(input, "push")) {
			int temp = 0;
			scanf("%d", &temp);
			Enqueue(temp, q);
		}
		else if (!strcmp(input, "pop")) {
			int rst = Dequeue(q);
			if (rst == NULL) {
				printf("-1\n");
			}
			else {
				printf("%d\n", rst);
			}
		}
		else if (!strcmp(input, "size")) {
			printf("%d\n", size);
		}
		else if (!strcmp(input, "empty")) {
			if (size == 0) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
		}
		else if (!strcmp(input, "front")) {
			if (size == 0) {
				printf("-1\n");
			}
			else {
				printf("%d\n", q->array[q->front+1]);
			}
		}
		else if (!strcmp(input, "back")) {
			if (size == 0) {
				printf("-1\n");
			}
			else {
				printf("%d\n", q->array[q->rear]);
			}
		}
	}
	return 0;
}

Queue CreateQueue() {
	Queue q = (Queue)malloc(sizeof(queue));

	q->array = (int*)malloc(sizeof(int) * MAX_QUEUE_SIZE);
	q->rear = -1;
	q->front = -1;

	return q;
}

void Enqueue(int num, Queue q) {
	if (q->rear != MAX_QUEUE_SIZE - 1) {
		q->rear += 1;
		q->array[q->rear] = num;
		size++;
	}
	else {
		printf("Q is full\n");
	}
}

int Dequeue(Queue q) {
	int num = NULL;

	if (q->front < q->rear) {
		q->front += 1;
		num = q->array[q->front];
		q->array[q->front] = NULL;
		size--;
	}

	return num;
}