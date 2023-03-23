from morse import MorseTree
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
        
    #TASK1

    #converts morse to text
    #E.g Input: .-- . / .-.. --- ...- . / .--. -.-. / -.-.-- ==> Output: WE LOVE PC !
    def decode_bt(self, code):
        decoded = ""
        value = 1 #first position in the heap, ignore start
        for word in code.split("/"):#each word 
            for letter in word.split():#each letter 
                for c in letter:
                    if c == ".": #left child
                        value = 2*value 
                    elif c == "-": #right child
                        value = 2*value + 1
                decoded += self.heap[value-1] #add each letter from heap index
                value = 1 #reset value for next lopp
            decoded += " " #add each word to text
        return decoded.strip()

   
    #TASK2
    def encode_ham(self, receiver,sender,message):
        # method to encode message for ham radio. Uses Node() from morse.py
        # returns String
        conversation = sender + "de" + receiver + "=" + message + "=("
        print(conversation)
        morse= MorseTree
        print(morse.encode(conversation))
        print(MorseTree.encode(conversation))

        return MorseTree.encode(sender + "de" + receiver + "=" + message + "=(")

    
    
    def decode_ham(self,code):
        decoded=self.decode_bt(code)
        #word before 'de' is receiver
        receiver = decoded[:decoded.rfind('DE')]
        #sender is between 'de' and first '='
        sender= decoded[decoded.find('DE')+len('DE'):decoded.rfind('=')].split('=')[0]
        #message is between "="
        transmit = decoded[decoded.find('=')+len('='):decoded.rfind('=(')]
        return f'RECEIVER: ' + receiver + f'\nSENDER: ' + sender + f'\nMESSAGE: ' + transmit 

morse = MorseHeap()
print(morse.encode_ham('r1','s1','hi'))