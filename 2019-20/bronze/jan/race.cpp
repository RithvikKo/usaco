#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream fin("race.in");
    ofstream fout("race.out");
    int k,n;
    fin >> k >> n;
	int x;
	//iterate through all finishing speeds
    for (int i=0; i<n; i++) {
        fin >> x;
	    int d=0,t=0,s=1;
	    //iterate through each speed
	    while (true) {
	        d+=s;
	        t++;
	        //break if finished race
	        if (d>=k) {
	            break;
			}
	        //have to slow down if speed is greater or equal to finishing speed
	        if (s>=x) {
				d+=s;
				t++;
				if (d>=k) {
					break;
				}
			}
	        s++;
		}
		fout << t << "\n";
	}
    return 0;
}
