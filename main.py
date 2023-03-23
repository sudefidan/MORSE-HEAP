from heap import MorseHeap

if __name__ == "__main__":
    morse = MorseHeap()

    #task1 - decode
    print('--------MORSE TO TEXT-------------')
    #morse_message = input(('Enter morse to decode ==> '))
    #decoded = morse.decode_bt(morse_message)
    #print('Decoded message: ' + decoded)

    #task2 - ham radio conversations
    receiver = input('Enter receiver ==> ') #r1
    sender  = input('Enter sender ==> ') #s1
    message = input('Enter message ==> ') #hi

    encode='hi'
    decode_message = ".-. .---- -.. . ... .---- -...- .... .. -...- -.--."
    print(morse.encode_ham(receiver,sender,message))
    print(morse.decode_ham(decode_message))