
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3309"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3309"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CP2104 Friend PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-CP2104-Friend-PCB')
    newPart['gitName'].append('Adafruit-CP2104-Friend-PCB')
    newPart['eagleBoard'].append('/Adafruit CP2104 Friend.brd')
    newPart['eagleSchem'].append('/Adafruit CP2104 Friend.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

