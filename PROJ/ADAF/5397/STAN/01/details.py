
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5397"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5397"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Charger BFF PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Charger-BFF-PCB')
    newPart['gitName'].append('Adafruit-Charger-BFF-PCB')
    newPart['eagleBoard'].append('/Adafruit LIPoly Charger BFF.brd')
    newPart['eagleSchem'].append('/Adafruit LIPoly Charger BFF.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

