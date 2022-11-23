import random

card_list = []

suit = ["Diamonds" , "Clubs", "Hearts", "Spades"]
card_value = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]

pack=[[0]*52 for x in range(2)]
for card_number in range (0,52):
    pack[0][card_number]=suit[card_number%4]
    pack[1][card_number]=card_value[card_number%13]

for i in range(0,4):
    for j in range(0,13):
        card_picture = (pack[1][j], "of " + pack[0][i])
        card_list.append(card_picture)

#print(card_list)
card_split = ([0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0])

# for i in card_split:
#     for x in i:
#         print(x)
#     print(i)

random.shuffle(card_list)

pack_position=0

for row in range (0,7):
    card_split[0][row]=card_list[pack_position]
    pack_position=pack_position+1
    card_split[1][row]=card_list[pack_position]
    pack_position=pack_position+1
    card_split[2][row]=card_list[pack_position]
    pack_position=pack_position+1
print(card_split)

pack_position=0

#def select(user_input):
print("Choose a card, tell me which pile it is in")
user_input = input()
if user_input == "1":
    print("You chose Pile 1")
    pack_position=0
    for row in range (0,7):
        card_split[1][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[0][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[2][row]=card_list[pack_position]
        pack_position=pack_position+1
elif user_input == "2":
        print("You chose Pile 2")
        pack_position=0
        for row in range (0,7):
            card_split[2][row]=card_list[pack_position]
            pack_position=pack_position+1
            card_split[1][row]=card_list[pack_position]
            pack_position=pack_position+1
            card_split[0][row]=card_list[pack_position]
            pack_position=pack_position+1
elif user_input == "3":
    print("You chose the Pile 3")
    pack_position=0
    for row in range (0,7):
        card_split[0][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[2][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[1][row]=card_list[pack_position]
        pack_position=pack_position+1
else:
    print("Invalid input")

print(card_split)

print("Choose a card, tell me which pile it is in")
user_input = input()
if user_input == "1":
    print("You chose Pile 1")
    pack_position=0
    for row in range (0,7):
        card_split[1][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[0][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[2][row]=card_list[pack_position]
        pack_position=pack_position+1
elif user_input == "2":
        print("You chose Pile 2")
        pack_position=0
        for row in range (0,7):
            card_split[2][row]=card_list[pack_position]
            pack_position=pack_position+1
            card_split[1][row]=card_list[pack_position]
            pack_position=pack_position+1
            card_split[0][row]=card_list[pack_position]
            pack_position=pack_position+1
elif user_input == "3":
    print("You chose the Pile 3")
    pack_position=0
    for row in range (0,7):
        card_split[0][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[2][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[1][row]=card_list[pack_position]
        pack_position=pack_position+1
else:
    print("Invalid input")


print(card_split)

print("Choose a card, tell me which pile it is in")
user_input = input()
if user_input == "1":
    print("You chose Pile 1")
    pack_position=0
    for row in range (0,7):
        card_split[1][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[0][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[2][row]=card_list[pack_position]
        pack_position=pack_position+1
elif user_input == "2":
        print("You chose Pile 2")
        pack_position=0
        for row in range (0,7):
            card_split[2][row]=card_list[pack_position]
            pack_position=pack_position+1
            card_split[1][row]=card_list[pack_position]
            pack_position=pack_position+1
            card_split[0][row]=card_list[pack_position]
            pack_position=pack_position+1
elif user_input == "3":
    print("You chose the Pile 3")
    pack_position=0
    for row in range (0,7):
        card_split[0][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[2][row]=card_list[pack_position]
        pack_position=pack_position+1
        card_split[1][row]=card_list[pack_position]
        pack_position=pack_position+1
else:
    print("Invalid input")
#print(card_split.extend([0]))

print(card_split)
exit = input("press enter to close")
