
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10121"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10121"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('IMU Digital Combo Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/IMU_Digital_Combo_Board')
    newPart['gitName'].append('IMU_Digital_Combo_Board')
    newPart['eagleBoard'].append('/Hardware/IMU_Digital_Combo_Board _-_6_Degrees_of_Freedom_-_ITG3200_-_ADXL345.brd')
    newPart['eagleSchem'].append('/Hardware/IMU_Digital_Combo_Board _-_6_Degrees_of_Freedom_-_ITG3200_-_ADXL345.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

