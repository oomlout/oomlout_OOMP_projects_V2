
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4464"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4464"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ICM20649 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ICM20649-PCB')
    newPart['gitName'].append('Adafruit-ICM20649-PCB')
    newPart['eagleBoard'].append('/Adaruit ICM20649.brd')
    newPart['eagleSchem'].append('/Adaruit ICM20649.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

