a=input("enter the word\t")

if a[-3:]=='ing':
    print(a+'ly')
elif a[-3:]!='ing':
    print(a+'ing')
