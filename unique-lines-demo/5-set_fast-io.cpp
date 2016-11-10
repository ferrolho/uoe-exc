#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
	ios::sync_with_stdio(false);

	unordered_set<string> seen;

	string line;
	while (getline(cin, line)) {
		if (seen.find(line) == seen.end()) {
			seen.insert(line);
			cout << line << endl;
		}
	}

	return 0;
}
