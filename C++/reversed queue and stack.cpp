#include <iostream>
#include <stack>
#include <queue>

std::stack<int> reverse_stack(std::stack<int> s) {
  std::stack<int> reversed_s;
  
  // write code here that returns a stack whose elements are
  // in reverse order from those in stack s
  int s_n = s.size();
  std::queue<int> temp_queue;
  for (int i = 0; i < s_n; i++){
    temp_queue.push(s.top());
    s.pop();
  }
  
  int temp_n = temp_queue.size();
  for (int j = 0; j < temp_n; j++){
    reversed_s.push(temp_queue.front());
    temp_queue.pop();
  }
  
  return reversed_s;
}

std::queue<int> reverse_queue(std::queue<int> q) {
  std::queue<int> reversed_q;
  
  // write code here that returns a queue whose elements are
  // in reverse order from those in queue q
  
  int q_n = q.size();
  std::stack<int> temp_stack;
  for (int i = 0; i < q_n; i++){
    temp_stack.push(q.front());
    q.pop();
  }
  
  int temp_n = temp_stack.size();
  for (int j = 0; j < temp_n; j++) {
    reversed_q.push(temp_stack.top());
    temp_stack.pop();
  }
  
  return reversed_q;
}

void print_stack(std::string name, std::stack<int> s) {
  std::cout << "stack " << name << ": ";
  while (!s.empty()) {
    std::cout << s.top() << " ";
    s.pop();
  }
  std::cout << std::endl;
}

void print_queue(std::string name, std::queue<int> q) {
  std::cout << "queue " << name << ": ";
  while (!q.empty()) {
    std::cout << q.front() << " ";
    q.pop();
  }
  std::cout << std::endl;
}

int main() {
  std::stack<int> s, rs;
  std::queue<int> q, rq;
  
  s.push(1); s.push(2); s.push(3); s.push(4); s.push(5);

  print_stack("s",s);

  rs = reverse_stack(s);

  print_stack("reversed s",rs);
  
  q.push(1); q.push(2); q.push(3); q.push(4); q.push(5);
  
  print_queue("q",q);
  
  rq = reverse_queue(q);
  
  print_queue("reversed q",rq);

  return 0;
}