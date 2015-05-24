############################################################
#   Neha Gupta
#   CSE 460 Honors Proj
#   Michigan State University under Prof Torng
#   NFA to FSA algorithm
############################################################
import copy

def NFAtoFSA():
    '''Input: NFA M1 (without Lambda transitions). The input file has
    the transition function listed line by line separated by commas where
    the first item on the line is the starting state, the second item is
    the transition and the 3rd element is the second state.
    Eg:
    1,a,3
    1,a,3
    would indicate that the state 1 goes to 3 with a
    and goes to 2 on b.
    Then, the accepting states are listed with "Accepting = statenum"
    Initial state similarly listed
    Prints components of FSA calculated
    Sample files given include NFAM1, from Mod 14 NFAtoFA.pdf
    '''
    fname = input("Please enter file name of textual NFA: ")
    try:
        fobj = open(fname, "r")
    except FileNotFoundError:
        print("Filename does not exist")
        return

    transitionfx = dict()
    #transitionfx is nfa transition vector (of other vectors) in format:
    #{state1: {transitionA: new state, transition b: newstate}, state2 : {...}}
    accepting = list()  #list of accepting states
    liststates = set()
    initial = ''
    alphabet = set()
    
    ###   READING TEXT FILE AND BUILDING NFA STRUCTRUE
    for i in fobj:
        line = i.strip().split()
        if line == "" or line == "\n" or line == "\t":
            continue
        elif (line[0].lower() == "initial"):
            initial = line[2]
            liststates.add(line[2])
        elif (line[0].lower() == "accepting" or line[0].lower() == "final"):
            accepting.append(line[2])
            liststates.add(line[2])
        else:
            line = tuple(i.strip().split(","))
            liststates.add(line[2])
            liststates.add(line[0])
            alphabet.add(line[1])
            if line[0] not in transitionfx:
                transitionfx[line[0]] = {line[1]: [line[2]]}
            elif line[1] not in transitionfx[line[0]]:
                transitionfx[line[0]][line[1]] = [line[2]]
            else:
                transitionfx[line[0]][line[1]].append(line[2])

    if initial == '':
        print("The initial state could not be found in text NFA")
        return
    elif len(accepting) == 0:
        print("No accepting states could  be found in the text NFA")
        return

    alphabet = list(alphabet)
    alphabet.sort()
    
    #SETTING UP THE FSA 
    fsa_trans = list() #list of tuples (state, transition dictionary)
    initialtrans = transitionfx[str(initial)]  
    fsa_trans.append((initial, transitionfx[str(initial)]))
    distributelist = list(transitionfx[str(initial)].values())
    if [initial] in distributelist:
        distributelist.remove([initial])

    #ALGORITHM FOR FSA TRANSITION     
    while True:
        if len(distributelist) != 0:
            goesto = distributelist.pop()
        else:
            break
        
        k = goesto
        if len(k) == 1: #A state that goes in FSA same form as in NFA
            if str(k[0]) in transitionfx:
                fsa_trans.append((k[0], transitionfx[str(k[0])]))
                
                nextdistribute = transitionfx[str(k[0])]
                for newstate in nextdistribute.values():
                    #This loop checks for what to add to "distribute list"
                    newbool = False
                    for states in fsa_trans:
                        if states[0] == newstate or [states[0]] == newstate:
                            newbool = True
                            break
                    if newbool == False:
                        for states in distributelist:
                            if states == newstate:
                                newbool = True
                                break
                    if newbool == False:
                        distributelist.append(newstate)
                        
                
            else:   #Here, it's a state that goes to {}
                null_add = dict()
                for letter in alphabet:
                    if letter not in (null_add):
                        null_add[letter] = "{}"
                fsa_trans.append((k[0],null_add))
                if "{}" not in fsa_trans:
                    newtup = dict()
                    for let in alphabet:
                        newtup[let] = "{}"
                    newtup = ("{}", newtup)
                    fsa_trans.append(newtup)
        else:  #Does NFA union algorithm on 2+ states
            mergetrans = dict() 
            x = []
            for item in goesto:
                x.append(item)
                
            for indiv in goesto:
                if indiv in transitionfx:
                    indiv_dict = transitionfx[indiv]
                    for indiv_item in indiv_dict.items():
                        if indiv_item[0] not in mergetrans:
                            mergetrans[indiv_item[0]] = copy.deepcopy(indiv_item[1])
                        else:
                            for second_item in indiv_item[1]:
                                if second_item not in mergetrans[indiv_item[0]]:
                                    mergetrans[indiv_item[0]].append(second_item)
            fsa_trans.append((x, mergetrans))

            for newstate in mergetrans.values():
                #this determines whether or not it's a new state and should
                #be added
                newbool = False
                for states in fsa_trans:
                    if states[0] == newstate or [states[0]] == newstate:
                        newbool = True
                        break
                if newbool == False:
                    for states in distributelist:
                        if states == newstate:
                            newbool = True
                            break
                if newbool == False:
                    distributelist.append(newstate)


    #PRINTING FSA STUFF
    fsa_accepting = list()
    print("ALPHABET:", alphabet)
    print("FSA TRANSITION:")
    nulltup = ''
    for fsa_state in fsa_trans:
        for component in fsa_state[0]:
            if component in accepting:
                fsa_accepting.append(fsa_state[0])
                break
        if set(fsa_state[1]) != set(alphabet):
            #ensures that if no transition found for state, it goes to {}
            for letter in alphabet:
                if letter not in set(fsa_state[1]):
                    fsa_state[1][letter] = "{}"
                    if "{}" not in fsa_trans:
                        nulltup = GenerateNull(fsa_trans, alphabet)
        print(fsa_state)
    if nulltup != '':
        fsa_trans.append(nulltup)
        print(nulltup)
                
    print("FSA ACCEPTING STATES: ", fsa_accepting)
    print("FSA initial: ", initial)


def GenerateNull(fsa_trans, alphabet):
    '''Used by NFAtoFSA
    Input is the fsa transition functon being built...list of tuples, where each
    tuple is the (statenum, {transition dictionary})
    And the alphabet
    Output is a tuple of straight nulls, so the statenum is {}
    and the transition dict goes to {} on each char in alphabet
    '''
    newtup = dict()
    for let in alphabet:
        newtup[let] = "{}"
    newtup = ("{}", newtup)
    return newtup


NFAtoFSA()
    
