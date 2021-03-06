#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("highcard.in");
    ofstream fout("highcard.out");
    int n;
    fin >> n;
    set<int> elsie;
    int card;
    for (int i=0; i<n; i++) {
        fin >> card;
        elsie.insert(card);
    }

    //find bessie's cards
    set<int> bessie;
    for (int i=1; i<=2*n; i++) {
        if (elsie.find(i)==elsie.end()) {
            bessie.insert(i);
        }
    }

    int result=0;
    //iterate through all of elsie's cards
    for (int elsie_card:elsie) {
        //use binary search to find the first card that bessie has that is greater than elsie's card
        auto iterator=bessie.upper_bound(elsie_card);
		if (iterator==bessie.end()) {
			break;
		} else {
            //remove card if used
            bessie.erase(iterator);
			result++;
		}
    }

    fout << result << "\n";
    return 0;
}
