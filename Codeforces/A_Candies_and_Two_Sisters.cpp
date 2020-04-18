#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t,n;
    cin >> t;
    while(t--){
        cin >> n;
        cout << (n - 1) - n/2  << endl;
    }
    return 0;

}