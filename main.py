from heap import MorseHeap

if __name__ == "__main__":
    morse = MorseHeap()

    #task1 - decode
    print('--------MORSE TO TEXT-------------')
    morse_message = input(('Enter morse to decode ==> '))
    print('Decoded message: ', morse.decode_bt(morse_message))

    #task2 - ham radio conversations
    #encoding
    print('--------ENCODING HAM CONVERSATIONS-------------')
    receiver = input('Enter receiver ==> ') #r1
    sender  = input('Enter sender ==> ') #s1
    message = input('Enter message ==> ') #hi
    print('Encoded ham conversation: ', MorseHeap.encode_ham(sender,receiver,message))
    #decoding
    print('--------DECODING HAM CONVERSATIONS-------------')
    ham_convo = input(('Enter ham conversation to decode ==> '))
    print(morse.decode_ham(ham_convo))