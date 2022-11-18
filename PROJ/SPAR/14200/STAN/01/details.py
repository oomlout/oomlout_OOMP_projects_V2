
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14200"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14200"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Robotic Finger Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/Robotic_Finger_Sensor')
    newPart['gitName'].append('Robotic_Finger_Sensor')
    newPart['eagleBoard'].append('/Hardware/Layout/Robotic_Finger_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/Layout/Robotic_Finger_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

