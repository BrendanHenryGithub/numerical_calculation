#include <iostream>
#include <utility>
#include <vector>
using namespace std;
double lagrange_interpolating(double);

vector<pair<double, double> > value_table;

int main() {
  value_table.push_back(make_pair(0.0, 0.5));
  value_table.push_back(make_pair(0.1, 0.5398));
  value_table.push_back(make_pair(0.2, 0.5793));
  value_table.push_back(make_pair(0.3, 0.6179));
  value_table.push_back(make_pair(0.4, 0.7554));

  cout << "f(0.13) = " << lagrange_interpolating(0.13) << endl;
  cout << "f(0.22) = " << lagrange_interpolating(0.22) << endl;
  cout << "f(0.36) = " << lagrange_interpolating(0.36) << endl;
  return 0;
}

double lagrange_interpolating(double x_value) {
  double sum = 0;
  for (int i = 0; i != value_table.size(); ++i) {
    double tmp1 = 1;
    double tmp2 = 1;
    for (vector<pair<double, double> >::iterator iter = value_table.begin();
         iter != value_table.end(); ++iter) {
      if (iter->first != value_table[i].first) {
        tmp1 = tmp1 * (x_value - iter->first);
        tmp2 = tmp2 * (value_table[i].first - iter->first);
      }
    }
    sum = sum + value_table[i].second * (tmp1 / tmp2);
  }
  return sum;
}