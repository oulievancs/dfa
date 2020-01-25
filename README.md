# DFA | Oulis Evangelos
-----
Deterministic Finite Auto for Computational Theory at UniWA.

Program reades from a file named <dfa.txt> a description for a Deterministic Finite Auto.
This file must have the folowing format:

dfa.txt
-------
3 			// The automatic has 3 states
0 1 		// The alphabet has 2 symbols, 0 and 1
0 			// The initial state is q0
0 1 		// The final state is q0 and q1
0 1 1 		// If the automatic is in the state q0 by 1 it will switch to the state q1
0 0 0 		// If the automatic is in the state q0 with 0 will switch to the state q0
1 1 2 		// If auto is in q1 mode with 1 it will switch to q2 mode
1 0 0 		// If the automatic is in the q1 state with 0 it will switch to the q0 state
2 1 2 		// If the automatic is in q2 mode with 1 it will switch to q2 mode
2 0 2 		// If the automatic is in q2 mode with 0 will switch to q2


Then the user give an input and program decides if it is ok or wrong following the given
<txt> description. Program ends when user give exit().
