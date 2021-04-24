import requests, json


def get_data(data: str, indicator: int):
    key = data
    page = indicator
    #Constant required parameters
    base_url = "https://job-search4.p.rapidapi.com/indeed/"
    required = {    'x-rapidapi-key': "883f54a2eemshc4d6fd4695f96aap1cf784jsn76c6b3c90387",
                    'x-rapidapi-host': "job-search4.p.rapidapi.com"}
    try:          
        search_parameters = [('query', key), ('page', page)]
        feedback = requests.request("GET", base_url, headers=required, params=search_parameters)
        
        result = feedback.json()

        with open('jobresults.json', 'w') as json_file:
            json.dump(result, json_file)
        
    #If we recieve a JSONDecodeError, our user must have inputed the wrong stock symbol
    except json.decoder.JSONDecodeError:
        #Inform the User that we cannot find stock data for their given symbol
        print(f'Cannot find jobs for {data} on page {page}.')
            
if __name__ == '__main__':
    get_data("qa", 1)         
        