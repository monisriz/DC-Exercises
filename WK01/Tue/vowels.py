# #5 Long-long vowels

speak = "leetspeak"

for i in range(len(speak)-1):
    if speak[i] == speak[i+1]:
        print(speak[i])
