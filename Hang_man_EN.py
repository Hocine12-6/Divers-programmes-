import random # Import random module
import string
words = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar',
         'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat',
         'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt',
         'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven',
         'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider',
         'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf',
         'wombat', 'zebra']# Word list to choose randomly
word = random.choice(words) # Randomly choose a word from the previous list

espace =("_ "*len(word)).split() # Make a list of spaces with the same length as the random word
print(" ".join(espace))# Print the spaces as a sentence, separating each underscore for clarity to the user

tries=7 # Set variable as attempt counter
false_guses=[]# List to record what the user entered
tries1use = 0
print('''
  +---+
      |
      |
      |
      |
      |
=========''')
print ("***The tries are your attempts*** ")
print("   TRIES = 7")
while  ("_"  in espace ) and ( tries > 0 ) : # As long as there are spaces and attempts > 0, repeat
	user_gues=input("__________\nGues a carecter :").lower() # Ask user to guess a character
	
##########################
	punctuation=False
	if user_gues:
	 		 			for x in user_gues:
	 		 				if x in string.punctuation:
	 		 					punctuation=True
	 		 					break
 
		
	if user_gues == "ls logs":# Print list of wrong letters input by the user 
		if len(false_guses) !=0:
			print("-".join(false_guses))
		else:
			print("YOUR LOGS ARE NONE")
		continue
		
	elif user_gues == "exit":# Exit the game
		exit()
		
	elif user_gues == "ls tries":# Show remaining attempts
		print(tries)
		continue
		
