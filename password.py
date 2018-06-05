import os
import sys
import string
import random
import time
from time import sleep #to get program to "sleep" to simulate loading
import pyperclip #to copy paste from terminal

# Used to simulate loading progress of the main program
start_loading = '\n\n\n\nLoading'
loading = '.' * 120 + '\n\n'

#clears the IDLE
os.system('cls') #for windows

# use the next line if you are on linux
# os.system('clear') 

#use input() so user has to type enter for next line to appear	
userInput = "" # initialize variable userInput as empty string
input("Welcome to the password generator! Hit <enter> to continue!")
input("You have two options for your password:")
input("1) Pick a word of your choice, your password will be based on the word you choose.")
input("2) Use a completely randomized password chosen by this application. (Note: Safer Choice)")


while(userInput != '1' or '2'):
	userInput = input("Type in '1' or '2' without the quotation marks - followed by <enter> to continue \n\n")
	os.system('cls')

	#user selects option 2
	if(userInput == '2'):
		#user selects input length of password
		initPw2 = input("How many characters do you want your password to be: ")
		while (initPw2.isdigit() == False): # use while true loop to force user to input value
			print("\n\nError: You did not enter digits...\nPlease enter digit(s) only")
			initPw2 = input("How many characters do you want your password to be: ")
		pwlength2 = int(initPw2)
		os.system('cls')

		# Used to simulate loading progress of the main program
		print(start_loading)
		for c in loading:
		    print(c, end = '')
		    sys.stdout.flush()
		    sleep(0.025)

		#Clear the IDE...
		os.system('cls')

		#initialize full range of characters on keyboard
		pwchar = string.ascii_letters + string.punctuation + string.digits

		#initialize "password" as empty string to use in for loop
		password2 = ""

		#for loop - add random characters to create password
		for x in range(pwlength2):
		    char = random.choice(pwchar)
		    password2 += char

		print("Your password is:")
		print(password2 + "\n\n")
		pyperclip.copy(password2)
		pyperclip.paste()
		print("Password has been copied to your clipboard... Hit <ctrl-v> to show!")
		input("Hit <enter> to end this program")
		break

	#user selects option 1
	elif(userInput == '1'):
		initPw1 = input("How many characters do you want your password to be: ")
		while (initPw1.isdigit() == False): # use while true loop to force user to input value
			print("\n\nError: You did not enter digits...\nPlease enter digit(s) only")
			initPw1 = input("How many characters do you want your password to be: ")
		pwlength1 = int(initPw1)

		# while loop to ensure length over user input is within boundaries of requested character limit.
		while True:
			userChoice = input("Enter your word of choice: ")		
			if(len(userChoice) == pwlength1): 
				print("\nError: Number of characters in word of choice cannot be equal to number of characters set in first line \nPlease try again \n\n")
			if(len(userChoice) > pwlength1): 
				print("\nError: Number of characters in word of choice cannot be more than number of characters set in first line \nPlease try again \n\n")
			if(len(userChoice) < pwlength1):
				break

		os.system('cls')

		# Used to simulate loading progress of the main program
		print(start_loading)
		for c in loading:
		    print(c, end = '')
		    sys.stdout.flush()
		    sleep(0.025)

		os.system('cls')

		password1 = ""

		#for loop to jumble capitalization of letters
		for k in userChoice:
		  password1 += "".join(random.choice([k.upper(), k]))

		#for loop to add digits to the end of jumbled letters
		# note: n - 1 --- so as to leave space for addition of one random symbol from string.punctuation
		loopTimes = pwlength1 - len(userChoice) - 1
		for i in range(loopTimes):
			password1 += random.choice(string.digits)
		print("Your password is: \n" + password1 + random.choice(string.punctuation) + "\n\n")
		pyperclip.copy(password1)
		pyperclip.paste()
		print("Password has been copied to your clipboard... Hit <ctrl-v> to show!")
		input("Hit <enter> to end this program")
		break
	else:
		print("You have entered an invalid option")
	
		


