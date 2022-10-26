
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4366"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4366"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TLV493D PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TLV493D-PCB')
    newPart['gitName'].append('Adafruit-TLV493D-PCB')
    newPart['eagleBoard'].append('/Adafruit_TLV493D.brd')
    newPart['eagleSchem'].append('/Adafruit_TLV493D.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

