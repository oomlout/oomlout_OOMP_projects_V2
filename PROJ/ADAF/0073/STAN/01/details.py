
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0073"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0073"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TV B Gone kit')
    newPart['gitRepo'].append('https://github.com/adafruit/TV-B-Gone-kit')
    newPart['gitName'].append('TV-B-Gone-kit')
    newPart['eagleBoard'].append('/pcb/tvbgone3.brd')
    newPart['eagleSchem'].append('/pcb/tvbgone3.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

