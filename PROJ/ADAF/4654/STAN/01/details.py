
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4654"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4654"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TPS61023 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TPS61023-PCB')
    newPart['gitName'].append('Adafruit-TPS61023-PCB')
    newPart['eagleBoard'].append('/Adafruit TPS61023.brd')
    newPart['eagleSchem'].append('/Adafruit TPS61023.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

