#include <bits/stdc++.h>
#define endl '\n'

using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n, aux,ans=0;
    cin >> n;

    for(int i=0; i<n;i++){
        cin >> aux;
        if (aux < 0){
            ans -= aux;
        }
    }

    cout << ans <<endl;
    return 0;
}