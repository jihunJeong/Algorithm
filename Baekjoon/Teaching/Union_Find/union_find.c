#include <iostream>
#include <stdio.h>

using namespace std;

int parent[1000001];

int Find(int x){

	if(x == parent[x]){
		return x;
	}
	else{
		int y = Find(parent[x]);
		parent[x] = y;
		return y;
	}

}

void Union(int x, int y){

	x = Find(x);
	y = Find(y);

	parent[y] = x;

}

int main(){

	int n,m;

	scanf("%d %d", &n, &m);

	// 배열 생성 및 초기화
	// 처음에는 자기 자신이 부모이다 -> 모두 떨어져있기 때문
	for(int i=0; i<=n; i++){
		parent[i] = i;
	}

	int op, a, b;
	while(m--){
		scanf("%d %d %d", &op, &a, &b);

		if(op == 0){
			Union(a,b);
		}

		else if(op == 1){
			int a_parent = Find(a);
			int b_parent = Find(b);

			if(a_parent == b_parent){
				printf("YES\n");
			}
			else{
				printf("NO\n");
			}
		}
	}
	return 0;
}
