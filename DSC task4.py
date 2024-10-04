#THE BOTTLE SHIPPING PROBLEM
def bottle_shipping():
    bottle=int(input("enter the number of bottels"))
    xl=int(bottle/48)
    l=int((bottle%48)/24)
    m=int(((bottle%48)%24)/12)
    s=int((((bottle%48)%24)%12)/6)
    print( xl,"xl," , l,"large,",m,"medium,",s,"small")
bottle_shipping()
    
