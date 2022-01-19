#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

template <typename K>
void print_unordered_set(const std::unordered_set<K>& m) {
	// 셋의 모든 원소들을 출력하기
	for (const auto& elem : m) {
		std::cout << elem << std::endl;
	}
}

int main(int argc, char *argv[]) {
	int n, i;
	freopen("input.txt", "rt", stdin);
	scanf("%d", &n);
	std::vector<int> ch(n);
	std::unordered_set<int> s;
	for (i = 0; i < n; i++)
		{
			std::scanf("%d", &ch[i]);
		}
	
	for (int i : ch)
		{
			s.insert(i);
		}
	
	//print_unordered_set(s);
	
	ch.assign(s.begin(), s.end());
	std::sort(ch.begin(), ch.end());
	std::cout << ch[ch.size() - 3];
	
	return 0;
}