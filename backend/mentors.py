# DIRECTORY = {}
#be able to sort it by field? 
#search by location?

def add_mentor(directory):
    while True:
        name = input("Name: ")
        field = input("Field: ")
        linkedin = input("Linkedin ID: ") 
        location = input("Country: ")
        if(name.strip() and field.strip() and linkedin.strip()  and location.strip() and linkedin.strip() not in directory):
            #first entry name, second entry field
            directory[linkedin] = [name, field, location]    
            #put mentor into the dictionary
            return
        else:
            print("Your entries {name}, {field}, {linkedin} are invalid. Please try again. ")

def search_field(field: str, directory):
    if(directory):
        #search through the dict for the field
        #put mentor into answer dictionary
        ans = dict()
        for k,v in directory.items():
            if(v[1] == field):
                ans[k] = v
        return ans
    else:
        print("There are no mentors available currently.")

def search_location(location: str, directory):
    #search through the dict for the country
    #put mentor into answer dictionary
    if(directory):
        ans = dict()
        for k,v in directory.items():
            if(v[2] == location):
                ans[k] = v
        return ans
    else:
        print("There are no mentors available currently.")

# fake people
# DIRECTORY['zhiHau475'] = ['Mary Kane', 'Quality Assurance Engineer', 'America'] 
# DIRECTORY['sdEddy4567'] = ['Shelly Zhang', 'Software Engineer', 'Canada'] 
# DIRECTORY['julie34564'] = ['Sarah J. Smith', "Computer Engineer", 'America'] 
# DIRECTORY['dann34fan'] = ['Dan O. Jones', 'Video Game Developer', 'UK'] 
# DIRECTORY['maryjone443'] = ['Sarah J. Smith', 'Computer Engineer', 'France'] 
# DIRECTORY['defes45667'] = ['James Capello', "Computer Engineer", 'America'] 
# DIRECTORY['4833dange4'] = ['Jane T. Foster ', "Software Engineer",'Italy' ] 
# DIRECTORY['dede5674'] = ['Talia Wright', 'Video Game Developer', 'America'] 
# DIRECTORY['green4651123d'] = ['Mia Phan', "Video Game Developer", 'America']

# print(searchLocation("America"))
# print(searchField("Computer Engineer"))
# searchField("Biology")
# searchLocation("Ireland")
# addMentor()
# print(DIRECTORY)

  
