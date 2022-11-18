
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15074"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15074"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Humidity SHTC3')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Humidity_SHTC3')
    newPart['gitName'].append('Qwiic_Humidity_SHTC3')
    newPart['eagleBoard'].append('/Hardware/SHTC3 Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SHTC3 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

