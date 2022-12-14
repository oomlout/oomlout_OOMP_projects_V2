
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5309"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5309"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MSA311 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_MSA311_PCB')
    newPart['gitName'].append('Adafruit_MSA311_PCB')
    newPart['eagleBoard'].append('/Adafruit MSA311.brd')
    newPart['eagleSchem'].append('/Adafruit MSA311.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

