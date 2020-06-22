import xml.etree.ElementTree as ET
import csv

tree = ET.parse("assets/lastDayClose_department_20200531123345.xml")
root = tree.getroot()

departmentData = open('/tmp/departmentData.csv', 'w')

csvWriter = csv.writer(departmentData)
