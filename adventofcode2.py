list=("1-3 a: abcde",
"1-3 b: cdefg",
"2-9 c: ccccccccc")

# list=open("input (1).txt","r").read().split("\n")[:-1]
try:
    list=open("C:\\Users\\mika1\\OneDrive\\Documents\\AdventOfCode\\input2.txt","r").readlines()
except:
    print("File not found")

def valid_passwords(list):
    valid=0
    for i in list:
        policy,pwd=i.split(": ")
        minimaxi,char=policy.split(" ")
        mini,maxi=minimaxi.split("-")
        count=0
        for letter in pwd:
            if(letter==char):
                count+=1
        if(count<=int(maxi) and count>=int(mini)):
            valid+=1
    return valid

print("Number of valid passwords in the provided list:",valid_passwords(list))

def valid_passwords2(list):
    valid=0
    for i in list:
        policy,pwd=i.split(": ")
        minimaxi,char=policy.split(" ")
        mini,maxi=minimaxi.split("-")
        count=0
        if(int(mini)<=len(pwd)):
            if(pwd[int(mini)-1]==char):
                count+=1
        if(int(maxi)<=len(pwd)):
            if(pwd[int(maxi)-1]==char):
                count+=1
        if(count==1):
            valid+=1
    return valid

print("Number of valid passwords in the provided list:",valid_passwords2(list))
