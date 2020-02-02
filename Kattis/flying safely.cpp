#include <bits/stdc++.h>

#define endl '\n'
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n, travels, pilots,u,v;
    cin >> n; 
    while( n--){
        cin >> travels >> pilots;
        cout << travels - 1 << endl;
        while(pilots--){
            cin >> u >> v;
        }
    }

    return 0;
}