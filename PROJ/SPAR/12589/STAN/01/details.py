
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12589"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12589"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBot Accelerometer')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBot_Accelerometer')
    newPart['gitName'].append('RedBot_Accelerometer')
    newPart['eagleBoard'].append('/Hardware/RedBot Accelerometer.brd')
    newPart['eagleSchem'].append('/Hardware/RedBot Accelerometer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

