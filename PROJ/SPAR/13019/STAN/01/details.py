
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13019"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13019"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('BLE Mate2')
    newPart['gitRepo'].append('https://github.com/sparkfun/BLE_Mate2')
    newPart['gitName'].append('BLE_Mate2')
    newPart['eagleBoard'].append('/Hardware/SparkFun_BLEMate2.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_BLEMate2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

