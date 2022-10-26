
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15210"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15210"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun u blox SAM M8Q')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_u-blox_SAM-M8Q')
    newPart['gitName'].append('SparkFun_u-blox_SAM-M8Q')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Ublox SAM-M8Q.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Ublox SAM-M8Q.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

