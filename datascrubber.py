#Imports needed for the methods in this py file.
import pandas as pd

# Main tag where I load in the data I scrapped, clean it and then save it to a .csv file
def main(file, stringclean):
    loadeddata = loadindata(file)
    cleaned_data = mrclean(loadeddata, stringclean)
    # Convert it to a Dataframe object and save it to a .csv
    DF_CD = pd.DataFrame(cleaned_data)
    alleduatt = pd.read_csv('AllEduAttainment.csv')
    schoollevel = pd.read_csv('2016_PSSA_School_Level_Perfomance_Results.csv')
    DF_CD.columns = ['City Name', 'Population', 'Age', 'Average Income', 'Percent of Men in City', 'Percent of Women in City', 'Per Capita Income', 'Median House Value', 'Racial Breakdown', 'County']
    alleduatt.columns = ['Index', 'County', 'Higher Degree', 'H.S Diploma', 'No H.S Diploma']

    # Do secondary cleaning to remove all additional special characters
    DF_CD = cd_file_cleanpass2(DF_CD)
    alleduatt = all_edu_cleaner(alleduatt)
    schoollevel = school_level_cleaner(schoollevel)

    # Save files to CSV files
    DF_CD.to_csv('Fully_Cleaned_CD_Data', sep='\t', encoding='utf-8')
    #alleduatt.to_csv('Fully_Cleaned_AEA_Data', sep='\t', encoding='utf-8')
    # schoollevel.to_csv('Fully_Cleaned_SS_Data', sep='\t', encoding='utf-8')


# Method to read in data I saved off with CD_scraping.py for cleaning
def loadindata(file):
    arr = list()
    with open(file, 'r') as f:
        for line in f:
            arr.append(line)
    return arr


def loadincsv(filename):
    pssa = pd.read_csv(filename)
    print(pssa)
    return pssa


# Method to take in all rows of city data and clean each element, wrote this before learning about pandas cleaning techniques
def mrclean(array, stringclean):
    cdata = list()
    for i in range(len(array)):
        dataarray = array[i].split("',")

        # Grab and clean city name
        cityarray = dataarray[0][2:]

        metricarray = dataarray[1].split("|")

        # Grab and clean city population
        poparray = metricarray[0].split(" ")[2]

        # Grab and clean average age
        agearray = metricarray[1].split(" ")[1][4:]

        # Grab and clean average income
        avgincarray = metricarray[2].lstrip().split(" ")[0]

        # Grab and clean percent of men in counties
        permenarray = metricarray[3][6:-2]

        # Grab and clean percent of women in counties
        perwomarray = metricarray[4][6:-2]

        # Grab and clean per capita income
        percaparray = metricarray[5].lstrip().split(" ")[0]

        # Grab Median House value and clean it
        if metricarray[6].strip()[-1] == 'n':
            mhvarray = metricarray[6].strip()[:-4]
        elif metricarray[6].strip()[-1] == '(':
            mhvarray = metricarray[6].strip()[:-2]

        # Grab Racial Breakdown and clean it
        racearray = metricarray[7]
        try:
            if racearray[-4:-1] == "])]":
                racearray
            elif racearray.strip() == "[]":
                racearray = "*"
            else:
                racearray = racearray + " " + dataarray[-1].split(" | ")[0][5:]
        except:
            pass

        # Grab county and clean it
        try:
            countyarray = dataarray[-1].split(" | ")[-1][0:-3]
        except:
            countyarray = "***"

        if stringclean is True:
            ip = [str(cityarray), str(poparray), str(agearray), str(avgincarray), str(permenarray), str(perwomarray),
                  str(percaparray), str(mhvarray), str(racearray), str(countyarray)]
        else:
            ip = [cityarray, poparray, agearray, avgincarray, permenarray, perwomarray, percaparray, mhvarray, racearray, countyarray]
        cdata.append(ip)
    return cdata


# Second pass on cleaning data in preparation for data analysis, this uses some of the more advanced methods we learned in class
def cd_file_cleanpass2(data):
    # Remove $ and , from Average Income
    data['Average Income'] = data['Average Income'].str.replace('$', '')
    data['Average Income'] = data['Average Income'].str.replace(',', '')

    # Remove $ and , from Per Capita Income
    data['Per Capita Income'] = data['Per Capita Income'].str.replace('$', '')
    data['Per Capita Income'] = data['Per Capita Income'].str.replace(',', '')

    # Remove $ and , from Median House Value
    data['Median House Value'] = data['Median House Value'].str.replace('$', '')
    data['Median House Value'] = data['Median House Value'].str.replace(',', '')

    # Remove % from Men and Women percentages in city
    data['Percent of Men in City'] = data['Percent of Men in City'].str.replace('%', '')
    data['Percent of Women in City'] = data['Percent of Women in City'].str.replace('%', '')

    # The racial data might take some more time to clean up

    # Get my county column in the same format as other files so we can user DataFram.Merge call
    data['County'] = data['County'].str.replace(' ', '-').str.strip()
    return data


def school_level_cleaner(data):
    # get counties in title case with -County appended
    data['County'] = data['County'].str.title()
    data['County'] = data['County'] + '-County'
    return data


def all_edu_cleaner(data):
    # Clean out all % signs from the educational attainment dataset
    data['Higher Degree'] = data['Higher Degree'].str.replace('%', '')
    data['H.S Diploma'] = data['H.S Diploma'].str.replace('%', '')
    data['No H.S Diploma'] = data['No H.S Diploma'].str.replace('%', '')
    data['County'] = data['County'].str.strip()
    return data


if __name__ == "__main__":
    main("all_cities.py", True)
   #  csvfile = loadincsv('2016_PSSA_School_Level_Perfomance_Results.csv')