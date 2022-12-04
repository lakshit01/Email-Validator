email = input("Enter your email: ") #l@l.in

k,j,m = 0,0,0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i==i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        m=1                     
                if k==1 or j==1 or m==1:
                    print('Wrong Email 5', j,k,m)
                else:
                    print('Right Email', j,k,m)
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email (You must have 1 @ in a email.)")
    else:
        print("Wrong Email (First letter of email can't be a number)")
else:
    print("Wrong Email (Email must have atleast 6 characters)")