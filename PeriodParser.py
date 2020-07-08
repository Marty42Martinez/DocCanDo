from os import listdir, chdir
from os.path import join, splitext
import xml.etree.ElementTree as ET
import csv

periodPath = 'assets/DepartmentFiles/'
periodFilePaths = [join(periodPath, f) for f in listdir(periodPath) if splitext(f)[1] == '.xml']

periodHeader = [
    "pd_PeriodSeqNum",
    "pd_SiteId",
    "pd_periodBeginDate",
    "pd_periodEndDate",
    "pd_BeginTime",
    "pd_EndTime",
    "pd_tz-GMT",
    "pd_PeriodIndex",
    "pd_SysID"
]

for file in periodFilePaths:
    tree = ET.parse(file)
    root = tree.getroot()
    sysId = root[0].attrib['sysid']
    periodSeqNum = root[0].attrib['periodSeqNum']
    site = root[1].text
    periodBegin = root[0].attrib['periodBeginDate'].split('T')
    periodBeginDate = periodBegin[0]
    [periodBeginTime, periodTZ] = periodBegin[1].split('-')
    periodEnd = root[0].attrib['periodEndDate'].split('T')
    periodEndDate = periodEnd[0]
    periodEndTime = periodEnd[1].split('-')[0]
    periodIndex = periodEndDate + "_" + site


    docName = periodSeqNum + "_" + site + "_" + periodEndDate + "_" + "period.csv"
    chdir('parsedDocs/Period/')
    periodData = open(docName, 'w')

    csvWriter = csv.writer(periodData)
    csvWriter.writerow(periodHeader)

    periodRow = [
        periodSeqNum, 
        site, 
        periodBeginDate,
        periodEndDate,
        periodBeginTime,
        periodEndTime,
        '-'+periodTZ,
        periodIndex,
        sysId
    ]
    csvWriter.writerow(periodRow)
    chdir('../..')
print("All done, yo!")
