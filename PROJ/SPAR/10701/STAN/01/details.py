
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10701"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10701"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Color Light Sensor Evaluation Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/Color_Light_Sensor_Evaluation_Board')
    newPart['gitName'].append('Color_Light_Sensor_Evaluation_Board')
    newPart['eagleBoard'].append('/Hardware/ADJD-S311_Breakout-v10.brd')
    newPart['eagleSchem'].append('/Hardware/ADJD-S311_Breakout-v10.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

