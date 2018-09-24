def main(file):
    loadeddata = loadindata(file)
    cleaned_data = mrclean(loadeddata)
    savedata(cleaned_data)


def loadindata(file):
    arr = list()
    with open(file, 'r') as f:
        for line in f:
            arr.append(line)
    return arr

def savedata(array):
    with open('cleaned_data.py', 'w') as f:
        for i in range(len(array)):
            f.write(str(array[i]) + "\n")


def mrclean(array):
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

        ip = [cityarray, poparray, agearray, avgincarray, permenarray, perwomarray, percaparray, mhvarray, racearray, countyarray]
        cdata.append(ip)
    return cdata


if __name__ == "__main__":
    main("all_cities.py")