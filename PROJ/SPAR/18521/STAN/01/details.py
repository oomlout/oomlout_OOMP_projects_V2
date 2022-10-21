
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18521"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18521"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Digital Temperature Sensor Breakout AS6212 Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Digital_Temperature_Sensor_Breakout_AS6212_Qwiic')
    newPart['gitName'].append('SparkFun_Digital_Temperature_Sensor_Breakout_AS6212_Qwiic')
    newPart['eagleBoard'].append('/Hardware/Sparkfun_AS6212_Qwiic.brd')
    newPart['eagleSchem'].append('/Hardware/Sparkfun_AS6212_Qwiic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

