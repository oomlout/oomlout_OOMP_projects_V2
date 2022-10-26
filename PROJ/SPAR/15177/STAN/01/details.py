
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15177"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15177"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Proximity Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Proximity_Sensor')
    newPart['gitName'].append('Qwiic_Proximity_Sensor')
    newPart['eagleBoard'].append('/Hardware/Qwiic Proximity Sensor - VCNL4040.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Proximity Sensor - VCNL4040.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

