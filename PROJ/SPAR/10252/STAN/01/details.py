
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10252"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10252"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('IMU Fusion Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/IMU_Fusion_Board')
    newPart['gitName'].append('IMU_Fusion_Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun_IMU_Fusion_Board.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_IMU_Fusion_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

