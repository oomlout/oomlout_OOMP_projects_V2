
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4702"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4702"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit RGB Matrix FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-RGB-Matrix-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-RGB-Matrix-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit RGB Matrix FeatherWing nRF52.brd')
    newPart['eagleSchem'].append('/Adafruit RGB Matrix FeatherWing nRF52.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

