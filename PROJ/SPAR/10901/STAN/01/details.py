
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10901"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10901"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Infrared Proximity Breakout VCNL4000')
    newPart['gitRepo'].append('https://github.com/sparkfun/Infrared_Proximity_Breakout-VCNL4000')
    newPart['gitName'].append('Infrared_Proximity_Breakout-VCNL4000')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Infrared_Proximity_Breakout-VCNL4000.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Infrared_Proximity_Breakout-VCNL4000.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

