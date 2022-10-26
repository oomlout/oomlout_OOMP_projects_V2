
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11028"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11028"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MPU 6050 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MPU-6050_Breakout')
    newPart['gitName'].append('MPU-6050_Breakout')
    newPart['eagleBoard'].append('/Hardware/Triple_Axis_Accelerometer_-_Gyro_Breakout_-_MPU-6050.brd')
    newPart['eagleSchem'].append('/Hardware/Triple_Axis_Accelerometer_-_Gyro_Breakout_-_MPU-6050.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

