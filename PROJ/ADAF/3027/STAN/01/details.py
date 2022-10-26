
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3027"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3027"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather 32u4 FONA PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-32u4-FONA-PCB')
    newPart['gitName'].append('Adafruit-Feather-32u4-FONA-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather 32u4 FONA.brd')
    newPart['eagleSchem'].append('/Adafruit Feather 32u4 FONA.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

