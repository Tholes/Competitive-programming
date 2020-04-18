#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n,ans;
    int foods[3];
    cin >> n;
    while(n--){
        ans = 0;
        for(int i = 0; i < 3; i++) cin >> foods[i];
        int n = sizeof(foods)/sizeof(foods[0]); 
        sort(foods, foods+3, greater<int>());
        for(int i = 0; i<3; i++){
            if (foods[i] > 0){
                ans++;
                foods[i]--;
            }

            for(int j = i+1; j<3; j++){
                if(foods[j] > 0 && foods[i] > 0){
                    foods[j]--;
                    foods[i]--;
                    ans++;
                }
            }
        }
        bool aux = true;
        for(int i = 0; i<3;i++){
            if(foods[i] == 0){
                aux = false;
                break;
            }
        }
        if(aux) ans++;
        cout << ans << endl;

    }
    return 0;

}