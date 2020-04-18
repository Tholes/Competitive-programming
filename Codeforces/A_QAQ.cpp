#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    string str;
    getline(cin,str);
    int count[] = {0,0,0};
    for(int i = 0; i < str.length(); i++){
        if(str[i] == 'A'){
            count[1] += count[0];
        }
        else if(str[i] == 'Q'){
            count[2] += count[1];
            count[0]++;
        }
    }
    cout << count[2] << endl;
    
    return 0;

}


