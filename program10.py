def simple_intrest(p,t,r) :
    s=float((p*r*t)/100)
    print("simple intrest is",s)
p=int(input("enter principal amount:"))
r=float(input("enter intrest rate (in%):"))
t=int(input("enter time:"))
simple_intrest(p,t,r)
