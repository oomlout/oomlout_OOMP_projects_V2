
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5580"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5580"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MAX17048 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MAX17048-PCB')
    newPart['gitName'].append('Adafruit-MAX17048-PCB')
    newPart['eagleBoard'].append('/Adafruit-MAX17048-STEMMA.brd')
    newPart['eagleSchem'].append('/Adafruit-MAX17048-STEMMA.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

