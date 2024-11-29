# Description: This program creates invoices for The Edsel Car Rental Company.
# Author: Justin Greenslade. 
# Class: Python SD 13.
# Dates: Sept 10 - Sept 20/ 2024 


#Assigned program constants
RENT_PER_DAY = 75.00 # Cost of automobile per day.
PER_KM_COST = 0.26 # Cost per km traveled.
INSUR_COST = 17.00 # Cost of Insurance on rental per day.
WINTER_DIS_RENTAL = .10 # Winter discount of 10% of Rentails
WINTER_DIS_MILE = .25 # Winter discount of 25% off mileage.
TAX = .15 # HST of 15%.


#Gathered user input.
print()
CustName = input("Enter the Customer name: ")
CustPhone = input("Enter the Customer phone number: ")
print()
DaysRented = input("Enter the number of days rented: ")
DaysRented = int(DaysRented) # input becomes a integer.
Odometer = input("Enter odometer reading at start of rental: ")
Odometer = int(Odometer) # input becomes a integer.
ReOdometer = input("Enter odometer reading at return of rental: ")
ReOdometer = int(ReOdometer) # input becomes a integer.)
print()


#Calculations
KmTot = ReOdometer - Odometer # calculates total km driven during rental
RentCost = DaysRented * RENT_PER_DAY # calculates total rental cost without the Km added
MileCost = KmTot * PER_KM_COST # calculates total mileage cost in km.
InsCost = DaysRented * INSUR_COST # calculates total insurance cost of rental.
DisRent = RentCost * WINTER_DIS_RENTAL # Calculates discount of rental during winter.
DisMile = MileCost * WINTER_DIS_MILE # Calculates discount of mileage during winter.
TotDis = DisRent + DisMile # Calculate total discount.

TotRentCost = RentCost + MileCost + InsCost - TotDis # Calculates total rental cost before taxs.
HST = TotRentCost * TAX # Calculates amount of taxs ( at 15% )
FinInvTot = TotRentCost + HST # Final invoice total cost for customer.

#Print/Display all values.
print("Customer name:                                                ", CustName)
print("Customer Phone Number:                                        ", CustPhone)

print()

print("The Number of days rented:                                    ", DaysRented)
print("The odometer reading at start of rental:                      ", Odometer)
print("The odometer reading at return of rental:                     ", ReOdometer)

print()

print("Total Mileage driven during rental:                           ", KmTot)
print("Total per day rental cost:                                    ",RentCost)
print("Total per km Mileage cost:                                    ", MileCost)
print("Total Insurance cost:                                         ", InsCost)

print()

print("Rental Winter discount:                                       ", DisRent)
print("Mileage Winter discount:                                      ", DisMile)
print("Total discount:                                               ", TotDis)
print()
print("Total rental cost:                                            ", TotRentCost)
print("HST:                                                          ", HST)
print("Final Invoice Total:                                          ", FinInvTot)