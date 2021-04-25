import requests, json

file = open(r"secret.txt","r+")
SECRET = file.readLine()
file.close()
def get_input():
    while True:
        indicator = input("Enter a keyword: ")
        if(indicator):
            country = input("Country: ")
            
            #only getting 1st page for now
            c_file = open(r"","r+")
            correct_country = False
            while True:
                line = c_file.readline()
                if country == line:
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

        with open('jobresults.json', 'w') as json_file:
            json.dump(result, json_file)
        json_file.close()
        
    #If we recieve a JSONDecodeError, our user must have inputed the wrong stock symbol
    except json.decoder.JSONDecodeError:
        #Inform the User that we cannot find stock data for their given symbol
        print(f'Cannot find jobs for {data} on page {page}.')
        return false
            
if __name__ == '__main__':
    get_data("qa", 1)         
        