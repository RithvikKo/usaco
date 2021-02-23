#include <bits/stdc++.h>
using namespace std;

struct Cow {int x,y,r;};

//calculate distance between two cows
float distance(struct Cow cow1, struct Cow cow2) {
    return sqrt(pow(cow1.x-cow2.x,2)+pow(cow1.y-cow2.y,2));
}

//find all cows that can be reached
void dfs(bool visited[],vector<int> relay[],int cow) {
    visited[cow]=true;
    for (int i=0; i<relay[cow].size(); i++) {
        if (not visited[relay[cow][i]]) {
            dfs(visited,relay,relay[cow][i]);
        }
    }
}

int main() {
    ifstream fin("moocast.in");
    ofstream fout("moocast.out");
    int n;
    fin >> n;
    struct Cow cows[n];
    for (int i=0; i<n; i++) {
        int x,y,r;
        fin >> x >> y >> r;
        cows[i].x=x;
        cows[i].y=y;
        cows[i].r=r;
    }

    vector<int> relay[n];
    //find all cows that each cow can directly relay to
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            if (i!=j && distance(cows[i],cows[j])<=cows[i].r) {
                relay[i].push_back(j);
            }
        }
    }

    int result=0;
    //iterate through all cows
    for (int i=0; i<n; i++) {
        bool visited[n];
        for (int j=0; j<n; j++) {
            visited[j]=false;
        }
        int reach=0;
        dfs(visited,relay,i);
        //find the number of cows that can be reached
        for (int j=0; j<n; j++) {
            if (visited[j]) {
                reach++;
            }
        }
        result=max(result,reach);
    }
    
    fout << result << "\n";
    return 0;
}
