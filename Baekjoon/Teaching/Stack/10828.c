#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define arraySize 10002

typedef struct stack* Stack;
Stack s;
typedef struct stack {
	int* array;
	int size;
	int top;
}stack;

Stack CreateStack();
Stack MakeEmptyStack(Stack s);
int IsEmpty(Stack s);
void Push(int x, Stack s);
int Pop(Stack s);
void DeleteStack(Stack s);

int main()
{
	int n = 0;
	scanf("%d", &n);
	s = CreateStack();

	while (n--) {
		char input[15];
		scanf("%s", input);
		if (!strcmp(input, "push")) {
			int temp = 0;
			scanf("%d", &temp);
			Push(temp, s);
		}
		else if (!strcmp(input, "pop")) {
			int rst = Pop(s);
			if (rst == NULL) {
				printf("-1\n");
			}
			else {
				printf("%d\n", rst);
			}
		}
		else if (!strcmp(input, "size")) {
			printf("%d\n", s->top + 1);
		}
		else if (!strcmp(input, "empty")) {
			if (s->top == -1) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
		}
		else if (!strcmp(input, "top")) {
			if (s->top == -1) {
				printf("-1\n");
			}
			else {
				printf("%d\n", s->array[s->top]);
			}
		}
	}
	DeleteStack(s);
	return 0;
}

Stack CreateStack() {
	Stack s = (Stack)malloc(sizeof(stack));

	s->size = arraySize;
	s->top = -1;
	s->array = (int*)malloc(sizeof(int) * arraySize);

	return s;
}

Stack MakeEmptyStack(Stack s) {
	int i;

	s->top = -1;

	for (i = 0; i < sizeof(s->array); i++) {
		s->array[i] = NULL;
	}

	return s;
}

int IsEmpty(Stack s) {
	if (s->top == -1) {
		return 1;
	}
	else {
		return 0;
	}
}

void Push(int x, Stack s) {
	s->top++;
	s->array[s->top] = x;
}

int Pop(Stack s) {
	if (IsEmpty(s) == 1) {
		return 0;
	}
	else {
		int ch;

		ch = s->array[s->top];
		s->array[s->top] = NULL;
		s->top--;
		return ch;
	}
}

void DeleteStack(Stack s) {
	free(s);
}