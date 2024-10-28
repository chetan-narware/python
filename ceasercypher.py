alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.cypher)
number=[0,1,2,3,4,5,6,7,8,9]

def cypher(simple_text,shift,cypher_direction):
    string=""
    if cypher_direction=="decode":
        shift *=-1
    for letter in simple_text:
         if letter in alphabet:
                position=alphabet.index(letter)
                newpos=position+shift
                string=string+alphabet[newpos]
            
         else:
            string=string+letter
    print(f"message is {string}")

keepgoing=True

while keepgoing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    cypher(text,shift,direction)
    ask=input("Do You Want To Continue-yes/no:")
    if ask=='no':
        keepgoing=False

    
#def encode(simple_text,shift):
    #string=""
   #for letter in simple_text:
        # if letter !=' ':
           # position=alphabet.index(letter)
            #newpos=position+shift
            #string=string+alphabet[newpos]
        # else:
     #    #   string=string+letter
   # #print(f"encoded message is {string}")
#
#def decode(simple_text,shift):
   # string=""
    #for letter in simple_text:
        #if letter !=' ':
           # position=alphabet.index(letter)
          #  newpos=position-shift
           # string=string+alphabet[newpos]
       # else:
           # string=string+letter
   #print(f"decoded message is {string}")   
#if direction=="encode":
   # encode(text,shift)
#else:
    #decode(text,shift)






