
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12787"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12787"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('APDS 9960 RGB and Gesture Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/APDS-9960_RGB_and_Gesture_Sensor')
    newPart['gitName'].append('APDS-9960_RGB_and_Gesture_Sensor')
    newPart['eagleBoard'].append('/Hardware/SparkFun_APDS-9960_RGB_and_Gesture_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_APDS-9960_RGB_and_Gesture_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

