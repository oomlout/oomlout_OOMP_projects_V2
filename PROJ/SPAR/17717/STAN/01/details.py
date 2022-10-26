
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17717"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17717"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Pro Micro RP2040')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Pro_Micro-RP2040')
    newPart['gitName'].append('SparkFun_Pro_Micro-RP2040')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ProMicro-RP2040.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ProMicro-RP2040.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

