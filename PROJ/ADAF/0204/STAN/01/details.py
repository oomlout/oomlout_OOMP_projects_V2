
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0204"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0204"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('monochron')
    newPart['gitRepo'].append('https://github.com/adafruit/monochron')
    newPart['gitName'].append('monochron')
    newPart['eagleBoard'].append('/pcb/ratt.brd')
    newPart['eagleSchem'].append('/pcb/ratt.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

