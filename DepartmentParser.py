from os import listdir, chdir
from os.path import join, splitext
import xml.etree.ElementTree as ET
import csv

departmentPath = 'assets/DepartmentFiles/'
departmentFilePaths = [join(departmentPath, f) for f in listdir(departmentPath) if splitext(f)[1] == '.xml']

totalHeader = [
    "dp_periodSeqNum",
    "dp_site",
    "dp_Sysid",
    "dp_deptType",
    "dp_name",
    "dp_NetSalesCount",
    "dp_NetSalesAmount",
    "dp_NetSalesItemCount",
    "dp_NetSalesUOM",
    "dp_RefundsCount",
    "dp_RefundsAmount",
    "dp_DiscountsCount",
    "dp_DiscountsAmount",
    "dp_PromosCount",
    "dp_PromosAmount",
    "dp_ManualDiscountsCount",
    "dp_ManualDiscountsAmount",
    "dp_GrossSales",
    "dp_PercentOfSales",
    "dp_Index"
]

for file in departmentFilePaths:
    tree = ET.parse(file)
    root = tree.getroot()

    periodSeqNum = root[0].attrib['periodSeqNum']
    site = root[1].text
    periodEnd = root[0].attrib['periodEndDate'].split('T')
    periodEndDate = periodEnd[0]
    periodIndex = periodEndDate + "_" + site

    docName = periodSeqNum + "_" + site + "_" + "_" + "department_totals.csv"
    chdir('parsedDocs/Department/')
    departmentData = open(docName, 'w')

    csvWriter = csv.writer(departmentData)

    totals = root[3]

    headerPresent = False
    
    index = 0
    for member in totals.findall('deptInfo'):
        deptInfo = []
        if (headerPresent == False):
            csvWriter.writerow(totalHeader)
            headerPresent = True
        deptBase = member[0]
        sysid = deptBase.attrib['sysid']
        deptType = deptBase.attrib['deptType']
        name = deptBase[0].text

        netSales = member.find('netSales')
        netSalesCount = netSales[0].text
        netSalesAmount = netSales[1].text
        netSalesItemCount = netSales[2].text
        netSalesUOM = netSales[2].attrib['uom'] if 'uom' in netSales[2].attrib else "None"

        refunds = member.find('refunds')
        refundsCount = refunds[0].text
        refundsAmount = refunds[1].text

        discounts = member.find('discounts')
        discountsCount = discounts[0][0].text
        discountsAmount = discounts[0][1].text

        promosCount = discounts[1][0].text
        promosAmount = discounts[1][1].text

        manualDiscountsCount = discounts[2][0].text
        manualDiscountsAmount = discounts[2][1].text

        grossSales = member.find('grossSales').text
        percentOfSales = member.find('percentOfSales').text


        deptInfo.append(periodSeqNum)
        deptInfo.append(site)
        deptInfo.append(sysid)
        deptInfo.append(deptType)
        deptInfo.append(name)
        deptInfo.append(netSalesCount)
        deptInfo.append(netSalesAmount)
        deptInfo.append(netSalesItemCount)
        deptInfo.append(netSalesUOM)
        deptInfo.append(refundsCount)
        deptInfo.append(refundsAmount)
        deptInfo.append(discountsCount)
        deptInfo.append(discountsAmount)
        deptInfo.append(promosCount)
        deptInfo.append(promosAmount)
        deptInfo.append(manualDiscountsCount)
        deptInfo.append(manualDiscountsAmount)
        deptInfo.append(grossSales)
        deptInfo.append(percentOfSales)
        deptInfo.append(periodIndex)

        csvWriter.writerow(deptInfo)
        index += 1
        print(index)

    departmentData.close()
    chdir('../..')
    print("Processed " + str(index) + " rows")
    print("On to the next File!")
print("Ahh, now I'm done!")
