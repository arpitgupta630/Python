fruits = ['Orange', "Banana", 'Apple', "Kiwi",
          "Straberry", "Pomogranate", "Grapes"]

# For Loop
print("***For Loop***")
for fruit in fruits:                        # Clean Syntax
    print(fruit)

# While Loop
print("\n***While Loop***")
i = 0
while i < len(fruits):                      # Lenghty & Messy Syntax
    print(f"{i+1}. {fruits[i]}")
    i += 1
