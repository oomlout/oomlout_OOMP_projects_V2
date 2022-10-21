
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15272"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15272"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator soil')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_soil')
    newPart['gitName'].append('gator_soil')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Soil_Moisture_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Soil_Moisture_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

