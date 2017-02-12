def compound_intrest(p,t,r) :
    s=float(p*((1+r)**t)-p)
    print("Compound intrest is",s)

p=float(input("Enter principal amount:"))
r=float(input("Enter intrest rate (in %) :"))
r=r/100
t=int(input("enter time:"))
compound_intrest(p,t,r)
