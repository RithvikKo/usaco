#include <bits/stdc++.h>
using namespace std;

//custom comparator to sort by left point of each mountain's base
bool comparator(pair<int,int> a,pair<int,int> b) {
    //if two mountains have the same left point, the mountain with further right base should be in front
    if (a.first<b.first || a.first==b.first && a.second>b.second) {
        return true;
    }
    return false;
}

int main() {
    ifstream fin("mountains.in");
    ofstream fout("mountains.out");
    int n;
    fin >> n;
    int x,y;
    pair<int,int> mountains[n];
    for (int i=0; i<n; i++) {
        fin >> x >> y;
        mountains[i]=make_pair(x-y,x+y);
    }
    //sort mountains
    sort(mountains,mountains+n,comparator);
    pair<int,int> longest=mountains[0];
    int result=1;
    //iterate through all mountains and keep track of the mountain with the furthest right base
    for (int i=1; i<n; i++) {
        if (mountains[i].first>=longest.first && mountains[i].second<=longest.second) {
            continue;
        }
        if (mountains[i].second>longest.second) {
            longest=mountains[i];
        }
        result++;
    }
    fout << result << "\n";
    return 0;
}
