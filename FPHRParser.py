from os import listdir, chdir
from os.path import join, splitext
import xml.etree.ElementTree as ET
import csv

fphrPath = 'assets/FPHRFiles/'
fphrFilePaths = [join(fphrPath, f) for f in listdir(fphrPath) if splitext(f)[1] == '.xml']

totalHeader = [
    "fphr_Index",
    "fphr_Product_Sysid",
    "fphr_ProductTypeNumber",
    "fphr_NAXMLFuelGradeID",
    "fphr_ProductName",
    "fphr_NonResettableTransactionCount",
    "fphr_NonResettableTransactionAmount",
    "fphr_NonResettableTransactionVolume",
    "fphr_Site",
    "fphr_PeriodSeqNum"
]

for file in fphrFilePaths:
    tree = ET.parse(file)
    root = tree.getroot()

    periodSeqNum = root[0].attrib['periodSeqNum']
    site = root[1].text
    periodEnd = root[0].attrib['periodEndDate'].split('T')
    periodEndDate = periodEnd[0]
    periodIndex = periodEndDate + "_" + site

    docName = periodSeqNum + "_" + site + "_" + "FPHR_totals.csv"
    chdir('parsedDocs/FPHR/')
    fphrData = open(docName, 'w')

    csvWriter = csv.writer(fphrData)

    totals = root[3]
    headerPresent = False

    index = 0
    for member in totals.findall('byFuelProduct'):
        info = []
        if (headerPresent == False):
            csvWriter.writerow(totalHeader)
            headerPresent = True
        fuelProdBase = member[0]
        sysid = fuelProdBase.attrib['sysid']
        typeNumber = fuelProdBase.attrib['number']
        fuelGradeId = fuelProdBase.attrib['NAXMLFuelGradeID']
        productName = fuelProdBase[0].text

        fuelInfo = member.find('fuelInfo')
        count = fuelInfo[0].text
        amount = fuelInfo[1].text
        volume = fuelInfo[2].text

        info = [
            periodIndex,
            sysid,
            typeNumber,
            fuelGradeId,
            productName,
            count,
            amount,
            volume,
            site,
            periodSeqNum
        ]
        csvWriter.writerow(info)
        index += 1
    fphrData.close()
    chdir('../..')
    print("Runnin' through those Hoses: " + str(index) + " rows processed")
    print("Next!")
print("What'chu waiting for? I'm done!")
