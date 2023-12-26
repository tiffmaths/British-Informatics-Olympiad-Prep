import string
#part A 
alphatonum = {char:count+1 for count, char in enumerate(string.ascii_uppercase)}
numtoalpha = {v:k for k, v in alphatonum.items()}

def decrypt(dstring):
    e = list(dstring.upper())
    l = []
    for i in range(0,len(e)):
        n = alphatonum[e[i]] - alphatonum[e[i-1]]
        if i == 0: 
            l.append(e[i])
        else:
            if alphatonum[e[i-1]] < alphatonum[e[i]]: 
                l.append(numtoalpha[n])
            else:
                l.append(numtoalpha[26+n])
    
    decrypted = ''.join(l)
    return decrypted

todecrypt = input("Please enter a string between 1 to 10 uppercase letters NO SPACES...")
decrypt(todecrypt)

#five letter string: ZZZZZ
# times needed for olympiad to return to itself (104)

#Part C 
def findit(str): 
    count = 1
    n = decrypt(str)
    while n!=str:
        count+=1
        n = decrypt(n)
    return count 

print(findit('OLYMPIAD'))


