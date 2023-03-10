
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
            self.print_tree(node.right, prefix + 'r ')