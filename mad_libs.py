firstAdjective = input("Enter an adjective: ")
firstVerb = input("Enter a verb:" )
secondAdjective = input("Enter an adjective: ")
firstNoun = input("Enter a noun: ")
firstColor = input("Enter a color: ")
firstPluralNoun = input("Enter a plural noun: ")
secondVerb = input("Enter a verb: ")
thirdAdjective = input("Enter and adjective: ")
thirdVerb = input("Enter a verb: ")
secondNoun = input("Enter a noun: ")
fourthAdjective = input("Enter an adjective: ")


firstLine = "Tonight is the night when all of the {} Monsters".format(firstAdjective)
secondLine = "come out to {}. {} Witches with big".format(firstVerb,secondAdjective)
thirdLine = "{} and {}".format(firstNoun, firstColor)
fourthLine = "make potions and very spooky brews. Vampires with"
fifthLine = "{} and long red capes visit with friends and search".format(firstPluralNoun)
sixthLine = "for neck napes. Ogres and Ghosts sometimes {}".format(secondVerb)
seventhLine = "and play, on this {} October day. All the".format(thirdAdjective)
eigthLine = "TRICK-OR-TREATERS {} and hunt for {}".format(thirdVerb, secondNoun)
ninthLine = "and scare, dressed up as princesses and cowboys here and"
tenthLine = "there. Have a {} HALLOWEEN IN 2017!".format(fourthAdjective)

print('\n')
print(firstLine+ '\n' + secondLine +  '\n' +  thirdLine +  '\n' +  fourthLine)
print(fifthLine+ '\n' + sixthLine +  '\n' +  seventhLine +  '\n' +  eigthLine)
print(ninthLine+ '\n' + tenthLine +  '\n')
