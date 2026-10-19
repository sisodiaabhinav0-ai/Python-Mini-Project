#Definig the menu of the hotel 
menu={
    "Pizza":200,
    "Pasta":100,
    "Cold Coffee":80,
    "Fries":50,
    "Spring Roll":120
}
#greeting
print("Welcome to our restaurant")
print("Pizza: 200\nPasta: 100\nCold Coffee: 80\nFries: 50\nSpring Roll: 120 ")

orderTotal = 0

#taking order
item1= input("What would you like to order? ")
if item1 not in menu:
    print(f"Sorry we don't have {item1}")
elif item1 in menu:
    orderTotal +=menu[item1]
    print(f"Your item {item1} has been added to your order")

anotherOrder=input("Do you want anything else? (Yes/No) ")
if anotherOrder.lower() == "yes":
    iteam2 = input("Please enter second item: ")
    if iteam2 in menu:
        orderTotal += menu[iteam2]
        print(f"Item {iteam2} has been added to your order ")
    else:
        print("Sorry we dont have that")
else:
    print("Thank you for ordering")

print(f"Total amount you have to pay is {orderTotal}")



#this is the end
