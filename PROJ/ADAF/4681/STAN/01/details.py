
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4681"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4681"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit BH1750 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-BH1750-PCB')
    newPart['gitName'].append('Adafruit-BH1750-PCB')
    newPart['eagleBoard'].append('/Adafruit BH1750.brd')
    newPart['eagleSchem'].append('/Adafruit BH1750.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

