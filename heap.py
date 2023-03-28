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
    #encoding ham conversations
    #E.g. Innput: receiver('r1'),sender('s1'),message('hi') ==> Output: .-. .---- -.. . ... .---- -...- .... .. -...- -.--.
    @staticmethod
    def encode_ham(sender:str, receiver:str,message:str) -> str:
        #Uses binary tree from morse.py for encoding
        morse= MorseTree()
        encoded = {  
            'message': morse.encode(str(receiver) + "de" + str(sender) + "=" + str(message) + "=(" )
        }
        return encoded['message']

    
    #decoding ham conversations
    #E.g. Input: .-. .---- -.. . ... .---- -...- .... .. -...- -.--. ==> Output: RECEIVER:R1 SENDER:S1 MESSAGE:HI
    def decode_ham(self,code):
        decoded=self.decode_bt(code)
        #word before 'de' is receiver
        receiver = decoded[:decoded.rfind('DE')]
        #sender is between 'de' and first '='
        sender= decoded[decoded.find('DE')+len('DE'):decoded.rfind('=')].split('=')[0]
        #message is between "="
        transmit = decoded[decoded.find('=')+len('='):decoded.rfind('=(')]
        return f'RECEIVER: ' + receiver + f'\nSENDER: ' + sender + f'\nMESSAGE: ' + transmit
    
    






