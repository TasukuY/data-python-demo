# first_name = 'Tasuku'
# last_name = 'Yamamoto'
# favorite_drink = '''tea
# and cocoa
# and lemonade
# and iced tea'''
# print(favorite_drink)

# age = 29
# bank_account = 14.99
# loves_me_some_Python = True

# # print(type(age))
# # print(type(bank_account))
# # print(type(loves_me_some_Python))

# if age >= 18:
#     print("I'm an adult")
# elif age >= 13:
#     print("I'm a teen")
# else:
#     print("I'm a child")

# if age >= 18 and bank_account > 0:
#     print("Good job adulting!")

# for x in [1, 2, 3, 4, 5]:
#     print(x)

# instructors = ["trew", "jeddy", "alec"]
# for instructor in instructors:
#     print(instructor.capitalize())

open_file = open("FinalGrades.csv")

total_a = 0
total_b = 0
total_c = 0

for line in open_file:
    line = line.rstrip('\n').split(',')
    # print(line)
    for value in line:
        # print(value[0])
        if value == "A":
            total_a += 1
        elif value == "B":
            total_b += 1
        elif value == "C":
            total_c += 1
        
# print("A's: ", total_a)
# print(f"B's: {total_b}")
# print(f"C's: {total_c}")

open_file.close()

