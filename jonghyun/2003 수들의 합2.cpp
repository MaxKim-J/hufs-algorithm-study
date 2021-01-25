#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n, m;
	cin >> n >> m;

	vector<int> seq;
	int input;
	for (int i = 0; i < n; i++) {
		cin >> input;
		seq.push_back(input);
	}

	int count = 0;
	for (int i = 0; i < n; i++) {
		int sum = 0;
		for (int j = i; j < n; j++) {
			sum += seq[j];
			if (sum == m) {
				count++;
			}
		}
	}

	cout << count;

	return 0;
}