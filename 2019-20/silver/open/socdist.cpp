#include <bits/stdc++.h>
using namespace std;
using ll=long long;

ll n,m;

struct Interval {ll start,end;};

bool interval_sort(struct Interval a,struct Interval b) {
    return a.start<b.start;
}

//determine if all cows can be placed with a minimum distance of d apart
bool enough(struct Interval intervals[],ll d) {
	ll last=intervals[0].start-d;
	int cows=0;
	for (int i=0; i<m; i++) {
		for (ll j=max(last+d,intervals[i].start); j<intervals[i].end+1; j+=d) {
			cows++;
			if (cows<n) {
				last=j;
			} else {
				return true;
			}
		}
	}
	return false;
}

//binary search for the largest distance between the closest pair of cows
ll bs(struct Interval intervals[]) {
    ll l=0,r=1e18;
    while (l<r) {
        ll m=(l+r)/2;
        if (enough(intervals,m)) {
            l=m+1;
        } else {
			r=m;
        }
    }
    return l-1;
}

int main() {
    ifstream fin("socdist.in");
    ofstream fout("socdist.out");
    fin >> n >> m;
    struct Interval intervals[m];
	int a,b;
    for (int i=0; i<m; i++) {
		fin >> a >> b;
		intervals[i].start=a;
		intervals[i].end=b;
    }

	sort(intervals,intervals+m,interval_sort);
    fout << bs(intervals) << "\n";
    return 0;
}
