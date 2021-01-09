#include<stdio.h>
#include<stdlib.h>

int main() {

    int n = 0;
    int max = 0;
    int m = 0;
    int all = 0;
    int rst = 0;
    int mid = 0;

    scanf("%d", &n);

    int* array = (int*)malloc((sizeof(int) * n));

    for (int i = 0; i < n; i++) {

        scanf("%d", &array[i]);

        if (max < array[i]) {
            max = array[i];
        }
        all += array[i];

    }
    scanf("%d", &m);

    if (all <= m) {
        printf("%d", max);
        return 0;
    } // ������ �������� ��û������ ���ް����Ҷ�. 

    int left = 0;
    int right = max;

    // ������ �������� ��û���� ������ �Ұ���.
    while (left <= right) {

        mid = (left + right) / 2;
        int temp = 0;

        //printf("%d %d %d\n", left, right, mid);

        for (int i = 0; i < n; i++) {

            if (array[i] < mid) {
                temp += array[i];
            }

            else {
                temp += mid;
            }
        }

        //printf("%d\n", temp);

        if (temp <= m) {
            left = mid + 1;
            rst = mid;
        }
        else {
            right = mid - 1;
        }
    }

    printf("%d", rst);

    free(array);

    return 0;
}

// test case�� ����ϴµ� �����ϸ� 30%�뿡 Ʋ�ȴ���.��