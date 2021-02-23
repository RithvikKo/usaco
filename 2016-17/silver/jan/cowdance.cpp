#include <bits/stdc++.h>
using namespace std;

int n,t;

//determine if the show can finish in time
bool finish(vector<int> cows,int k) {
    int result=0,last,shortest;
    vector<int> new_cows;
    //loop until all cows are done
    while (cows.size()) {
        last=min((int)cows.size(),k);
        shortest=1e5+1;
        //find shortest duration and subtract from all other cows on stage
        for (int i=0; i<last; i++) {
            shortest=min(shortest,cows[i]);
        }
        for (int i=0; i<last; i++) {
            cows[i]=max(0,cows[i]-shortest);
        }
        //remove all cows that are finished
        cows.erase(remove(cows.begin(),cows.begin()+last,0),cows.begin()+last);
        result+=shortest;
    }
    return result<=t;
}


//binary search for k
int bs(vector<int> cows) {
    int l=0,r=n;
    while (l<r) {
        int m=(l+r)/2;
        if (finish(cows,m)) {
            r=m;
        } else {
            l=m+1;
        }
    }
    return l;
}

int main() {
    ifstream fin("cowdance.in");
    ofstream fout("cowdance.out");
    fin >> n >> t;
    int d;
    vector<int> cows;
    for (int _=0; _<n; _++) {
        fin >> d;
        cows.push_back(d);
    }
    
    fout << bs(cows) << "\n";
    return 0;
}
