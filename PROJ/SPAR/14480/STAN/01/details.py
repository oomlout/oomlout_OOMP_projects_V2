
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14480"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14480"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Triple Axis Accelerometer Breakout H3LIS331DL')
    newPart['gitRepo'].append('https://github.com/sparkfun/Triple_Axis_Accelerometer_Breakout-H3LIS331DL')
    newPart['gitName'].append('Triple_Axis_Accelerometer_Breakout-H3LIS331DL')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Tri_Axis_Accel_Breakout-H3LIS331DL.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Tri_Axis_Accel_Breakout-H3LIS331DL.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

