
class MorseHeap:
    def __init__(self):
        self.populate()

    def populate(self):
        self.heap = ['start', 
                    'E', 'T', 
                    'I', 'A', 'N', 'M',
                    'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O',
                    'H', 'V', 'F', '', 'L', '', 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', '', '',
                    '5','4','','3','','¿','','2','&','','+','','','','','1','6','=','/','','','','(','','7','','','','8','','9','0',
                    '','','','','','','','','','','','','?','_','','','','','”','','','.','','','','','','','','','’','','','-','','','','','','','','',';','!','',')','','','','¡','',',','','','','',':','','','','','','','',
                    '','','','','','','','','','$'] 
        

    '''def decode_bt(self,code):
        decoded = ""
        index = 0
        #split the words: / means space between words in morsecode
        for word in code.split("/"):
            for letter in word.split():
                for c in letter:
                    #dot means left child, dash means right child
                    if c == ".":
                        index = (index * 2) + 1
                        print(index)
                    elif c == "-":
                        index = (index * 2) + 2
            decoded += self.heap[index]
            decoded += " "
        
        return decoded #Displaying the message'''
    
    def decode_bt(self,morseCode):
        message = "" # Here we start off with an empty string as our output.
        value = 1 # We set the value to 1 as the first position in the string.
        i = 0

        while i in range(len(morseCode)): # Looping over morse code.
            if i < (len(morseCode) - 1): # Forloops start with 0 so we need to - 1 to length.
                if morseCode[i] == "." : # First check
                    value = 2*value # Update variable of value to go down the 'left tree'.
                elif morseCode[i] == "-": # Second check
                    value = 2*value + 1 # Update variable of value to go down the 'right tree'.
                elif morseCode[i] == "/": # Third check defines a space
                    message += " "
                elif morseCode[i] == " ":
                    message += self.heap[value - 1]
                    value = 1
            else: # closes loop on last morse.
                if morseCode[i] == ".": 
                    value = 2*value 
                elif morseCode[i] == "-": 
                    value = 2*value + 1
                message += self.heap[value - 1] # Add character with the string index to our message.
                value = 1 # Reset the value to 1 for next loop.
            i += 1
        return message




morse = MorseHeap()
morseCode = "- .... .. ... / .. ... / .- / - . ... -" #THIS IS A TEST

print(morse.decode_bt(morseCode))




"""
def decode_bt(message):

    message = message.split(' ') #Splits the morse code word into morse code
    decoded = "" #String to hold decoded message
    number = 0 #Used for decoding 

    for char in message: #Every character in morse 
        if char == '/':
            decoded += ' ' #To add space to decoded message 
        else:
            for sym in char:
                if sym == '.': #Dot
                    number = (number * 2) + 1
                elif sym == '-': #Dash
                    number = (number * 2) + 2
        
    decoded += self.heap[number] #Giving the message

    return decoded #Displaying the message

#Task 2
def encode_ham(sender, receiver, message):
    
    hamencode = str(receiver) + "DE" + str(sender) + "=" + str(message) + "=(" #Creates the contents of message in a decoded form

    message_encode = encode(hamencode) #Places it within an encode funtion which is from worksheet2 part1

    return message_encode #Displays the message

def decode_ham(message):

    rawdata = decode_bt(message) #Decodes entire inputted message
    rawdatasplit = rawdata.split("=") #Split the =
    
    receiver = rawdatasplit[0].split("DE") #Splits string for the receiver
    sender = receiver[1] #The sender
    receipient = receiver[0] #The receiver
    data = rawdata.split[1] #conetnts of data

    return sender, receipient, data # #Displays the message

#prints the whole tree structure
    def print_tree(self, node=None, prefix=''):
        if not node:
            node = self.root
        if node.value:
            #arrange the print
            print( prefix[:-2].replace('r',' ').replace('l', ' ')+ prefix[-2:] + node.value)
        if node.left:
            #l means left child of the root
            self.print_tree(node.left, prefix + 'l ')
        if node.right:
            #r means right child of the root
            self.print_tree(node.right, prefix + 'r ')"""