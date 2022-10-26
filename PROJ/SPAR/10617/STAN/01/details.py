
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10617"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10617"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Lipo Fuel Gauge')
    newPart['gitRepo'].append('https://github.com/sparkfun/Lipo_Fuel_Gauge')
    newPart['gitName'].append('Lipo_Fuel_Gauge')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Lipo_Fuel_Gauge.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Lipo_Fuel_Gauge.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

