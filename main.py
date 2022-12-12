import random

#Defined three empty lists. They have to be filled with zeros as the cards are not appended to them.
card_split_one = [0,0,0,0,0,0,0]
card_split_two = [0,0,0,0,0,0,0]
card_split_three = [0,0,0,0,0,0,0]

#The 21 cards are added to card_orig, which are then added to card_list
card_orig = []
card_list = []

card_list.append(card_orig)

suit = ["Diamonds" , "Clubs", "Hearts", "Spades"]
card_value = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]

# for loop which adds the card value and the suit. % is used to use all the suits for all the pictures

for card_number in range (0,52):
    card_orig.append(card_value[card_number%13] + " of " + suit[card_number%4])

random.shuffle(card_orig)

#adds 21 cards from the 52 to card_list.
for card_number in range (0,21):
    card_list.append(card_orig[card_number])

#Carries out card split and card selection then card_list clear.
def card_trick():
    pack_position = 0

    #using global statement avoid an unbound Local error
    global card_split_one
    global card_split_two
    global card_split_three

    #Writes the values from the 21x1 to 7x3, instead of 1,2,3,4 etc. it writes 1,4,7,10 etc.
    for col in range (0,7):
        card_split_one[col]=card_list[0][pack_position]
        pack_position=pack_position+1
        card_split_two[col]=card_list[0][pack_position]
        pack_position=pack_position+1
        card_split_three[col]=card_list[0][pack_position]
        pack_position=pack_position+1

    print("Pile 1" , card_split_one)
    print("Pile 2" , card_split_two)
    print("Pile 3" , card_split_three)

    #if 1st column is picked then the first list is placed in the middle
    print("Choose a card, tell me which pile it is in")
    user_input = input()
    if user_input == "1":
        print("You chose pile 1")
        card_split_one,card_split_two=card_split_two, card_split_one
    elif user_input == "2":
        print("You chose pile 2")
    elif user_input == "3":
        print("You chose pile 3")
        card_split_three,card_split_two=card_split_two, card_split_three
    else:
        print("Invalid input")

    #This adds the three lists and combines then into one.
    combined_array = card_split_one + card_split_two + card_split_three
    #empties the previous card_list and then adds the new cards to it.
    del card_list[:]
    card_list.append(combined_array)

#tries is the iterating variable
for tries in range(0,3):
    card_trick()
#iterates and adds to the loop.
tries = tries + 1

#The card will be the 11th card. This will be [10] as the list starts at 0.
print("Your card is the" , card_list[0][10])
