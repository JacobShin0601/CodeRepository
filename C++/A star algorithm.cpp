#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	
}

// 이 소스 코드의 그래프는 인접 리스트 방식으로 그래프를 표현하였다.
using ii = pair<int, int>;

priority_queue<ii, greater<ii>, vector<ii> > pq;
/// N_VER은 그래프의 정점의 개수를 의미한다.
int dist[N_VER], cost[N_VER][N_VER]; /// dist[i]는 i번째 정점까지 가는 최단 거리를 의미한다.
vector<ii> edges[N_VER]; /// edges[i]는 i와 연결된 정점과 가중치를 묶어 저장하는 벡터이다.

int minDist(int src, int dst) {
	pq.push({0, src});
	bool success = false;
	while (!pq.empty()) {
		int v = pq.top(); pq.pop();
		if (v == dst) {
			success = true;
			break;
		}
		for (ii adj: edges[v]) {
			if (dist[adj.first] < g(v) + adj.second + h(adj.first)) {
				dist[adj.first] = g(v) + adj.second + h(adj.first); // 이완 (relaxation)
				pq.push({dist[adj], adj}); // 다음 정점 후보에 탐색하고 있는 정점을 넣는다.
			}
		}
	}
	if (!success) return -1;
	else return dist[dst];
}