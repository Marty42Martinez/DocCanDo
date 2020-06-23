import xml.etree.ElementTree as ET
import csv

tree = ET.parse("assets/lastDayClose_department_20200531123345.xml")
root = tree.getroot()

departmentData = open('/tmp/departmentData.csv', 'w')

csvWriter = csv.writer(departmentData)

data = root.find('pd:departmentPd')
periodIndex = data[0].attrib['periodSeqNum'] + data[1].text
totals = root.find('totals')

totalCount = 0
totalHeader = []
for member in totals.findall('deptInfo'):
    deptInfo = []
    if totalCount == 0:
        netSales = member.find('netSales').tag
        refunds = member.find('refunds').tag
        discounts = member.find('discounts').tag
        grossSales = member.find('grossSales').tag
        percentOfSales = member.find('percentOfSales').tag

        totalHeader.append(netSales)
        totalHeader.append(refunds)
        totalHeader.append(discounts)
        totalHeader.append(grossSales)
        totalHeader.append(percentOfSales)

        csvWriter.writerow(totalHeader)
        count += 1
    netSales = member.find('netSales')[1].text #Amount field
    deptInfo.append(netSales)

departmentData.close()
