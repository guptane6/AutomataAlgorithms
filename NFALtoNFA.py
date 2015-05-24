############################################################
#   Neha Gupta
#   CSE 460 Honors Proj
#   NFA/\ to NFA without /\ transitions
############################################################
#from operator import itemgetter
#import itertools
import copy


#Definitly include the alphabet in the file
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
    nfa_trans = dict()
    
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
            print(alphabet, type(alphabet))
            alphabet = list(alphabet)
            alphabet.sort()
            print(alphabet)
            numletters = len(alphabet)
            emptytrans = ("{} "*len(alphabet)).split()
        else:
            line = tuple(i.strip().split(","))
            print(line)
            if line[0] not in liststates:
                liststates.add(line[0])
                nfa_trans[line[0]] = copy.deepcopy(emptytrans)
            if line[1] != "l":
                index = alphabet.index(line[1])
                nfa_trans[line[0]][index] = line[2]
                print(nfa_trans)
            liststates.add(line[2])
            
            #alphabet.add(line[1])
            


    print("NFA-/\ Accepting: ", accepting)
    print("NFA-/\ Initial: ", initial)
    print("NFA-/\ list-states: ", liststates)
    print("NFA-/\ alphabet: ", alphabet)
    print("NFA trans: ", nfa_trans)
    

NFALtoNFA()
