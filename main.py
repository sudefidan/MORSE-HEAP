from heap import *
from morse_server import *

if __name__ == "__main__":
    morse = MorseHeap()
    """
    #task1 - decode E.g ... ..- -.. . ==> sude 
    print('--------MORSE TO TEXT-------------')
    morse_message = input(('Enter morse to decode ==> ')) 
    print('Decoded message: ', morse.decode_bt(morse_message))
     """
    #task2 - ham radio conversations
    #encoding
    print('--------ENCODING HAM CONVERSATIONS-------------')
    sender  = input('Enter sender ==> ') #S1
    receiver = input('Enter receiver ==> ') #R1
    message = input('Enter message ==> ') #HI
    print('Encoded ham conversation: ', MorseHeap.encode_ham(sender,receiver,message))
   
    #print: .-. .---- -.. . ... .---- -...- .... .. -...- -.--.
    #decoding
    """
    print('--------DECODING HAM CONVERSATIONS-------------')
    ham_convo = input(('Enter ham conversation to decode ==> '))
    print(morse.decode_ham(ham_convo))
    #print: RECEIVER: R1 / SENDER: S1 / MESSAGE: HI

    #task3 - morse server
    print("Echo client")
    asyncio.run(main())
    sender = input(('Hey sender, enter your name ==> '))
    message = input(('Hey sender, enter your message ==> '))
    print('--------SERVER:ECHO-------------')
    #changeECHO SERVER RESPONSE: SUDEECHO=HI=( ==>  ... ..- -.. . . -.-. .... --- -...- .... .. -...- -.--.
    print(f'Server response: ', asyncio.run(send_echo(sender,message))) #
    print('--------SERVER:TIME-------------')
    print('Server response: ', asyncio.run(send_time(sender)))"""