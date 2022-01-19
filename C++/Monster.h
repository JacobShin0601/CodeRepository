#pragma once
#include "Position2D.h"
#include <string>

class Monster {
private:
	std::string m_name;
	Position2D m_location;
	
public:
	Monster(const std::string name_in, const Position2D& pos_in)
	:m_name(name_in), m_location(pos_in)
	{}
	
	void moveTo(const Position2D& pos_target){
		m_location.set(pos_target);
	}
	
	friend std::ostream& operator << (std::ostream& out, Monster& mon){
		out << mon.m_name << " " << mon.m_location << std::endl;
		
		return out;
	}
	
	
};

