
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15777"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15777"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Lidar Lite')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Lidar_Lite')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Lidar_Lite')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Lidar_Lite/Hardware/Qwiic_Lidar_Lite/Qwiic_Lidar_Lite.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Lidar_Lite/Hardware/Qwiic_Lidar_Lite/Qwiic_Lidar_Lite.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

