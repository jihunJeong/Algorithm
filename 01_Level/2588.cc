#include <iostream>

using namespace std;
 
 int main ()
  {
   int a,b,sum = 0;

    cin >> a >> b;

    sum += a * (b % 10);
    cout << a * (b % 10) << endl;
 
     sum += ((b % 100) - (b % 10))  * a;
    cout << ((b % 100) - (b % 10)) * a / 10 << endl;
 
     sum += (b / 100) * a * 100;
    cout << (b / 100) * a << "\n" << sum << endl;
 
    return 0;
  }