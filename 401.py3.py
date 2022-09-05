#python3 program to find simple interest
#for given principal amount,time and
#rate of interest
def simple_interest(p,t,r):
    print('the principal is',p)
    print('the time period is',p)
    print('the rate of interest is',r)
    si= (p * t * r)/100
    print('the simple interest is', si)
    return si
#driver code        
simple_interest(8, 6, 8)    
