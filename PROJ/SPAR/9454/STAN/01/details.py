
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9454"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9454"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('QRE1113 Line Sensor Breakout Digital')
    newPart['gitRepo'].append('https://github.com/sparkfun/QRE1113_Line_Sensor_Breakout-Digital')
    newPart['gitName'].append('QRE1113_Line_Sensor_Breakout-Digital')
    newPart['eagleBoard'].append('/Hardware/SparkFun_QRE1113_Line_Sensor_Breakout_Digital.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_QRE1113_Line_Sensor_Breakout_Digital.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

