import xml.etree.ElementTree as ET

class DataReader:
    def reader(self,element):
        Path="C:/Users/lipikachawla/PycharmProjects/APIDEMOS/Resources/Properties.xml"
        point =open(Path,'rb')
        xml = ET.parse(point,None)
        start = xml.getroot()
        for x in start.findall('buttons'):
          result = x.find(element).text
        return result
