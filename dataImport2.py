# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 09:37:29 2020

@author: 10294643
"""

import pandas as pd

## IMPORT SCHOOL DISTRICTS NAMES FILE
refDistrictTable = pd.read_csv('School_District_Names.csv')
refDistrictList = refDistrictTable['Organization Name'][:]
print(refDistrictList)


## IMPORT REGISTRANTS TABLE
# Smart quote ' not unicode, need to encode with 'cp1252'
registrantsTable = pd.read_csv('Panel_Discussion_Registrants.csv',encoding='cp1252')
registrantsDistricts = registrantsTable['School District or Organization']
print(registrantsTable)
print(type(registrantsDistricts))


## REMOVE EMPTY ROWS
districtCol = []
typeCol = []

for inputDistrict in registrantsTable['School District or Organization']:
    type_inputDistrict = type(inputDistrict)
    districtCol.append(inputDistrict)
    typeCol.append(type_inputDistrict)

typeTable = {"District": districtCol, "Data Type": typeCol}
typeTableFrame = pd.DataFrame(typeTable)

emptyIndices = typeTableFrame[typeTableFrame['Data Type'] == float].index.values
print(emptyIndices)


## CLEAN UP DATA
registrantsTable = registrantsTable.drop(emptyIndices)
registrantsDistricts = registrantsTable['School District or Organization']
print(registrantsDistricts)

registrantsDistrictsCAPS = []

for inputDistrict in registrantsDistricts:
    inputDistrict = inputDistrict.upper()
#    print(inputDistrict)
    registrantsDistrictsCAPS.append(inputDistrict)
print(registrantsDistrictsCAPS)

A_Rows = refDistrictList[0:15]
print(A_Rows)
firstWordDistricts = []
for refDistrict in A_Rows:
    #print(district)
    if 'SCHOOL DISTRICT' in refDistrict:
        refDistrict = refDistrict.replace('SCHOOL DISTRICT', '')
#        print(district)
        refDistrictParsed = refDistrict.split(' ')
        keyword = refDistrictParsed[0]
#        print(keyword)
        firstWordDistricts.append(keyword)
#        print(firstWordDistricts)

for refDistrict in firstWordDistricts:
#    print(refDistrict)
    if refDistrict in registrantsDistrictsCAPS:
        indxRegr = registrantsDistrictsCAPS.index(refDistrict)

        print('{} reference district found at index {} of registrants list'.format(refDistrict, indxRegr))
        print('Registrants Inputted District Name: {}'.format(registrantsDistrictsCAPS[indxRegr]))
        
        #NEED TO LIST ALL INSTANCES WHERE 'refDistrict' IS FOUND IN 'registrantsDistrictsCAPS'
        
        
# print(indxRegr)
#        print(registrantsDistrictsCAPS[indxRegr])
        
