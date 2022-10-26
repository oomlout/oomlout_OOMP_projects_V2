
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4831"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4831"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LTR390 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LTR390-PCB')
    newPart['gitName'].append('Adafruit-LTR390-PCB')
    newPart['eagleBoard'].append('/Adafruit_LTR390.brd')
    newPart['eagleSchem'].append('/Adafruit_LTR390.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

