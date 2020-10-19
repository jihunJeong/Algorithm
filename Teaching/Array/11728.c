#include <stdio.h>
#include<string.h>
#include<stdlib.h> 


int main() {

    int n = 0;
    int m = 0;

    scanf("%d %d", &n, &m);

    int a = n + m;

    int* array1 = (int*)malloc((sizeof(int) * n));
    int* array2 = (int*)malloc((sizeof(int) * m));
    int* rstarray = (int*)malloc((sizeof(int) * a));

    for (int i = 0; i < n; i++) {
        scanf("%d", &array1[i]);
    }
    for (int i = 0; i < m; i++) {
        scanf("%d", &array2[i]);
    }

    int index1 = 0;
    int index2 = 0;
    int rstindex = 0;
    while (1) {
        if (index1 == n || index2 == m) {
            break;
        }

        if (array1[index1] <= array2[index2]) {
            rstarray[rstindex] = array1[index1];
            rstindex++;
            index1++;
        }
        else {
            rstarray[rstindex] = array2[index2];
            rstindex++;
            index2++;
        }

    }

    for (int i = index1; i < n; i++) {
        rstarray[rstindex] = array1[i];
        rstindex++;
    }

    for (int i = index2; i < m; i++) {
        rstarray[rstindex] = array2[i];
        rstindex++;
    }

    for (int i = 0; i < a-1; i++) {
        printf("%d ", rstarray[i]);
    }
    printf("%d\n", rstarray[a - 1]);

    free(array1);
    free(array2);
    free(rstarray);

    return 0;

}