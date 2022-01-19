#include <iostream>
#include <string>
#include <thread>
#include <chrono>
#include <vector>
#include <mutex>

using namespace std;

int main(int argc, char *argv[]) {
	cout << std::thread::hardware_concurrency() << endl;
	cout << std::this_thread::get_id() << endl;
}