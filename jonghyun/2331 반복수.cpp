#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

inline int myPow(int n, int i) {
	const static int table[5][10] = {
		{0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
		,{0, 1, 4, 9, 16, 25, 36, 49, 64, 81 }
		,{0, 1, 8, 27, 64, 125, 216, 343, 512, 729 }
		,{0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561 }
		,{0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049 }
	};

	return table[i - 1][n];
}
int myFunc(int num, int p) {
	int sum = 0;
	while (num) {
		int i = num % 10;		//마지막 자리의 수 뽑기
		sum += myPow(i, p);		//제곱한 숫자를 누적
		num = static_cast<int>(num / 10);		//마지막 자리의 수 없애기
	}

	return sum;
}

int main() {
	int a, p;
	cin >> a >> p;

	vector<int>seq(1, 0);
	unordered_map<int, int> visited;

	seq.push_back(a);
	visited[a] = seq.size() - 1;

	int result_value;
	while (true) {
		int target = myFunc(*seq.rbegin(), p);
		if (visited.find(target) != visited.end()) {
			result_value = visited[target] - 1;
			break;
		}

		seq.push_back(target);
		visited[target] = seq.size() - 1;
	}

	cout << result_value << "\n";

	for (auto& i : seq) {
		cout << i << " ";
	}
	return 0;
}