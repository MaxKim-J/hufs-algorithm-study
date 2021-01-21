#include <iostream>
#include <vector>

using namespace std;

void subseq(vector<int>& sub, vector<vector<int>>& subset, int level_max, int level_now) {
	subset.push_back(sub);

	for (int i = level_now; i < level_max; i++) {
		sub.push_back(i);
		subseq(sub, subset, level_max, i + 1);
		sub.pop_back();
	}
}

int main() {
	int n, s;
	cin >> n >> s;

	vector<int> seq;
	int input;
	for (int i = 0; i < n; i++) {
		cin >> input;
		seq.push_back(input);
	}

	vector <int> sub;
	vector<vector<int>> subset;
	subseq(sub, subset, n, 0);

	for (auto it = subset.begin(); it != subset.end(); it++) {		//크기가 양수가 아닌 단 하나의 원소를 지운다
		if (it->size() == 0) {
			subset.erase(it);
			break;
		}
	}

	int count = 0;
	for (auto& i : subset) {
		int sum = 0;
		for (auto& j : i) {
			sum += seq[j];
		}
		if (sum == s) {
			count++;
		}
	}

	cout << count << "\n";

	return 0;
}