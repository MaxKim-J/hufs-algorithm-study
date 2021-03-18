#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int dc[] = { 0,1,0,-1 };
int dr[] = { 1,0,-1,0 };

struct Node {
	int red_c, red_r, blue_c, blue_r, level;
	Node(int c1, int r1, int c2, int r2, int l) {
		red_c = c1, red_r = r1, blue_c = c2, blue_r = r2, level = l;
	}
};
bool is_same_node(Node* n1, Node* n2) {
	if (n1->red_c == n2->red_c
		&& n1->red_r == n2->red_r
		&& n1->blue_c == n2->blue_c
		&& n1->blue_r == n2->blue_r) {

		return true;
	}
	return false;
}

int main() {
	int n, m;
	cin >> n >> m;

	vector<string> field(n);
	for (auto& i : field) {
		cin >> i;
	}

	//공 추적, 비움
	int rc = -1, rr = -1, bc = -1, br = -1;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (field[i][j] == 'R') {
				rc = i, rr = j;
			}
			else if (field[i][j] == 'B') {
				bc = i, br = j;
			}
		}
	}
	field[rc][rr] = '.';
	field[bc][br] = '.';
	vector<string> field_empty(field);

	//BFS 준비
	queue<Node*> q;
	vector<Node*> visited;

	Node* start_node = new Node(rc, rr, bc, br, 0);
	q.push(start_node);
	visited.push_back(start_node);

	int min_success_level = 11;

	//BFS 시작
	while (!q.empty()) {
		Node* target = q.front();
		q.pop();
		bool flag_success;

		for (int d = 0; d < 4; d++) {
			if (min_success_level <= target->level + 1) {
				break;
			}

			field = field_empty;
			rc = target->red_c, rr = target->red_r, bc = target->blue_c, br = target->blue_r;
			field[rc][rr] = 'R', field[bc][br] = 'B';
			flag_success = false;

			while (field[rc + dc[d]][rr + dr[d]] == '.') {
				field[rc][rr] = '.';
				rc = rc + dc[d];
				rr = rr + dr[d];
				field[rc][rr] = 'R';
			}
			if (field[rc + dc[d]][rr + dr[d]] == 'O') {
				flag_success = true;
				
				//두 구슬이 동시에 빠지는지
				field[rc][rr] = '.';
				while (field[bc + dc[d]][br + dr[d]] == '.') {
					field[bc][br] = '.';
					bc = bc + dc[d];
					br = br + dr[d];
					field[bc][br] = 'B';
				}
				if (field[bc + dc[d]][br + dr[d]] == 'O') {
					flag_success = false;
					continue;
				}
			}
			else {
				while (field[bc + dc[d]][br + dr[d]] == '.') {
					field[bc][br] = '.';
					bc = bc + dc[d];
					br = br + dr[d];
					field[bc][br] = 'B';
				}
				if (field[bc + dc[d]][br + dr[d]] == 'O') {
					continue;
				}
				else {
					while (field[rc + dc[d]][rr + dr[d]] == '.') {
						field[rc][rr] = '.';
						rc = rc + dc[d];
						rr = rr + dr[d];
						field[rc][rr] = 'R';
					}
					if (field[rc + dc[d]][rr + dr[d]] == 'O') {
						flag_success = true;
					}
				}
			}

			//들어갔는지
			if (flag_success) {
				min_success_level = target->level + 1;
			}
			else if (target->level < min_success_level - 1) {
				Node* now = new Node(rc, rr, bc, br, target->level + 1);
				bool flag_visited = false;
				for (auto i : visited) {
					if (is_same_node(i, now)) {
						flag_visited = true;
						break;
					}
				}
				if (!flag_visited) {
					q.push(now);
				}
			}
		}
	}

	min_success_level = (min_success_level == 11) ? -1 : min_success_level;
	cout << min_success_level << "\n";


	return 0;
}