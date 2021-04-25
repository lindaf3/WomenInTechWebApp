import requests, json

file = open("secret.txt","r+")
SECRET = file.readline()
file.close()
def get_input():
    while True:
        indicator = input("Enter a keyword: ")
        if(indicator):
            country = input("Country: ")
            
            #only getting 1st page for now
            c_file = open("countries","r+")
            correct_country = False
            while True:
                line = c_file.readline()
                
                if country+'\n' == line:
                    correct_country = True
                    break
                if not line:
                    break
            
            if(correct_country):
                break
            else:
                print("Invalid country name. Please try again.")
        
    get_data(indicator, country, 1)

        
        
         

#worked = get_data(indicator, 1)
#results =  open('jobresults.json', 'w')

        

        
def get_data(data: str, country: str, indicator: int):
    key = data
    page = indicator
    #Constant required parameters
    base_url = "https://job-search4.p.rapidapi.com/indeed/"
    required = {    'x-rapidapi-key': SECRET,
                    'x-rapidapi-host': "job-search4.p.rapidapi.com"}
    try:          
        search_parameters = [('query', key), ('page', page)]
        feedback = requests.request("GET", base_url, headers=required, params=search_parameters)
        
        result = feedback.json()
        with open('jobresults.json') as json_file:
            d = json.load(json_file)
        json_file.close()
        ans = list()
        
        #print(d['results'][1]['country'])

        for item in d['results']: #loops through every result(job posting), d['results'] is a list
                if item['country'] == country:
                 ans.append(item)
        print(ans)
        
    except json.decoder.JSONDecodeError:
        print(f'Cannot find jobs for {data}.')
        return false
            
if __name__ == '__main__':
    get_input()        
        