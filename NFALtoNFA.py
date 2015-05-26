############################################################
#   Neha Gupta
#   CSE 460 Honors Proj
#   NFA/\ to NFA without /\ transitions
############################################################

from operator import itemgetter
import copy

#Perhaps change input file to standard capital L's? difficult to tell apart lower l and number 1. 

#Definitely include the alphabet in the file
#Then make nfa of the format [[statename,a trans,btrans],[state2, a.., b..]]
#start with empty blanks and fill them in as you go


#REQUIREMENT OF TEXT FILE:
#Alphabet must be listed before transition table
def NFALtoNFA():
    fname = input("Please enter file name of textual NFA-/\: ")
    try:
        fobj = open(fname, "r")
    except FileNotFoundError:
        print("Filename does not exist")
        return

    nfal = list()
    accepting = list()  #list of accepting states
    liststates = set()
    initial = ''
    alphabet = set()
    nfal_trans = list() #list of tuples (first state, trans, second state)
    nfa_trans = dict() #key = statenum, value = [[list of a trans], [list of b trans], [list of ...]]
    #order of transitions as listed in value is consistent, and determined by alphabetized
    #alphabet specified in text file
    
    ###   READING TEXT FILE AND BUILDING NFA-/\ STRUCTRUE
    for i in fobj:
        line = i.strip().split()
        #print(line)
        if line == "" or line == "\n" or line == "\t" or line == []:
            #print("cont")
            continue
        elif (line[0].lower() == "initial"):
            #print("in init")
            initial = line[2]
            liststates.add(line[2])
        elif (line[0].lower() == "accepting" or line[0].lower() == "final"):
            #print("accept")
            accepting.append(line[2])
            liststates.add(line[2])
        elif (line[0].lower() == "alphabet" or line[0].lower() == "sigma"):
            alphabet = set(line[2].strip().split(","))
            alphabet = list(alphabet)
            alphabet.sort()
            numletters = len(alphabet)
            emptytrans = ("{} "*len(alphabet)).split() #this is used in initializing nfa struct
        else:
            line = tuple(i.strip().split(","))
            nfal_trans.append(line)
            if line[0] not in liststates or line[0] not in nfa_trans:
                liststates.add(line[0])
                nfa_trans[line[0]] = copy.deepcopy(emptytrans)
            if line[1] != "l":
                index = alphabet.index(line[1])
                #nfa_trans[line[0]][index] = [line[2]]   #Hmm cut back???
                if nfa_trans[line[0]][index] == "{}":
                    nfa_trans[line[0]][index] = [line[2]]
                else:
                    nfa_trans[line[0]][index].append(line[2])

                #print(nfa_trans)
            liststates.add(line[2])
            
            #alphabet.add(line[1])
    nfal_trans = sorted(nfal_trans, key=itemgetter(0,1,2))        
    #sorts nfal by first state ascending, then transition, then second state
    #may not need. such inefficient if not lolol

    print("NFA-/\ Accepting: ", accepting)
    print("NFA-/\ Initial: ", initial)
    print("NFA-/\ list-states: ", liststates)
    print("NFA-/\ alphabet: ", alphabet)
    print("NFA trans: ", nfa_trans)
    print("NFA-/\ trans: ", nfal_trans)
    

NFALtoNFA()
