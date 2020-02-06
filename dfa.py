##Authors:   Oulis Evangelos
##Subject:   A silple lectical analyzer
##				using the simple deterministic finite automatic.
#===================================================================
#!/usr/bin/env python

import sys, traceback

try:
	with open('dfa.txt', 'r') as f:
		count_states = int(f.readline().rstrip('\n'))
		alphabet = f.readline().rstrip('\n').split(' ')
		start_state = f.readline().rstrip('\n')
		final_states = f.readline().rstrip('\n').split(' ')
				
		states = dict()		# each state inserts to a dictionary.
						# dictionary uses the id of state for primary key.
		#state={"n" : [[<input> <next_state>] [<input> <next_state>]]}
		
		
		#Read line-line the file except the \n character.
		line = f.readline().rstrip('\n')
		while line != None and line != '':
			#While reading -> building the automata.
			cur = line.split(' ')
			
			#Check if an input isn't into the alphabet.
			if not (cur[1] in alphabet):
				print('An alphabet problem accurred. You are referenced to an not alphabet symbol.')
				sys.exit()
			
			if not (cur[0] in states):
				states[cur[0]] = []
			
			states[cur[0]].append([cur[1], cur[2]])
			
			line = f.readline().rstrip('\n')
		
		print("======TRUETH TABLE========\n")
		print("State\t\tInput\t\tNext State\n")
		
		
		for key, s in states.items():
			for s1 in s:
				print (str(key) + "\t\t" + s1[0] + "\t\t" + s1[1])
		
		print ("==========================\n\n\n")
		while True:
			#Wait to get an input from user.
			user = str(input('##Give me an Input <exit()> for exit.:    '))
			
			#Exit if he wants.
			if user == 'exit()':
				break
			
			#Initialize the state to first state.
			index = 0
			state = start_state
			
			wrong = False
			#Read the user's input character-character.
			for user_char in user:
				#If user gave a false symbol.
				if (not user_char in alphabet):
					wrong = True
					break
				
				found = False
				#Get to next state.
				for j in states[state]:
					if j[0] == user_char:
						state = j[1]
						
						found = True
						break
				
				if not found:
					break
			
			#Prints the result.
			if state in final_states and not wrong:
				print("\n---> RESULT: OK\n\n")
			else:
				print("\n---> RESULT: NOT OK\n\n")
		

except TypeError as e:
	print("An error accurred. Descr: " + str(e))
	
	exc_type, exc_value, exc_traceback = sys.exc_info()
	print ("*** print_tb:")
	traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

except IOError as e:
	print("An error accurred on file opening. Descr: " + str(e))
	print ("You must provide a file DFA description.")
	
	exc_type, exc_value, exc_traceback = sys.exc_info()
	print ("*** print_tb:")
	traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

