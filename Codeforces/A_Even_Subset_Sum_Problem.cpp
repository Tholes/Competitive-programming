#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t,n,aux=0;
    cin >> t;


    while(t--){
        int ansImpar[2];
        bool par= false,impar= false;
        int ansPar;
        cin >> n;
        int numbers[n];
        aux = 0;
        for(int i = 0; i<n;i++) cin >> numbers[i];
        for(int i = 0; i< n;i++){
            if(numbers[i] % 2 == 0){
                ansPar = i+1;
                par = true;
                break;
            }
            else if(numbers[i] % 2 == 1){
                ansImpar[aux] = i+1;
                aux++;
                if(aux == 2){
                    impar = true;
                    break;
                }
            }
        }
        if(par){
            cout << 1 << endl;
            cout << ansPar << endl;
        } 
        else if(impar){
            cout << 2 << endl;
            cout << ansImpar[0] << " " << ansImpar[1] << endl;
        }
        else{
            cout << -1 << endl;
        }

    }
    return 0;

}