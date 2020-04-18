#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
long long prime(long long n){
    if(n % 2 == 0){
        return n/2;
    }
    for(long long i = 3; i * i <= n; i+=2){
        if(n % i == 0){
            return ((n-i) /2 ) + 1 ;
        }
    }
    return 1;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    long long n;
    cin >> n;
    cout << prime(n) << endl;
    return 0;

}