#include <bits/stdc++.h>
using namespace std;

//find all barns that can be reached
void dfs(bool visited[],vector<int> paths[],int barn) {
    visited[barn-1]=true;
    for (int i=0; i<paths[barn-1].size(); i++) {
        if (not visited[paths[barn-1][i]-1]) {
            dfs(visited,paths,paths[barn-1][i]);
        }
    }
}

int main() {
    ifstream fin("closing.in");
    ofstream fout("closing.out");
    int n,m;
    fin >> n >> m;
    vector<int> paths[n];
    for (int _=0; _<m; _++) {
        int a,b;
        fin >> a >> b;
        paths[a-1].push_back(b);
        paths[b-1].push_back(a);
    }
    int closed[n];
    for (int i=0; i<n; i++) {
        fin >> closed[i];
    }
    
    bool visited[n];
    //iterate through barns in order of when they are closed
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            visited[j]=false;
        }
        //set closed barns as true
        for (int j=0; j<i; j++) {
            visited[closed[j]-1]=true;
        }
        bool connected=true;
        dfs(visited,paths,closed[n-1]);
        //check if barn can reach all other barns
        for (int j=0; j<n; j++) {
            if (not visited[j]) {
                connected=false;
                break;
            }
        }
        //remove closed barn
        paths[closed[i]-1].clear();
        for (int j=0; j<n; j++) {
            for (int k=0; k<paths[j].size(); k++) {
                if (paths[j][k]==closed[i]) {
                    paths[j].erase(paths[j].begin()+k);
                }
            }
        }
        if (connected) {
            fout << "YES\n";
        } else {
            fout << "NO\n";
        }
    }
    return 0;
}
