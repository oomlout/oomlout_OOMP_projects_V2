
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12039"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12039"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun T5403 Barometric Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_T5403_Barometric_Breakout')
    newPart['gitName'].append('SparkFun_T5403_Barometric_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_T5403_Barometer_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_T5403_Barometer_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

