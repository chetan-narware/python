plain_text=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key_list=['u', 'd', 'x', 'n', 'y', 'g', 't', 'v', 'c', 'w', 'l', 'f', 'a', 'z', 'r', 'o', 'k', 'e', 'j', 'b', 's', 'q', 'm', 'h', 'p', 'i']

def encription():
    message=input("Hello There! please enter the message You want to encript: ")
    enc_str=" "
    for x in message:
        if x!=' ':
            i=ord(x)-ord('a')
            enc_str+=key_list[i]
        else:
            enc_str+=' '
    print(enc_str)


def decription():
    message=input("Hello There! please enter the message You want to decript: ")
    enc_str=" "
    for x in message:
        if x!=' ':
            i=key_list.index(x)
            enc_str+=plain_text[i]
        else:
            enc_str+=' '
    print(enc_str)

encription()
decription()