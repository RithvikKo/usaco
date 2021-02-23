#include <bits/stdc++.h>
using namespace std;

int n,m,c;

//determine if all cows can go to the convention with maximum waiting time
bool enough(int cows[],int max_wait) {
    int count=0,bus_arrival=cows[0],buses=m;
    for (int i=0; i<n-1; i++) {
		count++;
		if (count==c || cows[i+1]-bus_arrival>max_wait) {
			buses--;
            if (buses) {
                count=0,bus_arrival=cows[i+1];
            } else {
                return false;
            }
		}
    }
    return true;
}

//binary search for the smallest waiting time
int bs(int cows[]) {
    int l=0,r=1e9;
    while (l<r) {
        int m=(l+r)/2;
        if (enough(cows,m)) {
            r=m;
        } else {
            l=m+1;
        }
    }
    return l;
}


int main() {
    ifstream fin("convention.in");
    ofstream fout("convention.out");
    fin >> n >> m >> c;
    int cows[n];
    for (int i=0; i<n; i++) {
        fin >> cows[i];
    }

    sort(cows,cows+n);
    fout << bs(cows) << "\n";
    return 0;
}
