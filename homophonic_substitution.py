import string
import random
homophonic_dict={
    'a': ['01', '02', '03', '04', '05'],
    'b': ['06', '07'],
    'c': ['08', '09'],
    'd': ['10', '11', '12'],
    'e': ['13', '14', '15', '16', '17', '18'],
    'f': ['19', '20'],
    'g': ['21', '22'],
    'h': ['23', '24', '25'],
    'i': ['26', '27', '28', '29'],
    'j': ['30'],
    'k': ['31'],
    'l': ['32', '33', '34'],
    'm': ['35', '36'],
    'n': ['37', '38', '39', '40'],
    'o': ['41', '42', '43'],
    'p': ['44', '45'],
    'q': ['46'],
    'r': ['47', '48', '49'],
    's': ['50', '51', '52', '53'],
    't': ['54', '55', '56', '57'],
    'u': ['58', '59'],
    'v': ['60'],
    'w': ['61', '62'],
    'x': ['63'],
    'y': ['64', '65'],
    'z': ['66']
}


plain_dictionary={}
for x in string.ascii_lowercase:
    for q in homophonic_dict[x]:
        plain_dictionary[q]=x

def encription():
    message=input("Hello There! please enter the message You want to encript: ")
    enc_str=" "
    for x in message:
        if x!=' ':
            l=homophonic_dict[x]
            i=random.randint(0,len(l)-1)
            enc_str+=l[i]
    print(enc_str)

def decription():
    message=input("Hello There! please enter the message You want to encript: ")
    temp=message
    dstr=" "
    i = 0
    while i < len(message):
        if message[i] == ' ':
            dstr += " "
            i += 1
        else:
            e = message[i:i+2]
            dstr += plain_dictionary[e]
            i += 2
    print("Decrypted message:", dstr)



encription()
decription()