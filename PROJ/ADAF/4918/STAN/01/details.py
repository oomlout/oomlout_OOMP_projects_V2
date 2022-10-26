
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4918"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4918"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TCA8418 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TCA8418-PCB')
    newPart['gitName'].append('Adafruit-TCA8418-PCB')
    newPart['eagleBoard'].append('/Adafruit TCA8418.brd')
    newPart['eagleSchem'].append('/Adafruit TCA8418.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

