#SUDE FIDAN - 21068639

import unittest
from heap import *
from morse_server import *


class TestMorse(unittest.TestCase):
    #test1 - decode_bt
    def test_decode_bt(self):
        self.assertIn(heap.decode_bt('... ..-.'), 'SF IS MY CAPITALS') #true ==>   SF: ... ..-.
        self.assertEqual( heap.decode_bt('...- ... -.-. --- -.. .'), 'VSCODE') #true
        self.assertCountEqual('THE END',heap.decode_bt('- .... . / . -. -..')) #true
        self.assertEqual( heap.decode_bt('..--- ----- ..--- ...-- / -....- / ..--- ----- ..--- ....-'), '2023 - 2024') #true
        self.assertNotEqual( heap.decode_bt('.. -. - . .-. -.'), 'INTERNET') #false ==>  INTERNET: .. -. - . .-. -. . -
        self.assertNotIn( heap.decode_bt('- .... .. -. --. .'), 'I WAS BORN IN 2002') #false ==>  - .... .. -. --. . ==> thinge    

    #test2 - encode ham conversations
    def test_encode_ham(self):
        self.assertIn( heap.encode_ham('send','receive','here'), '.... .. -.. -.. . -. / .... .- -- / .. ... / .-. . -.-. . .. ...- . -.. . ... . -. -.. -...- .... . .-. . -...- -.--.') #true ==> RECEIVEDESEND=HERE=(
        self.assertEqual( heap.encode_ham('Sude Fidan', 'SF','secret'), '... ..-. -.. . ... ..- -.. . / ..-. .. -.. .- -. -...- ... . -.-. .-. . - -...- -.--.') #true ==> SFDESUDE FIDAN=SECRET=(
        self.assertCountEqual( '..--- ----- -.. . ..--- ...-- -...- ..--- ----- ..--- ...-- -...- -.--.', heap.encode_ham('23','20','2023')) #true ==> 20DE23=2023=(
        self.assertEqual(heap.encode_ham('23','20','20+17'), '..--- ----- -.. . ..--- ...-- -...- ..--- ----- .-.-. .---- --... -...- -.--.') #true ==> 20DE23=20+17=(
        self.assertEqual(heap.encode_ham('SEND','RECEIVE','WE LOVE PC !'), '.-. . -.-. . .. ...- . -.. . ... . -. -.. -...- .-- . / .-.. --- ...- . / .--. -.-. / -.-.-- -...- -.--.') #true ==> RECEIVEDESEND=WE LOVE PC !=(
        self.assertNotIn( heap.encode_ham('benedict','sude','iot'), '... ..- -.. . -.. . -... . -. . -.. .. -.-. - -...- .. --- - .-- --- .-. -.- ... .... . . - ..--- -...- -.--.') #false ==> Message: iotworksheet2 not iot
        self.assertNotEqual( heap.encode_ham('internet','of','things'), '--- ..-. -.. . .. -. - . .-. -. . - -...- .-.. .- ... - / .-- --- .-. -.. -...- -.--.') #false ==> Message:LAST WORD not things
    
    #test3 - decode ham conversations
    def test_decode_ham(self):
        self.assertIn('R', heap.decode_ham('.-. -.. . ... -...- .... .. -...- -.--.')) #true - RDES=HI=(
        self.assertEqual(heap.decode_ham('.---- ..--- -.. . ...-- ....- -...- .... .. -...- -.--.'), 'RECEIVER: ' + '12' + '\nSENDER: ' + '34' + '\nMESSAGE: ' + 'HI') #true ==> 12DE34=HI=(
        self.assertCountEqual('RECEIVER: ' + '+' + '\nSENDER: ' + '-' + '\nMESSAGE: ' + 'HI',heap.decode_ham('.-.-. -.. . -....- -...- .... .. -...- -.--.')) #true ==> +DE-=HI=(
        self.assertEqual( heap.decode_ham('..--- .-.-.- ..... -.. . ...-- .-.-.- ..... -...- -- ... --. -...- -.--.'), 'RECEIVER: ' + '2.5' + '\nSENDER: ' + '3.5' + '\nMESSAGE: ' + 'MSG') #true ==> 2.5DE3.5=MSG=(
        self.assertNotEqual( heap.decode_ham('-... . -. -.. . .. -. - . .-. -. . - -...- -- ... --. -...- -.--.'), 'RECEIVER: ' + 'BEN' + '\nSENDER: ' + 'INTERNET' + '\nMESSAGE: ' + 'BENEDICT') #false ==> Message: MSG not BENEDICT
        self.assertNotIn( 'I WAS BORN IN 2002', heap.decode_ham('.-. .---- -.. . ... .---- -...- .. / .-- .- ... / -... --- .-. -. / .. -. / ..--- ----- ..--- ...-- -...- -.--.')) #false ==> Message: 2002 not 2023

    #test4 - echo server
    def test_echo(self):
        self.assertIn(asyncio.run(send_echo('a','message')),('.- -.. . . -.-. .... --- -...- -- . ... ... .- --. . -...- -.--.')) #true  ==> ADEECHO=MESSAGE=(
        self.assertEqual(asyncio.run(send_echo('a1','message')), '.- .---- -.. . . -.-. .... --- -...- -- . ... ... .- --. . -...- -.--.') #true ==> A1DEECHO=MESSAGE=(
        self.assertCountEqual('.- .---- -... .---- -.. . . -.-. .... --- -...- .. ... -- . ... ... .- --. . - --- --- .-.. --- -. --. ..--.. -...- -.--.',asyncio.run(send_echo('a1 b1','is message too long?'))) #true ==> A1B1DEECHO=ISMESSAGETOOLONG?=(
        self.assertNotEqual( asyncio.run(send_echo('benedict','here is my message')), '-... . -. . -.. .. -.-. - -.. . . -.-. .... --- -...- - .... .. ... / .. ... / -. --- - / -- -.-- / -- . ... ... .- --. . -...- -.--.') #false ==> Message: HEREISMYMESSAGE not THIS IS NOT MY MESSAGE
        self.assertNotIn( '.. --- - -.. . . -.-. .... --- -...- ... . -.-. .-. . - -.-.-- -...- -.--.', asyncio.run(send_echo('iot','secret123'))) #false ==> Message: secret123 not secret!

    #test5 - time server
    def test_time(self):
        self.assertIn('-.. .',asyncio.run(send_time('10+10'))) #true  -.. .==> de
        self.assertIn('- .. -- .',asyncio.run(send_time('sender'))) #true  - .. -- .==> time
        self.assertNotEqual( asyncio.run(send_time('benedict 2023')), '-... . -. . -.. .. -.-. - ..--- ----- ..--- ...-- -.. . - .. -- . -...- .---- ....- ---... ....- --... ---... ...-- --... -...- -.--.') #false ==> server time changes
        self.assertIsNotNone(asyncio.run(send_time('2020+2023')))




if __name__ == '__main__':
    print('\n\n\n----------------------------- UNIT TESTING ---------------------------\n')
    heap = MorseHeap()
    unittest.main()