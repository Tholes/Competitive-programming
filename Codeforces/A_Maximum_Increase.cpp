#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n,local = 1, global = 1;
    cin >> n;
    int numbers[n];
    for(int i= 0; i<n;i++) cin >> numbers[i];
    
    for(int i = 1; i<n;i++){
        if(numbers[i] > numbers[i-1]){
            local += 1;
        }
        else{
            local = 1;
        }
        global = max(global, local);
    }
    cout << global << endl;

    return 0;

}