#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int ga1,gb1,ga2,gb2,ea1,eb1,ea2,eb2, gunnar, emma;
    cin >> ga1 >> gb1 >> ga2 >> gb2 >> ea1 >> eb1 >> ea2 >> eb2;
    gunnar = (ga1+gb1) + (ga2+gb2); 
    emma = (ea1+eb1) + (ea2+eb2);
    if(gunnar > emma){
        cout << "Gunnar" << endl;
    }
    else if(gunnar < emma){
        cout << "Emma" << endl;
    }
    else{
        cout << "Tie" << endl;
    }
    return 0;
}