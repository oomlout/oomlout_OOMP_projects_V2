
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16474"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16474"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Photodetector Breakout MAX30101 Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Photodetector_Breakout_MAX30101_Qwiic')
    newPart['gitName'].append('SparkFun_Photodetector_Breakout_MAX30101_Qwiic')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MAX30101_Qwiic.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MAX30101_Qwiic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

