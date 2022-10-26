
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0287"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0287"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Brain Machine Kit')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_Brain-Machine-Kit')
    newPart['gitName'].append('Adafruit_Brain-Machine-Kit')
    newPart['eagleBoard'].append('/pcb/brain.brd')
    newPart['eagleSchem'].append('/pcb/brain.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

