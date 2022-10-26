
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11977"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11977"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ITG 3200 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/ITG-3200_Breakout')
    newPart['gitName'].append('ITG-3200_Breakout')
    newPart['eagleBoard'].append('/Hardware/Triple_axis_digital_-_output_gyro_ITG-3200_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/Triple_axis_digital_-_output_gyro_ITG-3200_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

