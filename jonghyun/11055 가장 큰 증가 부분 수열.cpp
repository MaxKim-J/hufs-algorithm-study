#include <iostream>
#include <vector>

using namespace std;

int dp_lis(vector<int>& seq, vector<int>& save, int pos) {
	if (save[pos] != 0) {
	}
	else if (pos == 0) {
		save[pos] = seq[pos];
	}
	else {
		int max_idx = pos;
		for (int i = pos - 1; 0 <= i; i--) {
			int tmp_idx = dp_lis(seq, save, i);
			if (save[max_idx] < save[tmp_idx] && seq[i] < seq[pos]) {
				max_idx = tmp_idx;
			}
		}
		save[pos] = save[max_idx] + seq[pos];
	}

	//for (auto& i : save) {
	//	cout <<i << " / ";
	//}
	//cout << "\n";

	return pos;
}

int main() {
	int n;
	cin >> n;
	
	vector<int> seq(n, 0);
	vector<int>save(n, 0);
	for (int i = 0; i < n; i++) {
		cin >> seq[i];
	}

	dp_lis(seq, save, n - 1);

	int max = 1 << 31;
	for (auto& i : save) {
		if (max < i) {
			max = i;
		}
	}

	cout << max << "\n";

	return 0;
}
