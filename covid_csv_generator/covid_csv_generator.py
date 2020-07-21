
import requests
import json

file = open("result.csv","w+")
page = requests.get("https://api.covid19api.com/summary")
data = json.loads(page.text)

country_data= data['Countries']
list_of_countries = [data['Country'] for data in country_data ]


# get key 
def get_index(country):
    for index, value in enumerate(country_data):
        if country.lower() == value['Country'].lower():
            return index

# get summary 
def get_data(country):
    summary_data = country_data[get_index(country)]
    return summary_data

# get mortality rate
def get_mortality_rate(country):
    summary_data = get_data(country)
    mortality_rate=summary_data['TotalDeaths']/summary_data['TotalConfirmed']
    return "{:.4f}%".format(mortality_rate*100)

# get a single country 
def get_country_summary(country):
    summary_data=country_data[get_index(country)]
    new_recovered= summary_data['NewRecovered']
    total_recovered=summary_data['TotalRecovered']
    new_confirmed=summary_data['NewConfirmed']
    total_confirmed=summary_data['TotalConfirmed']
    new_death=summary_data['NewDeaths']
    total_death=summary_data['TotalDeaths']
    mort_rate=get_mortality_rate(country)
    return "{}, {}, {}, {}, {}, {}, {}, {}".format(country, new_recovered,total_recovered,new_confirmed,total_confirmed,new_death,total_death,mort_rate) 

def create_country_data():
    for country in list_of_countries:
        file.write(get_country_summary(country))
        file.write('\n')



file.write("Country, New Positive Case, Total Recovered, New Confirmed, Total confirmed, New Death, Total Death, Mortality Rate")
file.write('\n')
create_country_data()

file.close()