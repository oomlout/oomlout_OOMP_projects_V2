
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9721"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9721"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Barometric Pressure Sensor Breakout MPL115A1')
    newPart['gitRepo'].append('https://github.com/sparkfun/Barometric_Pressure_Sensor_Breakout-MPL115A1')
    newPart['gitName'].append('Barometric_Pressure_Sensor_Breakout-MPL115A1')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Pressure_Breakout-MPL115A1.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Pressure_Breakout-MPL115A1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

