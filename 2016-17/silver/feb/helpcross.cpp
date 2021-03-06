#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("helpcross.in");
    ofstream fout("helpcross.out");
    int n,c;
    fin >> c >> n;
    int chickens[c];
    for (int i=0; i<c; i++) {
        fin >> chickens[i];
    }
    vector<pair<int,int> > cows;
    int a,b;
    for (int i=0; i<n; i++) {
        fin >> a >> b;
        cows.push_back(make_pair(b,a));
    }

    //sort chickens and cows
    sort(chickens,chickens+c);
    sort(cows.begin(),cows.end());
    int result=0;
    //iterate through all chickens
    for (int chicken:chickens) {
        //go through all cows and pair chicken with the first cow that can be paired
        for (int i=0; i<cows.size(); i++) {
            if (cows[i].second<=chicken && chicken<=cows[i].first) {
                //remove cow
                cows.erase(cows.begin()+i);
                result++;
                break;
            }
        }
    }

    fout << result << "\n";
    return 0;
}
