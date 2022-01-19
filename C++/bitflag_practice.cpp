#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	unsigned char option_viewed = 0x01;
	unsigned char option_edited = 0x02;
	unsigned char option_liked = 0x04;
	unsigned char option_shared = 0x08;
	unsigned char option_deleted = 0x80;
	
	unsigned char my_article_flags = 0;
	
	cout << std::bitset<8>(my_article_flags) << endl;
	
	
	//when read articles
	my_article_flags |= option_viewed;
	cout << std::bitset<8>(my_article_flags) << endl;
	
	//when liked 'like'
	my_article_flags |= option_liked;
	cout << std::bitset<8>(my_article_flags) << endl;
	
	//when clicked like again
	my_article_flags &= ~option_liked;
	cout << std::bitset<8>(my_article_flags) << endl;
	
	//when delete article
	my_article_flags |= option_deleted;
	cout << std::bitset<8>(my_article_flags) << endl;
}