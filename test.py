msg = "Test python"

print(msg)

# Use this tag to make comments obviously

name = "Marie"

if name == "Nat":
    print("Hey!")
elif name == "Marie":
    print("Ur name is Marie")
else:
    print("Nayyy")

import random

def RandomerNumberer(name):
    print(name + " rolled: " + str(random.randint(1,10)))

RandomerNumberer(name)

cats = ["Muhammad", "Bobo", "Charlie", "Kazik", "Baltazar"]

def PrintCatsByRange(cats):
    for i in range(0, len(cats)):
        print(str(i) + " Cat " + cats[i])

def LoopPrintCats(cats):
    for cat in cats:
        print(cat)

LoopPrintCats(cats)
PrintCatsByRange(cats)