#SUDE FIDAN - 21068639

import unittest
from heap import MorseHeap


class TestMorse(unittest.TestCase):
    #test1
    def test_decode_bt(self):
        self.assertIn(heap.decode_bt('... ..-.'), 'SF IS MY CAPITALS') #true -  SF: ... ..-.
        self.assertEqual( heap.decode_bt('...- ... -.-. --- -.. .'), 'VSCODE') #true
        self.assertCountEqual('THE END',heap.decode_bt('- .... . / . -. -..')) #true
        self.assertEqual( heap.decode_bt('..--- ----- ..--- ...-- / -....- / ..--- ----- ..--- ....-'), '2023 - 2024') #true
        self.assertNotEqual( heap.decode_bt('.. -. - . .-. -.'), 'INTERNET') #false - INTERNET: .. -. - . .-. -. . -
        self.assertNotIn( heap.decode_bt('- .... .. -. --. .'), 'I WAS BORN IN 2002') #false - - .... .. -. --. . ==> thinge    

    #test2
    def test_encode_ham(self):
        print('a')
    
    #test3
    def test_decode_ham(self):
        print('a')
    
    #test4-server



if __name__ == '__main__':
    print('\n\n\n----------------------------- UNIT TESTING ---------------------------\n')
    heap = MorseHeap()
    unittest.main()