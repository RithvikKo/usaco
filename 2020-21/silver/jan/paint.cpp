#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,q;
    cin >> n >> q;
    string color;
    cin >> color;

    int last,prefix_sums[n];
    char lightest;
    prefix_sums[0]=1;
    for (int i=1; i<n; i++) {
        last=-1;
        for (int j=i-1; j>-1; j--) {
            if (color[j]==color[i]) {
                last=j;
                break;
            }
        }
        if (last!=-1) {
            lightest=color[i];
            for (int j=last+1; j<i; j++) {
                if (color[j]<lightest) {
                    lightest=color[j];
                }
            }
            if (lightest<color[i]) {
                last=-1;
            }
        }
        if (last==-1) {
            prefix_sums[i]=prefix_sums[i-1]+1;
        } else {
            prefix_sums[i]=prefix_sums[i-1];
        }
    }

    int suffix_sums[n];
    suffix_sums[n-1]=1;
    for (int i=n-2; i>-1; i--) {
        last=-1;
        for (int j=i+1; j<n; j++) {
            if (color[j]==color[i]) {
                last=j;
                break;
            }
        }
        if (last!=-1) {
            lightest=color[i];
            for (int j=i+1; j<last; j++) {
                if (color[j]<lightest) {
                    lightest=color[j];
                }
            }
            if (lightest<color[i]) {
                last=-1;
            }
        }
        if (last==-1) {
            suffix_sums[i]=suffix_sums[i+1]+1;
        } else {
            suffix_sums[i]=suffix_sums[i+1];
        }
    }

    int a,b,prefix,suffix;
    for (int i=0; i<q; i++) {
        cin >> a >> b;
        if (a!=1) {
            prefix=prefix_sums[a-2];
        } else {
            prefix=0;
        }
        if (b!=n) {
            suffix=suffix_sums[b];
        } else {
            suffix=0;
        }
        cout << prefix+suffix << "\n";
    }
    return 0;
}
