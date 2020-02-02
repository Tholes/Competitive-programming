#include <bits/stdc++.h>
#define endl '\n'

using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int coordenadas[6];
    int x1,y1,x2,y2,x3,y3;
    for(int i=0;i<6;i++){
        cin >> coordenadas[i];
    }
    pair<int, int > ans;
    if(coordenadas[0] == coordenadas[2]){
            ans.first = coordenadas[4];
    }
    else if(coordenadas[0] == coordenadas[4]){
        ans.first = coordenadas[2];
    }
    else if(coordenadas[2] == coordenadas[4]){
        ans.first = coordenadas[0];
    }

    if(coordenadas[1] == coordenadas[3]){
        ans.second = coordenadas[5];
    }
    else if(coordenadas[1] == coordenadas[5]){
        ans.second = coordenadas[3];
    }
    else if(coordenadas[3] == coordenadas[5]){
        ans.second = coordenadas[1];
    }
    cout << ans.first<<" "<<ans.second<< endl;
    return 0;
}