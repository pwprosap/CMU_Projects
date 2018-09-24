from bs4 import BeautifulSoup
import requests
import time
import numpy as np


def main(url, loop=0):
    timeout = 60
    while True:  # Had some blacklist issues so added in this retry loop to try and help
        try:
            web_input = requests.get(url, stream=True, timeout=timeout)
            break  # If it downloads, get out and get on with life
        except requests.exceptions.RequestException as e:  # If it doesn't download after the timeout period, an exceptions is thrown, and we try again
            print(e)
            pass
    soup = BeautifulSoup(web_input.content, 'html.parser')
    all_tr = soup.find_all('tr')
    all_cities = list()
    # Collect all cities from the website that we need to scrape
    for city in all_tr:
        try:
            if city['class'][0] == 'rT' or city['class'][0] == 'rS' or city['class'][0] == 'rB':
                name = city.select('a')
                name = str(name[0].contents[0]).split(",")
                all_cities.append(name[0])
        except KeyError:
            pass
    print(len(all_cities))
    data = list()
    for i in range(loop, len(all_cities)): # this needs to be set to range(0, len(all_cities)) to run over all cities
        population = scrapernoscraping(all_cities[i])
        print(str(i) + ": " + str(all_cities[i]))
        time.sleep(1)
        data.append(population)
        if i > 0 and i % 150 == 0:
            # Added in loop to make sure we start at the zip starting with the correct city
            if loop != 0:
                output = list(zip(all_cities[loop:], data))
            else:
                output = list(zip(all_cities, data))
            file = 'output' + str(i) + '.py'
            with open(file, 'w') as f:
                for j in range(0, len(output)):
                    f.write(str(output[j]) + "\n")
    if loop != 0:
        output = list(zip(all_cities[loop:], data))
    else:
        output = list(zip(all_cities, data))
    with open('output.py', 'w') as f:
        for k in range(0, len(output)):
            f.write(str(output[k]) + "\n")


def rerun(line):
    main('http://www.city-data.com/city/Pennsylvania.html', loop=line)


def loadindata(file):
    arr = list()
    with open(file, 'r') as f:
        for line in f:
            arr.append(line)
    return arr


def scrapernoscraping(name):
    namearr = name.split(" ")
    url = 'http://www.city-data.com/city/'
    for k in range(0, len(namearr)):
        if k == len(namearr) - 1:
            url = url + namearr[k]
        else:
            url = url + namearr[k] + "-"
    url = url + '-Pennsylvania.html'
    if name == "O'Hara Township":  #special handling for some weirdly named cities
        url = "http://www.city-data.com/city/O-Hara-Township-Pennsylvania.html"
    elif name == 'Penn State Erie (Behrend)':
        url = 'http://www.city-data.com/city/Penn-State-Erie-Behrend-Pennsylvania.html'
    elif name == 'Tharptown (Uniontown)':
        url = 'http://www.city-data.com/city/Tharptown-Uniontown-Pennsylvania.html'
    timeout = 60
    web_input = requests.get(url, stream=True, timeout=timeout)
    more_soup = BeautifulSoup(web_input.content, 'html.parser')
    all_sections_cp = more_soup.find_all('section', {'id': 'city-population'})
    all_section_ma = more_soup.find_all('section', {'class': 'median-age'})
    all_section_mhi = more_soup.find_all('section', {'class', 'median-income'})
    all_section_pbs = more_soup.find_all('section', {'class', 'population-by-sex'})
    all_section_zip = more_soup.find_all('section', {'id': 'zip-codes'})
    all_ol_county = more_soup.find_all('ol', {'class': 'breadcrumb'})
    all_ul_race = more_soup.find_all('ul', {'class': 'list-group'})
    #I want to try and make a single FOR loop that takes in a list of Beautiful Soup objects to loop over
    tup1 = citypopulation(all_sections_cp)
    tup2 = medianage(all_section_ma)
    tup3, tup6, tup7 = moneystuff(all_section_mhi)
    tup4, tup5 = men_women(all_section_pbs)
    tup8 = racebr(all_ul_race)
    tup9 = zipscrape(all_ol_county)
    # Tuple structure is (population, median age, median household income, % of men, % of women, per capita income, median house value, racial breakdown, county)
    metrics = tup1 + ' | ' + tup2 + ' | ' + tup3 + ' | ' + tup4 + ' | ' + tup5 + ' | ' + tup6 + ' | ' + tup7 + ' | ' + str(tup8) + ' | ' + tup9
    # tup = tuple((tup1, tup2, tup3, tup4, tup5, tup6, tup7, tup8, tup9))
    return metrics


# Helper functions for grabbing certain types of data from City-Data website ////// NOT DONE
def zipscrape(zips):
    for zip in zips:
        try:
            zip2 = zip.select('li')
            tup9 = zip2[2].contents[0].contents[0]
        except:
            pass
        #print(zipout)
        #for i in range(0,len(zipout)):
         #   try:
          #      print(len(zipout[i].contents))
           #     for j in range(0, len(zipout[i].contents)):
            #        print(zipout[i].contents[j])
             #       #zipout = zipout[i]
             #   print(zipout)
              #  for j in range(0, zipout[i]):
               #     zipout = zipout[i].contents
              #      print(zipout)
            #except:
             #   pass
    return tup9 #returns city zip codes


def citypopulation(all_sections_cp):
    for sect in all_sections_cp:
        try:
            tup1 = str(sect.contents[1].split(".")[0]) #population
        except KeyError:
            pass
    return tup1 #returns city population


def racebr(race):
    tup8 = list()
    for sect in race:
        for i in range(0, len(sect.select('li')[1].contents[0]), 2):
            try:
                tup8.append((sect.select('li')[1].contents[0].contents[i].contents[2].contents, sect.select('li')[1].contents[0].contents[i].contents[0].contents)) #racial breakdown
            except(KeyError, AttributeError):
                pass
    return tup8 #returns city breakdown by race


def men_women(pbs):
    for sect in pbs:
        try:
            tup4 = str(sect.select('td')[1].contents[-1]) #% male in city
            tup5 = str(sect.select('td')[3].contents[-1]) #% female in city
        except (KeyError, IndexError):
            pass
    return tup4, tup5    #returns city % of men and women


def moneystuff(ms):
    for sect in ms:
        try:
            tup3 = str(sect.contents[1].strip()) #median-household-income
            tup6 = str(sect.select('br')[1].contents[1]) #per capita income
            try:
                tup7 = str(sect.select('br')[3].contents[1].contents[3]) #median house value
            except:
                tup7 = str(sect.select('br')[1].contents[10])
        except (KeyError, IndexError):
            pass
    return tup3, tup6, tup7 #returns a tuple of median household income, per capita income, median house value


def medianage(mage):
    for sect in mage:
        try:
            tup2 = str(sect.select('td')[1].contents[-1]) #median-age info
        except KeyError:
            pass
    return tup2 #returns city median age


if __name__ == "__main__":
    #scrapernoscraping("Wyalusing")
    main('http://www.city-data.com/city/Pennsylvania.html')
    # rerun(1651)
