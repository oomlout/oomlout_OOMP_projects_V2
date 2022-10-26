
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13601"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13601"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SX1509 IO Expander')
    newPart['gitRepo'].append('https://github.com/sparkfun/SX1509_IO-Expander')
    newPart['gitName'].append('SX1509_IO-Expander')
    newPart['eagleBoard'].append('/Hardware/SparkFun-SX1509-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun-SX1509-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

