
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13169"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13169"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Blackberry Trackballer Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Blackberry_Trackballer_Breakout')
    newPart['gitName'].append('Blackberry_Trackballer_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Blackberry_Trackballer_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Blackberry_Trackballer_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

