#include <iostream>
#include <utility>
#include <vector>
using namespace std;
void difference_quotient();
double newton_interpolating(double);

vector<pair<double, double> > value_table;

int main() {
  value_table.push_back(make_pair(0.0, 0.5));
  value_table.push_back(make_pair(0.1, 0.5398));
  value_table.push_back(make_pair(0.2, 0.5793));
  value_table.push_back(make_pair(0.3, 0.6179));
  value_table.push_back(make_pair(0.4, 0.7554));

  difference_quotient();
  for (int i = 0; i < 40; ++i) {
    cout << "f(" << 0.01 * (i + 1)
         << ") = " << newton_interpolating(0.01 * (i + 1)) << "          \t";
  }
  return 0;
}

void difference_quotient() {
  for (int i = 0; i != value_table.size() - 1; ++i) {
    for (vector<pair<double, double> >::iterator iter = value_table.end() - 1;
         iter != value_table.begin() + i; --iter) {
            iter->second = (iter->second - (iter - 1)->second) /
            (iter->first - (iter - i - 1)->first);
    }
  }
}

double newton_interpolating(double x_value) {
  double sum = value_table.begin()->second;
  double tmp = 1;
  for (vector<pair<double, double> >::iterator iter = value_table.begin();
       iter != value_table.end() - 1; ++iter) {
    tmp = tmp * (x_value - iter->first);
    sum = sum + ((iter + 1)->second) * tmp;
  }
  return sum;
}