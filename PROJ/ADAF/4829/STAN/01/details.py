
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4829"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4829"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SGP40 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SGP40-PCB')
    newPart['gitName'].append('Adafruit-SGP40-PCB')
    newPart['eagleBoard'].append('/Adafruit SGP40.brd')
    newPart['eagleSchem'].append('/Adafruit SGP40.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

