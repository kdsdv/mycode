''' Python Basics
    Lab 46: Excel and Intro to Pandas 
    CUSTOMIZATION 01 & 02 | kdsdv '''

# CUSTOMIZATION 01: Transform one type of file to another type of file
# CUSTOMIZATION 02: Manipulate format (i.e. sort columns, delete columns, etcetera)
#!/user/bin/env python3

import pandas  # access to pandas

def main():
    print('CUSTOMIZATION 01 & 02: TRANSFORM & MANIPULATE DATA')  # print message

    # pandas read json, csv, and excel files respectively
    jsonfile = pandas.read_json('5movies.json')
    csvfile = pandas.read_csv('5movies.csv')
    excelfile = pandas.read_excel('5movies.xlsx')

    # sorts the values under "Director" column 
    jsonfile = jsonfile.sort_values('Director')
    csvfile = csvfile.sort_values('Director')
    excelfile = excelfile.sort_values('Director')

    # deletes columns that begin with 'Face"
    jsonfile = jsonfile.loc[:,~jsonfile.columns.str.contains('^Face')]
    csvfile = csvfile.loc[:,~csvfile.columns.str.contains('^Face')]
    excelfile = excelfile.loc[:,~excelfile.columns.str.contains('^Face')]

    # pandas convert files respectively: json to csv, csv to excel, excel to html
    jsonfile.to_csv('5movies-json2csv.csv')
    csvfile.to_excel('5movies-csv2excel.xlsx')
    excelfile.to_html('5movies-excel2html.html')

    print('Data maniuplated and transformed.')  # print message when data has been manipulated and transformed

main()
