#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t,n, antX, antY,x,y;
    bool ans;
    cin >> t;
    while(t--){
        cin >> n;
        cin >> antX >> antY;
        ans = true;
        if(antY > antX){
            ans = false;
        }
        for(int i = 0; i < n - 1; i++ ){
                cin >> x >> y;
                if(y > x){
                    ans = false;
                }
                else if(x < antX || y < antY){
                    ans = false;
                }
                else if(abs(y-antY) > abs(antX-x)){
                    ans = false;
                }
                antX = x;
                antY = y;
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
