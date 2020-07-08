from os import listdir, chdir
from os.path import join, splitext
import xml.etree.ElementTree as ET
import csv

networkPath = 'assets/NetworkFiles/'
networkFilePaths = [join(networkPath, f) for f in listdir(networkPath) if splitext(f)[1] == '.xml']

totalHeader = [
    "nt_Index",
    "nt_periodSeqNum",
    "nt_SiteID",
    "nt_CardNumber",
    "nt_CardName",
    "nt_CardChargesCount",
    "nt_CardChargesAmount",
    "nt_CardCorrectionsCount",
    "nt_CardCorrectionsAmount"
]

for file in networkFilePaths:
    tree = ET.parse(file)
    root = tree.getroot()

    periodSeqNum = root[0].attrib['periodSeqNum']
    site = root[1].text
    periodEnd = root[0].attrib['periodEndDate'].split('T')
    periodEndDate = periodEnd[0]
    periodIndex = periodEndDate + "_" + site

    docName = periodSeqNum + "_" + site + "_" + "_" + "network_totals.csv"
    chdir('parsedDocs/Network/')
    networkData = open(docName, 'w')

    csvWriter = csv.writer(networkData)

    totals = root[3]

    headerPresent = False
    
    index = 0
    for member in totals.findall('cardInfo'):
        networkInfo = []
        if (headerPresent == False):
            csvWriter.writerow(totalHeader)
            headerPresent = True

        cardNumber = member.find('cardNumber').text
        cardName = member.find('cardName').text

        charges = member.find('cardCharges')
        chargeCount = charges[0].text
        chargeAmount = charges[1].text

        corrections = member.find('cardCorrections')
        correctionCount = corrections[0].text
        correctionAmount = corrections[1].text
        
        networkInfo = [
            periodIndex,
            periodSeqNum,
            site,
            cardNumber,
            cardName,
            chargeCount,
            chargeAmount,
            correctionCount,
            correctionAmount
        ]
        csvWriter.writerow(networkInfo)
        index += 1

    networkData.close()
    chdir('../..')
    print("Cha'ching! " + str(index) + " rows processed")
    print("On to the next File!")
print("Ahh, now I'm done!")
