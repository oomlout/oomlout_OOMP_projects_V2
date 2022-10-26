
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10612"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10612"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Tri Axis Gyro Breakout L3G4200D')
    newPart['gitRepo'].append('https://github.com/sparkfun/Tri-Axis_Gyro_Breakout-L3G4200D')
    newPart['gitName'].append('Tri-Axis_Gyro_Breakout-L3G4200D')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Gyro_Breakout-L3G4200D.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Gyro_Breakout-L3G4200D.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

