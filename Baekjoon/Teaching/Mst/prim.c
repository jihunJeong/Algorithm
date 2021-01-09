#include <stdio.h>
#include <stdlib.h>

#define infi 10000

typedef struct set {
   
   int x;
   
   int y;

}st;

void pirm(int n, int w[9][9]) {
   
   int vnear = 0; // 그 정점에서 가장 가까운 인덱스

   int nearest[9] = { 0 }; // 확장가능성이 있는 정점의 인덱스
   
   int distance[9] = { 0 }; // 그것의 거리

   for (int i = 2; i <= n; i++) {
         nearest[i] = 1; // v1과 모든 정점부터 보겠다.
         distance[i] = w[1][i]; //각 정점부터 v1까지의 가중치
   }
    idx = 1
   while (idx <= n - 1) {
      
      int min = infi;
      
      for (int i = 2; i <= n; i++) {
         
         if (0 <= distance[i] &&  distance[i] <= min) {
            min = distance[i]; // 정점에 대해서 가중치(distance)를 조사해 가장 가중치가 인접(vnear)을 찾아냄
            vnear = i;
         }
      
      }
      
      //int [0][0] = { { i,vnear } }; // vnear로 가중치 최소를 찾았다면,,, 근데 어디서 최소인지를 알아야하지 않나,,?

      distance[vnear] = -1;

      for (int i = 2; i <= n; i++) {
         if (w[i][vnear] < distance[i]){
            distance[i] = w[i][vnear];
            nearest[i] = vnear; // 이부분 
            }
      }
      idx++;
   }

}

void make_set(int x, int y) {
   
   st* st;

   st->x = x;

}

void kruskal(int n,int w[9][9]) {


   for (int i = 0; i < n; i++) {

   }
}

   





int main() {

   int weight[9][9] = {
      {0,0,0,0,0,0,0,0},
      {0,0,11,9,8,infi,infi,infi,infi},
      {0,11,0,3,infi,8,8,infi,infi},
      {0,9,3,0,15,infi,12,1,infi},
      {0,8,infi,15,0,infi,infi,10,infi},
      {0,infi,8,infi,infi,0,7,infi,4},
      {0,infi,8,12,infi,7,0,infi,5},
      {0,infi,infi,1,10,infi,infi,0,2},
      {0,infi,infi,infi,infi,4,5,2,0}
   };

   for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
         printf("%d ", weight[i][j]);
      }
      printf("\n");
   }


}