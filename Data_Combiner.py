import pandas as pd


# Method to combine two CSV files together using Pandas merge calls
def main(file1, file2): # File1 should probably be the CD_CSV file mostly
    df_file1 = pd.DataFrame(pd.read_csv(file1, sep='\t', encoding='utf-8'))
    df_file2 = pd.DataFrame(pd.read_csv(file2, sep='\t', encoding='utf-8'))

    # print(df_file1['County'].head(5))
    if file2 == 'Fully_Cleaned_AEA_Data':
        # By making this new DataFrame I cut out the excess index column from the second file.
        stats_from_file_two = pd.DataFrame(data=[df_file2['County'], df_file2['Higher Degree'], df_file2['H.S Diploma'], df_file2['No H.S Diploma']]).transpose()
        df_output = pd.merge(df_file1, stats_from_file_two, on='County')
        df_output.to_csv('CD_and_Statistical_Atlas_Data_Combined', sep='\t', encoding='utf-8')
    elif file2 == 'Fully_Cleaned_SS_Data':
        summarize_school_scores(df_file2)
        # Make new data frame to remove excess index column
        # school_file_two = pd.DataFrame(data=[df_file2['County'], df_file2['Higher Degree'], df_file2['H.S Diploma'], df_file2['No H.S Diploma']]).transpose()
        # df_output = pd.merge(df_file1, df_file2, on='County')
    # print(df_output.head(5))

    # df_output.to_csv('CD_SA_SS_Data_Combined', sep='\t', encoding='utf-8')


def combinezips(file1, file2):
    df_file1 = pd.DataFrame(pd.read_csv(file1, sep=',', encoding='utf-8'))
    df_file2 = pd.DataFrame(pd.read_csv(file2, sep=',', encoding='utf-8'))

    df_file2['ZipCode'] = df_file2['ZipCode'].astype('int32')

    combined = pd.merge(df_file1, df_file2, on='ZipCode')
    combined_main_columns = pd.DataFrame(data=[combined['City'], combined['ZipCode'], combined['Lat'], combined['Long']]).transpose()
    combined_main_columns['ZipCode'] = combined_main_columns['ZipCode'].astype('int32')

    main_file = pd.DataFrame(pd.read_csv('CD_and_Statistical_Atlas_Data_Combined', sep='\t', encoding='utf-8'))
    main_file = main_file.rename(index=str, columns={"City Name": "City"})

    updated_main = pd.merge(main_file, combined_main_columns, on='City')

    # Where I deal with small cities that didn't get given a zip code on web site we scrapped by giving them county level lat/long
    blank_subset = pd.merge(main_file, combined_main_columns, on='City', how='left')
    blank_subset['ZipCode'] = blank_subset['ZipCode'].fillna(0)
    blank_subset = blank_subset[blank_subset['ZipCode'] == 0]
    county_zip1 = pd.DataFrame(pd.read_csv('County_Zip.csv', sep=',', encoding='utf-8'))
    county_zip2 = pd.DataFrame(pd.read_csv('County_Zip_Lat_Long.csv', sep=',', encoding='utf-8'))
    county_zip2['ZipCode'] = county_zip2['ZipCode'].astype('int32')
    combined_county_zip = pd.merge(county_zip1, county_zip2, on='ZipCode')
    combined_county_zip['County'] = combined_county_zip['County'] + '-County'
    blank_subset_filled = pd.merge(blank_subset, combined_county_zip, on='County')

    # Clean out 2 useless columns
    updated_main = updated_main.drop(updated_main.columns[0], axis=1)
    updated_main = updated_main.drop(updated_main.columns[0], axis=1)
    blank_subset_filled = blank_subset_filled.drop(blank_subset_filled.columns[0], axis=1)
    blank_subset_filled = blank_subset_filled.drop(blank_subset_filled.columns[0], axis=1)


    #pd.set_option('display.max_columns', 22)
    del blank_subset_filled['Unnamed: 0_y']
    del blank_subset_filled['Unnamed: 0_x']
    del blank_subset_filled['Long_x']
    del blank_subset_filled['Lat_x']
    del blank_subset_filled['ZipCode_x']
    blank_subset_filled = blank_subset_filled.rename(index=str, columns={'Lat_y': 'Lat', 'Long_y': 'Long', 'ZipCode_y': 'ZipCode'})
    blank_subset_filled['ZipCode'] = blank_subset_filled['ZipCode'].astype('int32')
    blank_subset_filled['Lat'] = blank_subset_filled['Lat'].astype('object')
    blank_subset_filled['Long'] = blank_subset_filled['Long'].astype('object')

    print(blank_subset_filled.dtypes)
    print(updated_main.dtypes)

    df = [updated_main, blank_subset_filled]

    #print(updated_main)
    #print(blank_subset_filled)

    final_dataframe = pd.concat(df)
    final_dataframe.to_csv('CD_SA_with_Zip_all.csv', sep='\t', encoding='utf-8')


# Method to summarize all school score data into one score per county
def summarize_school_scores(data):
    advancedgroup = data['% Advanced'].groupby(data['County'])
    proficientgroup = data['% Proficient'].groupby(data['County'])
    basicgroup = data['% Basic'].groupby(data['County'])
    belowbgroup = data['% Advanced'].groupby(data['County'])

    print(advancedgroup.head(5))


# Make sure to update what files you are passing in for combination. At this point,
# CD_and_Statistical_Atlas_Data_Combined is the master file currently
if __name__ == '__main__':
    # main('Fully_Cleaned_CD_Data', 'Fully_Cleaned_AEA_Data')
    combinezips('City_Zip.csv', 'City_Zip_Lat_Long.csv')