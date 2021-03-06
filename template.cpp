#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("_.in");
    ofstream fout("_.out");
    int n;
    cin >> n;
    int _[n];
    for (int i=0; i<n; i++) {
        cin >> _[i];
    }
    pair<int,int> _[n];
    //tuple<int,int,int> _[n];
    for (int i=0; i<n; i++) {
        cin >> _[i];
    }
    int _[n][m];
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> _[i][j];
        }
    }
    int result=0;
    cout << result << "\n";
    return 0;
}

//for dfs/flood fill
bool visited[n];
for (int i=0; i<n; i++) {
    visited[i]=false;
}

//depth first search
void dfs(bool visited[],vector<int> adjacent[],int _) {
    visited[_]=true;
    for (int _: adjacent[_]) {
        if (not visited[_]) {
            dfs(visited,adjacent,_);
        }
    }
}

//flood fill
void ff(bool visited[],int i,int j) {
    visited[i*n+j]=true;
    if (i!=0 && not visited[(i-1)*n+j]) {
        ff(visited,i-1,j);
    }
    if (i!=n-1 && not visited[(i+1)*n+j]) {
        ff(visited,i+1,j);
    }
    if (j!=0 && not visited[i*n+j-1]) {
        ff(visited,i,j-1);
    }
    if (j!=n-1 && not visited[i*n+j+1]) {
        ff(visited,i,j+1);
    }
}

//binary search on the answer
int bs() {
    int l=0,r=_,m;
    while (l<r) {
        m=(l+r)/2;
        if (_(m)) {
            l=m+1;
        } else {
            r=m;
        }
    }
    return l;
}
