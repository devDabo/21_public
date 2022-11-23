suit = ["Diamonds" , "Clubs", "Hearts", "Spades"]
card_value = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]


pack=[[0]*52 for x in range(2)]
for card_number in range (0,51):
    pack[0][card_number]=suit[card_number%4]
    pack[1][card_number]=card_value[card_number%13]

print(pack)
print(pack[1][2], "of " + pack[0][2])
