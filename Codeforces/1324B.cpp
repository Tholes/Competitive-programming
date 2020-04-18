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
        int numbers[n];
        for(int i = 0; i < n; i++){
            cin >> numbers[i];
        }
        bool ans = false;
        for(int i = 0; i < n; i++){
            for(int j = i+2; j < n;j++ ){
                if( numbers[i] == numbers[j]){
                    ans = true;
                    break;
                }
            }
        }
        if(ans){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }
    return 0;

}