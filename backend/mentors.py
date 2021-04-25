DIRECTORY = {}
#be able to sort it by field? 
#search by location?

def addMentor():
    while True:
        name = input("Name: ")
        field = input("Field: ")
        linkedin = input("Linkedin ID: ") 
        location = input("Country: ")
        if(name.strip() and field.strip() and linkedin.strip()  and location.strip() and linkedin.strip() not in DIRECTORY):
            #first entry name, second entry field
            DIRECTORY[linkedin] = [name, field, location]    
            #put mentor into the dictionary
            return
        else:
            print("Your entries {name}, {field}, {linkedin} are invalid. Please try again. ")
       
    

def searchField(field: str):
    if(DIRECTORY):
        #search through the dict for the field
        #put mentor into answer dictionary
        ans = dict()
        for k,v in DIRECTORY:
            if(v[1] == field):
                ans[k] = v
        return ans
    else:
        print("There are no mentors available currently.")

def searchLocation(location: str):
    #search through the dict for the country
    #put mentor into answer dictionary
    if(DIRECTORY):
        ans = dict()
        for k,v in DIRECTORY:
            if(v[2] == location):
                ans[k] = v
        return ans
    else:
        print("There are no mentors available currently.")



  
