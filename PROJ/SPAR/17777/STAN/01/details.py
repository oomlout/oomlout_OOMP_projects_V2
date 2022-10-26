
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17777"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17777"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Zio Qwiic Ultrasonic Distance Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/Zio-Qwiic-Ultrasonic-Distance-Sensor')
    newPart['gitName'].append('Zio-Qwiic-Ultrasonic-Distance-Sensor')
    newPart['eagleBoard'].append('/EAGLE/Zio Ultrasonic Distance Sensor.brd')
    newPart['eagleSchem'].append('/EAGLE/Zio Ultrasonic Distance Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

