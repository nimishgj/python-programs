import json
data={
 "users":[
       {
           "name":"nimi",
           "age":""

       },
       {
           "name":"shgj"
       }
   ]
}

def inputing():
    #_name=input("Enter the name:-")
    #_age=int(input("Enter the age:-"))
    #_mobno=input("Enter the mobile number:-")
    #_email=input("Enter the email:-")
    #_dob=input("Enter the date of birth:-")
    a={
        "name":1,
        "age":1,
        "mobno":1,
        "email":1,
        "dob":21
    }
    with open('dat.json','w') as f:
        dt=json.dumps(data)
        json.dump(dt,f)
        print(type(dt))

    with open('dat.json','r') as f:  
        nd=json.loads(json.load(f))  
        for d in nd['users']:
            print(d['name'])

inputing()        