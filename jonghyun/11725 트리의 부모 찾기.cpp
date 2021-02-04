#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

struct Node {
	int parent;
	vector<int> link;
};

int main() {
	int n;
	cin >> n;

	vector<Node> graph(n);
	int node1, node2;
	for (int i = 0; i < n-1; i++) {
		cin >> node1 >> node2;
		node1--;		//1번 노드는 인덱스가 0이 되기 때문에
		node2--;

		graph[node1].link.push_back(node2);
		graph[node2].link.push_back(node1);
	}

	queue<int> q;

	//최초의 값 큐에 넣기 - 여기서는 인덱스 0번 노드가 처음이다
	int idx_now = 0;
	q.push(idx_now);

	int debug_count = 0;
	//BFS 실행
	while (q.size()) {
		idx_now = q.front();

		//cout << "[" << debug_count++ << "] idx: " << idx_now << ", parent: " << graph[idx_now].parent+1 << "\n";

		q.pop();

		for (auto& i : graph[idx_now].link) {
			if (i == graph[idx_now].parent) {
				continue;
			}

			q.push(i);
			graph[i].parent = idx_now;
		}		
	}

	bool flag_skipped_first = false;
	for (auto& i : graph) {
		if (flag_skipped_first) {
			cout << i.parent + 1 << "\n";
		}
		else {
			flag_skipped_first = true;
		}
	}

	return 0;
}