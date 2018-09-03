#!/usr/bin/env python3
#read_data_from_xlsx.py - reads contents of censuspopdata.xlsx

import openpyxl, pprint

def main():
    print('Opening workbook...')
    wb = openpyxl.load_workbook('censuspopdata.xlsx')
    sheet = wb['Population by Census Tract']
    countyData = {}
    
    print('Reading rows...')
    for row in range(2, sheet.max_row + 1):
        state  = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        pop    = sheet['D' + str(row)].value
        
        # make sure the key for this state exists.
        countyData.setdefault(state, {})
        # make sure the key for this country in this state exists.
        countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
        
        # each row represents one census tract, so increment by one
        countyData[state][county]['tracts'] += 1
        # increase the county pop by the pop in this census tract
        countyData[state][county]['pop'] += int(pop)
    
    # open a new text file and write the contents of countyData to it.
    print('Writing results...')
    # census2010.py can be imported: import census2010 and used: census2010.allData['AK']['Anchorage']
    resultFile = open('census2010.py', 'w')
    resultFile.write('allData = ' + pprint.pformat(countyData))
    resultFile.close()
    print('Done!')
    
if __name__ == "__main__":
    main()