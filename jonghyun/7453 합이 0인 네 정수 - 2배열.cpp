#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
enum { A, B, C, D };

int main() {
	int n;
	cin >> n;

	vector<int> row(n, 0);
	vector<vector<int>> arrays(4, row);
	for (int i = 0; i < n; i++) {
		cin >> arrays[A][i] >> arrays[B][i] >> arrays[C][i] >> arrays[D][i];
	}

	if (n == 1) {
		if (arrays[A][0] + arrays[B][0] + arrays[C][0] + arrays[D][0] == 0) {
			std::cout << 1 << "\n";
		}
		else {
			std::cout << 0 << "\n";
		}

		return 0;
	}

	vector<int> AB, CD;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			AB.push_back(arrays[A][i] + arrays[B][j]);
			CD.push_back(arrays[C][i] + arrays[D][j]);
		}
	}

	sort(AB.begin(), AB.end());
	sort(CD.begin(), CD.end());

	//for (auto& i : AB) {
	//	std::cout << i << "\t";
	//}
	//std::cout << "\n";
	//for (auto& i : CD) {
	//	std::cout << i << "\t";
	//}

	//소문자는 해당 배열의 인덱스
	int ab = 0;
	int cd = CD.size() - 1;

	long long count = 0;
	while (true) {
		int sum = AB[ab] + CD[cd];

		//합을 판단하는 부분 - 판단 후 c,d를 조절한다
		if (sum == 0) {
			int ab_target = AB[ab], cd_target = CD[cd];		//인덱스를 증가시키면서 타겟 숫자와 같은지 세어보는것
			long long ab_count = 0, cd_count = 0;		//몇개가 같은지 - 기본 1개
			while (ab < AB.size() && AB[ab] == ab_target) {
				ab_count++;
				ab++;
			}
			while (0 <= cd && CD[cd] == cd_target) {
				cd_count++;
				cd--;
			}

			count += ab_count * cd_count;		//ab, cd 각 배열에 같은 수가 잇으면 만들 수 있는 가지수는 n*m
		}
		else if (sum < 0) {
			ab++;
		}
		else {
			cd--;
		}

		bool ab_end = false, cd_end = false;

		//c,d가 조절된 후 범위를 지키는지 검사한다
		if (AB.size() <= ab && cd < 0) {
			ab_end = cd_end = true;
		}
		else if (AB.size() <= ab) {
			ab_end = true;
			ab--;
			while (true) {
				if (AB[ab] - CD[cd] == 0) {
					count++;
					break;
				}
				cd--;
				if (cd < 0) {
					cd_end = true;
					break;
				}
			}
		}
		else if (cd < 0) {
			cd_end = true;
			cd++;
			while (true) {
				if (AB[ab] - CD[cd] == 0) {
					count++;
					break;
				}
				ab++;
				if (AB.size() <= ab) {
					ab_end = true;
					break;
				}
			}
		}

		if (ab_end || cd_end) {
			break;
		}
	}

	std::cout << count << "\n";

	return 0;
}

/*
2
1 1 -1 -1
1 1 -1 -1

*/