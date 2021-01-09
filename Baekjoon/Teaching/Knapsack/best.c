#include < stdio.h>
#include <stdbool.h>

#define MAX_N 1024

int W = 9;
int include[5] = { 0 };
int numset[5] = { 0 };
int bestset[5] = { 0 };
int maxprofit = 0;
int w[5] = { 2,5,7,3,1 };
int p[5] = { 20,30,35,12,3 };
int n = 5;

typedef struct node {

   int level;
   int profit;
   int weight;
   int bound; // float인데 int로 선언함 나눠 떨어지니까.

}Node;

typedef struct heap {
    int arr[MAX_N];
    int size;
} heap;
 
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
void initHeap(heap *hp) {
    hp->size = 0;
}
void insert(heap* hp,int data) {
    int here = ++hp->size;
     
    while ((here!=1)&&(data<hp->arr[here/2])) {
        hp->arr[here] = hp->arr[here / 2];
        here /= 2;
    }
    hp->arr[here] = data;
}
 
int deleteData(heap *hp) {
    if (hp->size == 0) return -1;
    int ret = hp->arr[1];
    hp->arr[1]=hp->arr[hp->size--];
    int parent = 1;
    int child;
 
    while (1) {
        child = parent * 2;
        if (child + 1 <= hp->size && hp->arr[child]>hp->arr[child + 1])
            child++;
 
        if (child>hp->size||hp->arr[child] > hp->arr[parent]) break;
         
        swap(&hp->arr[parent], &hp->arr[child]);
        parent = child;
    }
     
    return ret;
     
}
int main() {
    heap hp;
    initHeap(&hp);
     
    insert(&hp, 3);


void initialize(Q* q) {
   q->front = -1;
   q->rear = -1;
   q->size = 0;
}

int bound(Node* u) {
   int j, k;
   int totweight;
   int result;

   if (u->weight = W) {
      return 0;
   }
   else {
      result = u->profit;
      j = u->level + 1;
      totweight = u->weight;
      while ((j <= n) && (totweight + w[j] <= W)) {
         totweight = totweight + w[j];
         result = result + p[j];
         j++;
      }
      k = j;
      if (k <= n) {
         result = result + (W - totweight) * p[k] / w[k];
         return result;
      }


   }


}
void enque(Node* node) {



}

Node* deque() {

}


bool isempty(Q* q) {
   if (q->size == 0) {
      return true;
   }

   return false;
}



void best_search() {

   Node* u = (Node*)malloc(sizeof(Node));
   Node* v = (Node*)malloc(sizeof(Node));
   Q* pq;
   
   initialize(pq);

   v->level = 0;
   v->profit = 0;
   v->weight = 0;
   v->bound = bound(v);

   //maxprofit은 전역변수로 빼줌.

   pq.enque(v);

   while (isempty(q) != 0) {
      v = pq.deque();
      if (v->bound > maxprofit) {
         u->level = v->level + 1;
         u->profit = v->profit + p[u->level];
         u->weight = v->weight + w[u->level];
         if ((u->weight <= W) && (u->pro > maxprofit)) {
            maxprofit = u->profit;
         }

         u->bound = bound(u);
         if (bound(u) > maxprofit) {
            pq.enque(u);
         }
         
         u->weight = v->weight;
         u->profit = v->profit;
         u->bound = v->bound;

         if (u->bound > maxprofit) {
            pq.enque(u);
         }

      }


   }



}





int main() {



}