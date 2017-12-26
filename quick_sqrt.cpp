#include <iostream>
using namespace std;

float Q_rsqrt( float number )
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;
	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                       
	i  = 0x5f3759df - ( i >> 1 );               
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   
	return y;
}

int main(){
    float num=19588;
    cout << num*Q_rsqrt(num) << endl;
    return 0;
}