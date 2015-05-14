import random
words_first=("Thee","Ye","Thou","Ye Olde")
print (random.choice(words_first))

words_second=("tottering","fobbing","loggerheaded","saucy","goatish","spongy","mammering","wayward","lumpish","surly","dankish","fawning","pribbling","yeasty","mewling")
print (random.choice(words_second))

words_third=("fly-bitten","beetle-headed","elf-skinned","dizzy-eyed","hedge-born","swag-bellied","onion-eyed","rude-growling","knotty-pated","doghearted","common-kissing","bat-following","flap-mouthed","boil-brained","sheep-biting")
print (random.choice(words_third))

words_fourth=("pignut","harpy","barnacle","boar-pig","apple-john","malt-worm","measle","lewdster","flap-dragon","giglet","foot-licker","dewberry","bum-bailey","haggard","maggot-pie")
print (random.choice(words_fourth))

question= input("Would you like another insult? y/n")
if question== "y" or question== "Y":
    print (random.choice(words_first))
    print (random.choice(words_second))
    print (random.choice(words_third))
    print (random.choice(words_fourth))
else:
    print ("Ok")
