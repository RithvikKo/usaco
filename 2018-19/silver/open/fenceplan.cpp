#include <bits/stdc++.h>
using namespace std;

struct Cow {int x,y;};

//get all cows in moo network and border cows
void dfs(int borders[],struct Cow cows[],bool visited[],vector<int> adjacent[],int cow) {
    borders[0]=max(borders[0],cows[cow-1].x);
    borders[1]=min(borders[1],cows[cow-1].x);
    borders[2]=min(borders[2],cows[cow-1].y);
    borders[3]=max(borders[3],cows[cow-1].y);
    visited[cow-1]=true;
    for (int i=0; i<adjacent[cow-1].size(); i++) {
        if (not visited[adjacent[cow-1][i]-1]) {
            dfs(borders,cows,visited,adjacent,adjacent[cow-1][i]);
        }
    }
}

int main() {
    ifstream fin("fenceplan.in");
    ofstream fout("fenceplan.out");
    int n,m;
    fin >> n >> m;
    struct Cow cows[n];
    for (int i=0; i<n; i++) {
        int x,y;
        fin >> x >> y;
        cows[i].x=x;
        cows[i].y=y;
    }
    vector<int> adjacent[n];
    for (int _=0; _<m; _++) {
        int a,b;
        fin >> a >> b;
        adjacent[a-1].push_back(b);
        adjacent[b-1].push_back(a);
    }

    bool visited[n];
    for (int j=0; j<n; j++) {
        visited[j]=false;
    }
    vector<int> components;
    int result=4e8+1;
    //iterate through all moo networks and greedily search for the smallest perimter
    for (int cow=1; cow<n+1; cow++) {
        if (!visited[cow-1]) {
            components.push_back(cow);
            int borders[4]={-1,1e8+1,1e8+1,-1};
            dfs(borders,cows,visited,adjacent,cow);
            result=min(result,2*(borders[0]-borders[1]+borders[3]-borders[2]));
        }
    }
    
    fout << result << "\n";
    return 0;
}
