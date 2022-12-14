
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2030"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2030"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PowerBoost 1000 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PowerBoost-1000-PCB')
    newPart['gitName'].append('Adafruit-PowerBoost-1000-PCB')
    newPart['eagleBoard'].append('/Adafruit PowerBoost 1000 Basic.brd')
    newPart['eagleSchem'].append('/Adafruit PowerBoost 1000 Basic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

