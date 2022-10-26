
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9774"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9774"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Benchtop Power Board Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/Benchtop_Power_Board_Kit')
    newPart['gitName'].append('Benchtop_Power_Board_Kit')
    newPart['eagleBoard'].append('/Hardware/Benchtop Power Supply.brd')
    newPart['eagleSchem'].append('/Hardware/Benchtop Power Supply.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

