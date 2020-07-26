#include<stdio.h>
#include<stdlib.h>

typedef long long ll;

int main() {

   //이진탐색은 기준으로 나눠가면서 하는게 포인트.
   
   //malloc에서 sizeof는 요소의 데이터타입.
   
   int n = 0, m = 0;
   ll max = 0, mid = 0, temp = 0;
   ll anw = 0;

   scanf("%d %d", &n, &m);
   
   int* array = (int*)malloc((sizeof(int) * n));
   
   for (int i = 0; i < n; i++) {
      
      scanf("%d", &array[i]);
      
      if (max < array[i]) {
         max = array[i];
      }
   }

   ll right = max;
   
   ll left = 0;

   while (left <= right) {


      mid = (left + right) / 2;
   
      temp = 0;

      //printf("%d %d\n", left, right);

      for (int i = 0; i < n; i++) {
         
         if (array[i] - mid > 0) {
            temp += array[i] - mid;
         }
      
      }
      

      if (temp >= m) {

         if (mid > anw) {
            anw = mid;
         //printf("%d\n", anw);
         }
         left = mid + 1;
         
      }
      else  {

          right = mid - 1;

      }


   }
   
   printf("%d\n", anw);
   
   free(array);

   return 0;

}
// 예제는 맞는데 제출하면 틀렸다고 뜸.