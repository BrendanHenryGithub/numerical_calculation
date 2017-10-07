#include <iomanip>
#include <iostream>
using namespace std;

void recurrence(int, int, double, int = 4);

int main() {
  recurrence(0, 9, 0.6321);
  recurrence(9, 0, 0.0684);
  return 0;
}

void recurrence(int input_subscript, int destination_subscript,
                double input_value, int precision) {
  double value = input_value;
  int subscript = input_subscript;
  cout << "I[" << subscript << "] = " << setprecision(precision) << value
       << endl;
  if (subscript < destination_subscript) {
    while (subscript != destination_subscript) {
      value = 1 - (++subscript) * value;
      cout << "I[" << subscript << "] = " << setprecision(precision) << value
           << endl;
    }
  } else {
    while (subscript != destination_subscript) {
      value = (1 - value) / (subscript--);
      cout << "I[" << subscript << "] = " << setprecision(precision) << value
           << endl;
    }
  }
}