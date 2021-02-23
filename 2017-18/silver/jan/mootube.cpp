#include <bits/stdc++.h>
using namespace std;

//find how many videos can be recommended
void dfs(bool visited[],vector<int> adjacent[],vector<int> relevance[],int video,int k) {
    visited[video-1]=true;
    for (int i=0; i<adjacent[video-1].size(); i++) {
        if (not visited[adjacent[video-1][i]-1] and relevance[video-1][i]>=k) {
            dfs(visited,adjacent,relevance,adjacent[video-1][i],k);
        }
    }
}

int main() {
    ifstream fin("mootube.in");
    ofstream fout("mootube.out");
    int n,q;
    fin >> n >> q;
    vector<int> adjacent[n];
    vector<int> relevance[n];
    for (int i=0; i<n-1; i++) {
        int a,b,r;
        fin >> a >> b >> r;
        adjacent[a-1].push_back(b);
        adjacent[b-1].push_back(a);
        relevance[a-1].push_back(r);
        relevance[b-1].push_back(r);
    }
    
    //iterate through every question
    for (int i=0; i<q; i++) {
        int k,video;
        fin >> k >> video;
        bool visited[n];
        for (int j=0; j<n; j++) {
            visited[j]=false;
        }
        dfs(visited,adjacent,relevance,video,k);
        int result=-1;
        for (int j=0; j<n; j++) {
            if (visited[j]) {
                result++;
            }
        }
        fout << result << "\n";
    }
    return 0;
}
