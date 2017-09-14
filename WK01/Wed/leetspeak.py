# #4 Leetspeak

speak = "Given a paragraph of text as a string, print the paragraph in leetspeak.".upper()
#[A,E,G,I,O,S,T]=[4,3,6,1,0,5,7]
for i in range(len(speak)):
    if speak[i] == "A":
        speak = speak.replace("A","4")
    elif speak[i] == "E":
        speak = speak.replace("E", "3")
    elif speak[i] == "G":
        speak = speak.replace("G", "6")
    elif speak[i] == "I":
        speak = speak.replace("I", "1")
    elif speak[i] == "O":
        speak = speak.replace("O", "0")
    elif speak[i] == "S":
        speak = speak.replace("S", "5")
    elif speak[i] == "T":
        speak = speak.replace("T", "7")
print(speak)
