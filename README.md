# **WORKSHEET2 - MORSE HEAP**

## 🚀 **Getting Started**

This repository contains python module that creates a binary heap for morse code. By using that module you can do translation between morse code and sentence. Binary Heap uses binary tree to accomplish some features [[Morse Tree](https://gitlab.uwe.ac.uk/s2-fidan/worksheet2part1.git)].

![morse tree](images/morsetree.jpg)

## 🖥️ **How to Run**
0. Ensure you have [python3](https://www.python.org/download/releases/3.0/) installed.
   
   At a command prompt, type `python --version` to ensure you have version 3.
1. Download or clone this repository.
   
   If you download as a zip file, be sure to unzip it.
2. To decode morse code with using binary heap, run main.py
3. To decode and encode ham conversations, run main.py
4. To use echo and time services through WebSocket, run main.py.
5. To do unit testing, run morseunit.py

## 🔧 **Implementations**
**Morse Heap Implementation :** *Tree is implemented with decode_bt(), encode_ham(), decode_ham() functions.*

**Morse Server Implementation :**  Server has two services including echo and time.

**Unit Test Implementation:** *Test are done using assertIn(), assertNotIn(), assertEqual(), assertNotEqual(), assertCountEqual(), assertIsNotNone()*
## 🎯 **Features**
* Translation from morse code to text (decoding)
* Ham conversation from text to morse code(encoding).
* Ham conversation from morse to text code(decoding).
* Echo server service(return echo).
* Time server service(return time).
* Unit testing.

## 🖇️ **Example Usage**

📍 Main.py

User can translate from text to morse and morse to text:
```python
#messages
print('--------MORSE TO TEXT-------------')
morse_message = input(('Enter morse to decode ==> ')) 
print('Decoded message: ', morse.decode_bt(morse_message))
```
Expected Output:

![decode_bt](images/decode_bt.jpg)

Here is some other examples with their expected output to try:
Text  | Morse
------------- | -------------
Sude Fidan  | ... ..- -.. . / ..-. .. -.. .- -.
2023 + 2017 | ..--- ----- ..--- ...-- / .-.-. / ..--- ----- .---- --..
WE LOVE PC ! | .-- . / .-.. --- ...- . / .--. -.-. / -.-.--


User can also have encoded and decoded ham radio conversation:
```python
print('--------ENCODING HAM CONVERSATIONS-------------')
sender  = input('Enter sender ==> ') #S1
receiver = input('Enter receiver ==> ') #R1
message = input('Enter message ==> ') #HI
print('Encoded ham conversation: ', MorseHeap.encode_ham(sender,receiver message))
print('--------DECODING HAM CONVERSATIONS-------------')
ham_convo = input(('Enter ham conversation to decode ==> '))
print(morse.decode_ham(ham_convo))
```
Expected Output:

![printing morse tree](images/print_tree_terminal.jpg)


## 💡 **Unit Testing**
📍 Morseunit.py

Program has some unit testing if user wants to test. There are 7 tests available:

1. Testing for encode() function

    Encode function translate from text to morse. Here are the examples that are done under testing:
    Assert Function | Message         | Encoded Version     | Message 2   | Comparison| Pass/Fail
    -------------   | ------------- | ------------- | ------------- | ------------- | -------------
    assertIn() | here | .... . .-. . | .. / .- -- / .... . .-. . | True |Pass
    assertEqual() | Sude Fidan | ... ..- -.. . / ..-. .. -.. .- -. |... ..- -.. . / ..-. .. -.. .- -.| True|Pass
    assertCountEqual() | 2023 | ..--- ----- ..--- ...-- | ..--- ----- ..--- ...-- | True|Pass
    assertEqual() | 2023 + 2017 | ..--- ----- ..--- ...-- / .-.-. / ..--- ----- .---- --... | ..--- ----- ..--- ...-- / .-.-. / ..--- ----- .---- --... | True|Pass
    assertEqual()| FIDAN | ..-. .. -.. .- -. | ..-. .. -.. .- -.| True|Pass
    assertEqual()| WE LOVE PC ! | .-- . / .-.. --- ...- . / .--. -.-. / -.-.-- | .-- . / .-.. --- ...- . / .--. -.-. / -.-.--| True|Pass
    assertNotIn() | benedict |-... . -. . -.. .. -.-. - | -... . -. . -.. | False|Pass
    assertNotEqual() | internet of the things | .. -. - . .-. -. . - / --- ..-. / - .... . / - .... .. -. --. ... | .. -. - . .-. -. . - / --- ..-. / - .... . / - .... .. -. --. | False|Pass

2. Testing for decode() function

    Decode function translate from morse to text. Here are the examples that are done under testing:

    Assert Function | Message         | Decoded Version     | Message 2   | Comparison | Pass/Fail
    -------------   | ------------- | ------------- | ------------- | ------------- | ------------- 
    assertIn() | ... ..-. | SF| SF IS MY CAPITALS | True |Pass
    assertEqual()| ...- ... -.-. --- -.. . | VSCODE |VSCODE|True|Pass
    assertCountEqual() |- .... . / . -. -.. | THE END | THE END| True|Pass
    assertEqual() | ..--- ----- ..--- ...-- / -....- / ..--- ----- ..--- ....- | 2023 - 2024 | 2023 - 2024| True|Pass
    assertNotEqual() | .. -. - . .-. -. | INTERN | INTERNET| False|Pass
    assertNotIn() | - .... .. -. --. . | THINGE | I WAS BORN IN 2002 |False|Pass


3. Testing for is_empty() function:
   
    Is_Empty function returns True if tree is empty. Our morse code tree is already populated under constructor so it is not empty so function will return False.

    Assert Function | Function | True/False | Pass/Fail
    -------------   | ------------- | -------------  | -------------  
    assertFalse() | tree.is_empty() | True |Pass

4. Testing for is_not_empty() function:

    Is_Not_Empty function returns True if tree is not empty. Our morse code tree is already populated under constructor so it is not empty so function will return True.

    Assert Function | Function | True/False| Pass/Fail
    -------------   | ------------- | -------------  | -------------
    assertTrue() | tree.is_not_empty() | True |Pass

5. Testing for find() function:

    Find function finds the character from morse code inside of morse dictionary.

    Assert Function | Char | Decoded Version | Location | True/False| Pass/Fail
    -------------   | ------------- | -------------  | ------------- | -------------| -------------
    assertIn() | .- | A | *morse.dictionary* | True |Pass
    assertIn() | ...| S | SUDE| True |Pass

1. Testing for insert() function:

    Insert function inserts new character to tree with its node and to dictionary.

    Assert Function | Symbol | Morse | Is Inserted ?| True/False| Pass/Fail
    -------------   | ------------- | -------------  | ------------- | ------------- | -------------
    assertNotIn() | @ | .--.-. |No | True |Pass
    assertIn() | @| .--.-.| Yes | True|Pass
    assertNotIn() | *Not Valid* | .........| No | False |Pass

7. Testing for additional symbols:

    Symbol | Morse | Symbol | Morse | Symbol | Morse 
    -------------   | ------------- | -------------   | -------------   | ------------- | -------------   
    . | .-.-.- | ( |-.--. | , | .-.-.- | ) | -.--.-
    ! | -.-.-- | ¡ | --...- | -|-....- | _ |..--.-
    +| .-.-. | ? | ..--.. | ¿ | ..-.- | & | .-...
    ’ |  .----. | :| ---... |  ;| -.-.-. | ”| .-..-.
    $ |...-..-

    Above additional symbols are added to morse dictionary and tree.

    Assert Function | Message         | Translation     | Message 2   | Comparison| Pass/Fail
    -------------   | ------------- | ------------- | ------------- | ------------- | ------------- 
    assertEqual() | .-.-.- | . | . | True|Pass
    assertEqual() | ..--.- | _ | _ | True|Pass
    assertIs() | -....- | - | - | True |Pass
    assertIs() | --...- | ¡ | ¡| True|Pass
    assertEqual() | ..--.. -.-.-- | ?! | ?!| True|Pass
    assertEqual() | -.--. / -.--.- | ( ) | ( )| True|Pass
    assertIn() | ...-..- | $| $€£ | True|Pass
    assertIn() | .----.| ’| ’| True|Pass
    assertIn() | ---...| : | *morse.dictionary* | True|Pass
    assertIn() | + | .-.-. | *morse.dictionary* | True|Pass
    assertCountEqual() | & | .-... | .-... | True|Pass
    assertCountEqual() | - | -....- | -....- | True|Pass
    assertNotIn() | ¿¿¿ | ..-.- ..-.- ..-.- | *morse.dictionary* | False|Pass
    assertNotEqual() | -.-.-. | ;| A | False|Pass
    assertNotEqual() | -.-.-. | *Not Valid* | ” | False|Pass
    assertIsNot() | , | --..-- | ..--.- | False|Pass



After running all tests expected output:

![printing unit testing](images/unit_testing_terminal.jpg)

## 📚 **Library** 
Here is the library for unit testing: [unittest](https://docs.python.org/3/library/unittest.html)
## 📪 **Installation** 
User does not need to install any packages.

## 🤓 **Maintainers** 
Sude Fidan(@s2-fidan)
## 📖  **Referencing** 
* https://morsecode.world/international/translator.html
* https://www.geeksforgeeks.org/morse-code-translator-python/
* https://favtutor.com/blogs/heap-in-python
* https://en.wikipedia.org/wiki/Binary_heap

