#include <vector>
#include <iostream>
using namespace std;

int main() {
  vector<double> coefficient;  // polynomial coefficient
  double tmp;
  // while (cin >> tmp)
  // {
  //     coefficient.push_back(tmp);
  // }
  coefficient.push_back(2);
  coefficient.push_back(0);
  coefficient.push_back(-3);
  coefficient.push_back(3);
  coefficient.push_back(-4);

  double x_value = -2;
  // cin >> x_value;
  double poly_value = coefficient.front(),
         first_derivative = coefficient.front();
  vector<double>::size_type subscript_i = 0;
  while (subscript_i != coefficient.size() - 1) {
    poly_value = poly_value * x_value + coefficient[++subscript_i];
    if (subscript_i != coefficient.size() - 1) {
      first_derivative = first_derivative * x_value + poly_value;
    }
  }
  cout << "poly_value: " << poly_value << endl;
  cout << "first_derivative: " << first_derivative << endl;
  return 0;
}