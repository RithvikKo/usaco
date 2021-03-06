#include <bits/stdc++.h>
using namespace std;
using ll=long long;

int n;

//dfs through locations and mark visited
void dfs(bool visited[],vector<pair<int,ll> > adjacent[],int cow,ll min_w) {
    visited[cow-1]=true;
    for (pair<int,ll> adjacent_cow:adjacent[cow-1]) {
        if (not visited[adjacent_cow.first-1] && adjacent_cow.second>=min_w) {
            dfs(visited,adjacent,adjacent_cow.first,min_w);
        }
    }
}

//check if all locations can be visited, ignoring locations that are sorted
bool check(set<int> unsorted,bool visited[]) {
    for (int i=0; i<n; i++) {
        if (not visited[i] && unsorted.find(i+1)!=unsorted.end()) {
            return false;
        }
    }
    return true;
}

//binary search for the maximum wormhole width that can be sorted
ll bs(ll min_w,ll max_w,set<int> unsorted,vector<pair<int,ll> > adjacent[]) {
    ll l=min_w,r=max_w,m;
    bool visited[n];
    while (l<r) {
        m=(l+r)/2;
        for (int i=0; i<n; i++) {
            visited[i]=false;
        }
        dfs(visited,adjacent,1,m);
        if (check(unsorted,visited)) {
            l=m+1;
        } else {
            r=m;
        }
    }
    return l-1;
}

int main() {
    ifstream fin("wormsort.in");
    ofstream fout("wormsort.out");
    int m;
    fin >> n >> m;
    int cows[n];
    for (int i=0; i<n; i++) {
        fin >> cows[i];
    }
    vector<pair<int,ll> > adjacent[n];
    int a,b;
    ll w,min_w=10e9,max_w=1;
    for (int i=0; i<m; i++) {
        fin >> a >> b >> w;
        adjacent[a-1].push_back(make_pair(b,w));
        adjacent[b-1].push_back(make_pair(a,w));
        min_w=min(min_w,w);
        max_w=max(max_w,w);
    }

    //create array of sorted cows
    int sorted[n];
    copy(cows,cows+n,sorted);
    sort(sorted,sorted+n);
    //create set of all unsorted cows
    set<int> unsorted;
    for (int i=0; i<n; i++) {
        if (sorted[i]!=cows[i]) {
            unsorted.insert(cows[i]);
        }
    }

    //check if cows are already sorted
    if (unsorted.size()) {
        fout << bs(min_w,max_w,unsorted,adjacent) << "\n";
    } else {
        fout << "-1\n";
    }
    return 0;
}
