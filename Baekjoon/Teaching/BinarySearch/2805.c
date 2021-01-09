#include<stdio.h>
#include<stdlib.h>

typedef long long ll;

int main() {

   //����Ž���� �������� �������鼭 �ϴ°� ����Ʈ.
   
   //malloc���� sizeof�� ����� ������Ÿ��.
   
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
// ������ �´µ� �����ϸ� Ʋ�ȴٰ� ��.