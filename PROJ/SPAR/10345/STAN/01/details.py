
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10345"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10345"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Triple Axis Accelerometer Breakout LIS331')
    newPart['gitRepo'].append('https://github.com/sparkfun/Triple_Axis_Accelerometer_Breakout-LIS331')
    newPart['gitName'].append('Triple_Axis_Accelerometer_Breakout-LIS331')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Tri_Axis_Accel_Breakout-LIS331.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Tri_Axis_Accel_Breakout-LIS331.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

