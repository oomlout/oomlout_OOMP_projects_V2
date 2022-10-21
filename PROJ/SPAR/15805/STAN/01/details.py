
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15805"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15805"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun High Precision Temperature Sensor TMP117 Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_High_Precision_Temperature_Sensor_TMP117_Qwiic')
    newPart['gitName'].append('SparkFun_High_Precision_Temperature_Sensor_TMP117_Qwiic')
    newPart['eagleBoard'].append('/Hardware/Sparkfun_TMP117_Qwiic.brd')
    newPart['eagleSchem'].append('/Hardware/Sparkfun_TMP117_Qwiic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

