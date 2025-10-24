print("Loops")
print("=====")
print()

print("For loop with list:")
list = ["Bla", "Blub", "Nudelsuppe"]

for entry in list:
    print(entry)

input("press enter for next") 

print()
print("For loop with dict:")

dict = {
    "Bla": 5,
    "Blub": 8,
    "Nudelsuppe": 10
}

for key in dict:
    value = dict[key]
    print(key +": "+ str(value))

input("press enter for next") 

print()
print("For loop with string:")

text = "Nudelsuppe"

for letter in text:
    print(letter)

input("press enter for next") 

print()
print("For loop with range")

for i in range(1, 10):
    print("Loop "+ str(i))

input("press enter for next") 

print()
print("For loop with range and continue on 5")

for i in range(1, 10):
    if i == 5:
        continue
    print("Loop "+ str(i))


input("press enter for next") 

print()
print("For loop with range and break on 5")

for i in range(1, 10):
    if i == 5:
        break
    print("Loop "+ str(i))

input("press enter for next") 

print()
print("While loop with lower")

i = 1
while (i < 5):
    print(i)
    i += 1

input("press enter for next") 

print()
print("While loop with lower equals")

i = 1
while (i <= 5):
    print(i)
    i += 1

input("press enter for next") 

print()
print("While loop infinite")

i = 1
while (True):
    print(i)
    i += 1
