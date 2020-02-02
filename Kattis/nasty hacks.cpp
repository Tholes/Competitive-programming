#include <bits/stdc++.h>
#define endl '\n'

using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n,withOut,advertasing,price;

    cin >> n;
    for(int i= 0;i<n; i++){
        cin >> withOut >> advertasing >> price;
        if (withOut > (advertasing-price)){
            cout << "do not advertise" << endl;
        }
        else if (withOut == (advertasing-price)){
            cout << "does not matter" << endl;
        }
        else{
            cout << "advertise" << endl;
        }
    }
    return 0;
}