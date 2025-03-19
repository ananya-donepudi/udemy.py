print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 15:
    bill = 7
    print("Your tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
else:
  print("sorry! you are not eligible to ride the rollercoaster.")
wants_photo = input("Do you want a photo taken? (Y or N): ")
if wants_photo == "Y" or "y":
  bill += 3
  print(f"Your final bill is ${bill}")
print("Thank You!")
