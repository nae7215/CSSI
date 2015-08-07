# user_guess = input("Guess A Number 1-10")
# actual_number = 3
#
# if (user_guess == actual_number):
#     print 'you won'
# elif (user_guess > actual_number):
#     print 'you lost too high'
# else:
#     print 'you lost too low'


# some_numbers =[2, 52, 19, 46, 1000]
#
# for i in some_numbers:
#     print (i + 10) / 2

# words = ['mary', 'had', 'a', 'little', 'lamb']
#
# for i in words:
#     word = words[::-1]
#     words = word
# print words

# def add(x,y): #def is how to define a function
#     return x + y
# print add(3,5)

# def first_letters(words)
#     for name in words:
#         letters.append(words)
#     return letters
#
# words = ['Zach', 'Arely', 'Mannuel', 'Yulissa']
# first_letters(words) #['z','a','m','y']



# dwarf_names = ['Doc', 'Dopey', 'Bashful', 'Grumpy'] #this is just defining a list
#
# def order(random_list): #this is defining a function called "order" for a PLACEHOLDER list called "random_list"
#
#     for name in random_list: #"name" is just one piece of "random_list" separated from the others with commas
#         print name #this executes the function visibly
#
#
# order(dwarf_names) #this puts the list "dwarf_names" in for the placeholder list "random list" above
# order(["one", "cow", "bear"]) #^same


# planeteer_calls = ['earth', 'wind', 'fire', 'water', 'heart']
#
# def first_letter(random_list):
#
#     for word in random_list:
#         word = str.capitalize(word)
#         print word
#
# first_letter(planeteer_calls)


percy_invitation = "The family of Percy Weasley proudly invite you to their graduation commencement on Saturday the 22nd of May 1993. Festivities will be held at The Burrow. See you then!"

ron_invitation = percy_invitation.replace("Percy","Ron").replace("Saturday","Sunday").replace("22nd","18th").replace("1993","1997")

print ron_invitation
