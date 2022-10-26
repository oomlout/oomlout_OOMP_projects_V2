
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3382"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3382"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Metro M4 Express PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Metro-M4-Express-PCB')
    newPart['gitName'].append('Adafruit-Metro-M4-Express-PCB')
    newPart['eagleBoard'].append('/Adafruit Metro M4 Express.brd')
    newPart['eagleSchem'].append('/Adafruit Metro M4 Express.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

