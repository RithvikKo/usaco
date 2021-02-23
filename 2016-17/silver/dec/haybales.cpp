#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("haybales.in");
    ofstream fout("haybales.out");
    int n,q;
    fin >> n >> q;
    int haybales[n];
    for (int i=0; i<n; i++) {
        fin >> haybales[i];
    }
    sort(haybales,haybales+n);
    int a,b;
    //binary search to count the number of cows from a to b
    for (int i=0; i<q; i++) {
        fin >> a >> b;
        fout << upper_bound(haybales,haybales+n,b)-lower_bound(haybales,haybales+n,a) << "\n";
    }
    return 0;
}
