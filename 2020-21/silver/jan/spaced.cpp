#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int beauty[n][n];
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> beauty[i][j];
        }
    }

    int horizontal=0;
    for (int i=0; i<n; i++) {
        int odd=0,even=0;
        for (int j=0; j<n; j++) {
            if (j%2) {
                odd+=beauty[i][j];
            } else {
                even+=beauty[i][j];
            }
        }
        horizontal+=max(odd,even);
    }
    
    int vertical=0;
    for (int i=0; i<n; i++) {
        int odd=0,even=0;
        for (int j=0; j<n; j++) {
            if (j%2) {
                odd+=beauty[j][i];
            } else {
                even+=beauty[j][i];
            }
        }
        vertical+=max(odd,even);
    }

    cout << max(horizontal,vertical) << "\n";
    return 0;
}
