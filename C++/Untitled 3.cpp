#include <iostream>
#include "Cube.h"

using namespace uiuc;
// Function prototype for "contains":
int contains(Cube outer, Cube inner);
// ...
Cube a(10),b(5);
int a_bounds_b = contains(a,b);