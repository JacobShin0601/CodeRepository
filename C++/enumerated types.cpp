#include <iostream>
#include <typeinfo>


//int computeDamage(int weapon_id)
//{
//	if(weapon_id == 0) //sword
//	{
//		return 1;
//	}
//	
//	if(weapon_id == 1) // hammer
//	{
//		return 2;
//	}
//}


enum Color // user-defined data types
{
	COLOR_BLACK = -3,
	COLOR_RED,
	COLOR_GREEN,
	COLOR_BLUE
};

enum Feeling 
{
	HAPPY,
	BLUE,
	EXCITING,
	MAD,
};





















int main(int argc, char *argv[]) {
	using namespace std;
	
	Color apple{COLOR_RED};
	Color paint(COLOR_BLACK);
	Color house(COLOR_BLUE);
	
	int color_id = COLOR_RED;
	
	Color my_color = static_cast<Color> (-1);
	
	
	int in_number;
	cin >> in_number;
	
	if(in_number == static_cast<Color> (-2))
		my_color = static_cast<Color> (-2);
	
	string str_input;
	
	std::getline(cin, str_input);
	if (str_input == "COLOR_BLACK")
		my_color = static_cast<Color> (-3);
	
	return 0;
}