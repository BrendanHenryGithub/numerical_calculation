#%%
from math import sin
import math

def f(x):
    if x==0:
        return 1
    return sin(x)/x

def Romberg(function,lower_limit,upper_limit,deviation):
    T_n=1/2*(function(lower_limit)+function(upper_limit))
    length=(upper_limit-lower_limit)
    divide=1
    step=length/divide
    k=0
    T_list=[]
    T_list.append(T_n)
    print("k={0}  T_0={1}".format(k,T_n))
    while True:
        tmp=0
        for i in range(divide):
            tmp=tmp+function(((lower_limit+i*step)+(lower_limit+(i+1)*step))/2)
        T_2n=1/2*T_n+step/2*tmp
        print("\nk={0}  T_0={1}".format(k+1,T_2n))
        T_list.append(T_2n)
        m=1
        for j in range(len(T_list)-1,0,-1):
            temp=4**m/(4**m-1)*T_list[j]-1/(4**m-1)*T_list[j-1]
            print("m={0}  T={1}".format(m,temp))
            if j==1 :
                if abs(temp-T_list[j-1])<deviation:
                    return temp
            T_list[j-1]=temp
            m=m+1

        T_n=T_2n
        k=k+1
        divide=2**k
        step=length/divide

def main():
    Romberg(f,0,1,0.5*10**(-5))

if __name__ == '__main__':
    main()


# result:
# k=1  T_0=0.9397932848061772
# m=1  T=0.9461458822735866

# k=2  T_0=0.9445135216653896
# m=1  T=0.9460869339517938
# m=2  T=0.9460830040636743

# k=3  T_0=0.9456908635827013
# m=1  T=0.9460833108884718
# m=2  T=0.946083069350917
# m=3  T=0.9460830703872224