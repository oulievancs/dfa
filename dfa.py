##Authors:   Oulis Evangelos
##Subject:   A silple lectical analyzer
##				using the simple deterministic finite automatic.
#===================================================================
#!/usr/bin/env python

import sys, traceback

try:
	f=open('dfa.txt', 'r')
	if f != None:
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
			#Wrile reading -> building the automata.
			cur = line.split(' ')
			if not (cur[0] in states):
				states[cur[0]] = []
			
			states[cur[0]].append([cur[1], cur[2]])
			
			line = f.readline().rstrip('\n')
		
		while True:
			#Wait to get an input from user.
			user = input('##Give me an Input <exit()> for exit.:    ')
			
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
				
				#Get to next state.
				for j in states[state]:
					if j[0] == user_char:
						state = j[1]
						break
			
			#Prints the result.
			if state in final_states and not wrong:
				print("\n---> RESULT: OK\n\n")
			else:
				print("\n---> RESULT: NOT OK\n\n")
						
	else:
		print ("You must provide a file DFA description.")
except TypeError as e:
	print("An error accurred. Descr: " + str(e))
	
	exc_type, exc_value, exc_traceback = sys.exc_info()
	print ("*** print_tb:")
	traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

except IOError as e:
	print("An error accurred on file opening. Descr: " + str(e))
	
	exc_type, exc_value, exc_traceback = sys.exc_info()
	print ("*** print_tb:")
	traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

