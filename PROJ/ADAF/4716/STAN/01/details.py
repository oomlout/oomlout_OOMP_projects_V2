
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4716"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4716"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MS8607 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MS8607-PCB')
    newPart['gitName'].append('Adafruit-MS8607-PCB')
    newPart['eagleBoard'].append('/Adafruit MS8607.brd')
    newPart['eagleSchem'].append('/Adafruit MS8607.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

