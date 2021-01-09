#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<time.h>

int test = 52; // 검사할 숫자.
int rst = 0;
int depth = -1;

int w[6] = { 2,10,13,17,22,42 };
int monte[128] = { -1 };

bool promising(int index, int weight, int total) {

   if (weight + total >= test && (weight == test || weight + w[index + 1] <= test)) {

      return true;

   }

   return false;

}


void estimate(int weight, int total) {

   int m, mprod, t, numnodes;

   int v = 0;

   numnodes = 1;
   m = 1;
   mprod = 1;


   while (m != 0) {

      t = 0;

      if (monte[(2 * v) + 1] != -1) {
         t++;
         printf("monte L%  d \n", monte[(2 * v) + 1]);
      }

      if (monte[(2 * v) + 2] != -1) {
         t++;
         printf("monte R%  d \n", monte[(2 * v) + 2]);
      }
      

      depth++;

      mprod = mprod * m;

      numnodes = numnodes + mprod * t;

      m = 0;
      
      bool flag = false;
      

      if (monte[(2 * v) + 1] != -1 && promising(depth, monte[(2 * v) + 1], total) == true) {
         m++;
         flag = true;
      }

      if (monte[(2 * v) + 2] != -1 && promising(depth, monte[(2 * v) + 2], total) == true) {
         m++;

      }
      printf("m %d\n", m);

      if (m != 0) {
         if (m == 2) {
            
            int ran = rand() % 2 + 1;
         

            printf("ran %d\n", ran);
            
            v = 2 * v + ran;
            printf("v %d \n", v);
         
         }
         else {

            if (flag == true) {
               v = 2 * v + 1;
            }

            else {
               v = 2 * v + 2;
            }
         }


      }

   }
   printf("%d \n", numnodes);
}


void sum_of_sets(int index, int weight, int total, int include[], int monte_index) {

   

   if (promising(index, weight, total)) {
      monte[monte_index] = weight;
      //printf("weight = %d \n", weight);
      //printf("index = %d \n", index);
      //printf("\n");

      if (weight == test) {
         printf("답은  ");
         for (int i = 0; i < 6; i++) {
            if (include[i] != 0) {
               printf(" w%d ", i);

            }

         }
         printf("\n");
         printf("\n");
         printf("\n");
      }

      else {
         include[index + 1] = w[index + 1];

         sum_of_sets(index + 1, weight + w[index + 1], total - w[index + 1], include, ((2 * monte_index) + 1));

         include[index + 1] = 0;

         sum_of_sets(index + 1, weight, total - w[index + 1], include, ((2 * monte_index) + 2));

      }
   }
}





int main() {


   int include[6] = { 0 };

   int index = -1;
   int total = 0;
   int weight = 0;

   for (int i = 0; i < 6; i++) {

      total += w[i];

   }

   int monte_index = 0;
   for (int i = 0; i < 128; i++) {

      monte[i] = -1;

   }
   
   sum_of_sets(index, weight, total, include, monte_index);
   srand(time(NULL));
   printf("--------------------------------------\n");
   estimate(weight, total);

}