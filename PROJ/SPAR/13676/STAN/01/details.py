
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13676"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13676"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun BME280 Breakout Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_BME280_Breakout_Board')
    newPart['gitName'].append('SparkFun_BME280_Breakout_Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun_BME280_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_BME280_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

