#ICSE 2017 7(a)
#Name: Ritvik Sai C
#Roll no.: cs21btech11054

#computes the interest at the end of 6 months 
def computedue(p,r,t):
    return (p*r*t/(100*365))
    
p1 = 3000 #The principle
r = 6 #rate of interest
t1= 3 #no of days in the bank

interest1= computedue(p1,r,t1)
 
p2 = 5600 #The principle
r = 6 #rate of interest
t2= 29 #no of days in the bank    

interest2= computedue(p2,r,t2)
    
p3 = 4100 #The principle
r = 6 #rate of interest
t3= 58 #no of days in the bank

interest3= computedue(p3,r,t3)
    
p4 = 2000 #The principle
r = 6 #rate of interest
t4= 28 #no of days in the bank

interest4= computedue(p4,r,t4)
    
p5 = 8500 #The principle
r = 6 #rate of interest
t5= 23 #no of days in the bank

interest5= computedue(p5,r,t5)

p6 = 10000 #The principle
r = 6 #rate of interest
t6= 34 #no of days in the bank

interest6= computedue(p6,r,t6)

interest=  interest1 + interest2 + interest3 + interest4 + interest5 + interest6

print("interest at the end of 6 months = ",interest);