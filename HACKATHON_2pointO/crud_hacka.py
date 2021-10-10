import json

print("""
1) Insert 
2) Update 
3) Delete
    """)
   
option = input("enter any option :-----")
if option == '1': 
    with open('crud.json','r') as l:
        re=json.load(l)
        contact=input('enter your contact :-----')
        list1 = []
        dict1={}
        dict2={}
        if list1 == re:
            user_name = input('enter the name :---')
            email = input("enter your email :--- ")

            dict1['user name'] = user_name
            dict1['email'] = email
            dict2[contact] = dict1
            re.append(dict2)
            print("successfuly insert your detail !!!")
                
            with open('crud.json','w+') as k:
                json.dump(re,k,indent=4)
        else:
            for j in re:
                if contact in j:
                    print('this account already exist')
                    break
                else:
                    user_name = input('enter the name :---')
                    email = input("enter your email :--- ")

                    dict1['user name'] = user_name
                    dict1['email'] = email
                    dict2[contact] = dict1
                    re.append(dict2)
                    print('successfuly insert your detail !!!')
                    with open('crud.json','w+') as k:
                        json.dump(re,k,indent=4)
                    break
elif option == '2':
    contact=input('enter the contact:---')
    with open('crud.json','r') as l:
        re=json.load(l)
        for j in re:
            if contact in j:
                for y in j.values():
                    store = y
                    new_user = input("Enter your new user :- ")
                    new_email = input("Enter your new email :- ")
                    store["user name"]=new_user
                    store["email"]=new_email
                    print('successfuly update your detail !!!')
                    break
        
    with open ("crud.json","w") as m:
        json.dump(re,m,indent=4)
else:
    contact=input('enter the contact:---')
    with open('crud.json','r') as l:
        re=json.load(l) 
        for j in re:
            if contact in j:
                ml=j
                re.remove(ml)
                print('seccessfuly delete your account !!!')
                break
    with open('crud.json','w') as n:
        json.dump(re,n,indent=4)