
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17731"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17731"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Zio Qwiic Soil Moisture Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/Zio-Qwiic-Soil-Moisture-Sensor')
    newPart['gitName'].append('Zio-Qwiic-Soil-Moisture-Sensor')
    newPart['eagleBoard'].append('/EAGLE/SparkFun Qwiic Soil Moisture Sensor.brd')
    newPart['eagleSchem'].append('/EAGLE/SparkFun Qwiic Soil Moisture Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

