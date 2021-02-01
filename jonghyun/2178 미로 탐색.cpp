#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <array>

using namespace std;

enum { U, R, D, L };
int dc[] = { -1,0,1,0 };
int dr[] = { 0,1,0,-1 };

int main() {
	int n, m;
	cin >> n >> m;

	vector<int> row(m, 0);
	vector<vector<int>> field(n, row);
	vector<vector<int>> visited(field);

	string input_str;
	for (auto& i : field) {
		cin >> input_str;
		for (int j = 0; j < m; j++) {
			i[j] = static_cast<int>(input_str[j] - '0');
		}
	}

	int c = 0, r = 0, level = 1;
	queue<array<int, 3>> q;

	q.push({ c,r,level });
	visited[c][r] = level;

	int flag_goal_result = 0;
	while (q.size()) {
		array<int, 3> target = q.front();
		q.pop();
		//cout << "target: " << target[0] << " " << target[1] << ": " << target[2] << "\n";
		c = target[0];
		r = target[1];
		level = target[2];

		int new_c, new_r;
		for (int dir = U; dir <= L; dir++) {
			new_c = c + dc[dir];
			new_r = r + dr[dir];

			if (!(0 <= new_c && new_c < n) || !(0 <= new_r && new_r < m)) {
				continue;
			}

			if (!field[new_c][new_r]) {
				continue;
			}

			if (visited[new_c][new_r] != 0) {
				continue;
			}

			q.push({ new_c,new_r,level+1 });
			visited[new_c][new_r] = level+1;

			if (new_c == n-1 && new_r == m-1) {
				flag_goal_result = level+1;
				break;
			}
		}
		if (flag_goal_result) {
			break;
		}
	}

	cout << flag_goal_result;

	return 0;
}