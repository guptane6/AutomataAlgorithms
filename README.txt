Neha Gupta
CSE 460 Honors Project


 _   _ ______     _        ______ _____         
 | \ | |  ____/\  | |      |  ____/ ____|  /\    
 |  \| | |__ /  \ | |_ ___ | |__ | (___   /  \   
 | . ` |  __/ /\ \| __/ _ \|  __| \___ \ / /\ \  
 | |\  | | / ____ \ || (_) | |    ____) / ____ \ 
 |_| \_|_|/_/    \_\__\___/|_|   |_____/_/    \_\
                                                 
System Requirements:
----------------------------------------------------------------
Python version 3                                                


How to run:
----------------------------------------------------------------
Windows python application:
Open NFAtoFSA.py via right clicking and selecting Edit-With-Idle
Run module (F5)


Command-line:
$ python NFAtoFSA.py
or
$ python3 NFAtoFSA.py


Included Test Files
------------------------------------------------------------------

NFA1.txt from lecture slides of conversion of NFA to FA

NFA2.txt from some other course materials (lecture slides?)

NFA3.txt is the textual form of the NFA on page 128 of the 
textbook.

NFA4.txt from figure 4.10 in the textbook



Test File Format
------------------------------------------------------------------

The input file has the transition function listed line by line 
separated by commas where the first item on the line is the 
starting state, the second item is the transition and the 3rd 
element is the second state.

    Eg:
    1,a,3
    1,a,3
    
would indicate that the state 1 goes to 3 with a 
and state 1 goes to 2 on b.

The accepting states are listed with "Accepting = statenum"

Initial state listed as "Initial = statenum"