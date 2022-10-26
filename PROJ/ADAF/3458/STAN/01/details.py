
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3458"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3458"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather 328P PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-328P-PCB')
    newPart['gitName'].append('Adafruit-Feather-328P-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather 328P.brd')
    newPart['eagleSchem'].append('/Adafruit Feather 328P.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

