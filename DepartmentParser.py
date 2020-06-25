import xml.etree.ElementTree as ET
import csv

tree = ET.parse("assets/lastDayClose_department_20200531123345.xml")
root = tree.getroot()

departmentData = open('/tmp/departmentData.csv', 'w')

csvWriter = csv.writer(departmentData)

periodSeqNum = root[0].attrib['periodSeqNum']
site = root[1].text
periodIndex = periodSeqNum + site
totals = root[3]

headerPresent = False
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
