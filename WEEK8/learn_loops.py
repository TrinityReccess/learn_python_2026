# print("***********COUNTER*************")
# print("This is a program that counts numbers according to what you input.")

# from_number = int(input("Please enter where you want to start from: "))
# end_number = int(input("Please enter where you want to end: "))


# for value in range(from_number, end_number):
#     print(f"This is number: {value}")
    
    
# country = input("Enter the country: ")

# for chr in country:
#     print(chr)
    
#     if chr == "a":
#         print("This country has 'a' in it")


# counter = 1

# while counter <=5:
#     print(f"The current count is {counter}")
    
#     counter +=1



print("ATM MACHINE 🏧🏧🏧")

MAX_ATTEMPTS = 3
user_attempts = 0
correct_pin = "1232"

while user_attempts < MAX_ATTEMPTS:
    user_pin = input("Please enter PIN: ")
    if user_pin == correct_pin:
        print("Success ✅")
        break
    user_attempts = user_attempts + 1
else:
    print("Your account has been blocked ❌")
    
