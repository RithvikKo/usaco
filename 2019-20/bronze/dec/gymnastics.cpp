#include <bits/stdc++.h>
using namespace std;

bool consistent(int a,int b) {
    for (int i=0; i<k; i++) {
        int a_index,b_index;
        for (int j=0; j<n; j++) {
            if (rankings[i][j]==a) {
                a_index=j;
            }
        }
        for (int j=0; j<n; j++) {
            if (rankings[i][j]==b) {
                b_index=j;
            }
        }
        if (a_index>b_index) {
            return false;
        }
    }
    return true;
}

int main() {
    ifstream fin("gymnastics.in");
    ofstream fout("gymnastics.out");
    int k,n;
    fin >> k >> n;
    int rankings[10][20];
    for (int i=0; i<k; i++) {
        for (int j=0; j<n; j++) {
            fin >> rankings[i][j];
        }
    }

    int result=0;
    for (int a=1; a<n+1; a++) {
        for (int b=1; b<n+1; b++) {
            if (a!=b && consistent(a,b)) {
                result++;
            }
        }
    }

    fout << result;
    return 0;
}
