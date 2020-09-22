# Week 2
# Hester Huisman

# 2.1
a = "All"
b = " work"
c = " and"
d = " no"
print(a+b+c+d)

# 2.2
print(6*(1-2))

# 2.4
bruce = 6
print(bruce + 4)

# 2.5
P = float(input("Please enter the principle amount: "))
r = float(input("Please enter the annual nominal interest rate: "))
n = float(input("Please enter the number of times the interest is compounded per year: "))
t = float(input("Please enter the number of years: "))

A = (P*(1+r/n))**(n*t)
print(A)

# 2.6
# last one gave an error term

# 2.7 & 2.8
Start_time = float(input("Please enter the start time hh.mm: "))
Hours = int(input("Please enter the number of hours to wait: "))

End_time = (Start_time + (Hours % 24))
print(End_time)


# Travel model
D = int(input("Please enter the distance in whole km: "))
M = input("Please enter the mode of transportation: walking/biking/car: ")

#speed
if M == "walking":
    Speed = 20
elif M == "biking":
    Speed = 5
else:
    Speed = 1
Speed = int(Speed)

# total time
Parking_Car = input("Please enter how many minutes it takes to park the car: ")
Parking_Bike = input("Please enter how many minutes it takes park the bike: ")

if M == "walking":
    Total = D*Speed
elif M == "biking":
    Total = D*Speed
else:
    Total = D*Speed
Total = int(Total)

Hours = (Total//60)
Minutes = (Total % 60)
print(Hours, "hours and", Minutes, "minutes")