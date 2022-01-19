#include <iostream>
#include <future>
#include <thread>


using namespace std;

int main(int argc, char *argv[]) {
	std::promise<int> prom;
	
	auto fut = prom.get_future();
	
	auto t = std::thread([](std::promise<int> && prom){
		prom.set_value(1+2);}, std::move(prom));
	
	cout << fut.get() << endl;
	t.join();
}
