s=input()
c1=0 
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
c10=0
for i in s:
    if i == 'a':
        c1+=1 
    if i == 'e':
        c2+=1
    if i == 'i':
        c3+=1
    if i == 'o':
        c4+=1  
        
    if i == 'u':
        c5+=1    
        
    if i == 'A':
        c6+=1    
        
    if i == 'E':
        c7+=1    
        
    if i == 'I':
        c8+=1
        
    if i == 'O':
        c9+=1    
    if i=='U':
        c10+=1
st=""
for j in range(len(s)):
    if s[j] not in st:
        for k in range(j+1,len(s)):
            if s[j]==s[k]:
                st+=s[j]
                break
        else:
            st+=s[j]
        
for i in st:
    if i == 'a':
        print("a :",c1) 
    if i == 'e':
        print("e :",c2)
    if i == 'i':
        print("i :",c3)
    if i == 'o':
        print("o :",c4)
        
    if i == 'u':
        print("u :",c5)
        
    if i == 'A':
        print("A :",c6)
        
    if i == 'E':
        print("E :",c7)
        
    if i == 'I':
        print("I :",c8)
        
    if i == 'O':
        print("O :",c9)
    if i=='U':
        print("U :",c10)
        
