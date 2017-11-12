#%%
from math import sin

def f(x):
    if x==0:
        return 1
    return sin(x)/x

def composite_trapezoidal_formula(function,lower_limit,upper_limit,divide):
    tmp=0
    step=(upper_limit-lower_limit)/divide
    for i in range(divide):
        tmp=tmp+function(lower_limit+i*step)+function(lower_limit+(i+1)*step)
    return step/2*tmp

def compound_Simpson_formula(function,lower_limit,upper_limit,divide):
    tmp=0
    step=(upper_limit-lower_limit)/divide
    for i in range(divide):
        tmp=tmp+function(lower_limit+i*step)+function(lower_limit+(i+1)*step)+4*function(((lower_limit+i*step)+(lower_limit+(i+1)*step))/2)
    return step/6*tmp

def half_trapezoidal(function,lower_limit,upper_limit,deviation):
    T_n=1/2*(function(lower_limit)+function(upper_limit))
    length=(upper_limit-lower_limit)
    divide=1
    step=length/divide
    k=0
    while True:
        tmp=0
        for i in range(divide):
            tmp=tmp+function(((lower_limit+i*step)+(lower_limit+(i+1)*step))/2)
        T_2n=1/2*T_n+step/2*tmp
        print("等分次数：{0}  Tn:{1}".format(k+1,T_2n))
        if abs(T_2n-T_n)<deviation :
            return T_2n
        T_n=T_2n
        k=k+1
        divide=2**k
        step=length/divide

def main():
    print("复合梯形求积：{}".format(composite_trapezoidal_formula(f,0,1,8)))
    print("复合辛普森求积：{}".format(compound_Simpson_formula(f,0,1,4)))
    half_trapezoidal(f,0,1,0.5*10**(-6))

if __name__ == '__main__':
    main()
        

# result:
# 复合梯形求积：0.9456908635827014
# 复合辛普森求积：0.9460833108884719
# 等分次数：1  Tn:0.9397932848061772
# 等分次数：2  Tn:0.9445135216653896
# 等分次数：3  Tn:0.9456908635827013
# 等分次数：4  Tn:0.9459850299343859
# 等分次数：5  Tn:0.946058560962768
# 等分次数：6  Tn:0.9460769430600631
# 等分次数：7  Tn:0.9460815385431521
# 等分次数：8  Tn:0.9460826874113472
# 等分次数：9  Tn:0.946082974628235