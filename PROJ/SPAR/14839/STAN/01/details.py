
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14839"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14839"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Bluetooth Mate 4.0')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Bluetooth_Mate_4.0')
    newPart['gitName'].append('https://github.com/sparkfunX/Bluetooth_Mate_4.0')
    newPart['eagleBoard'].append('sourceFiles/git/Bluetooth_Mate_4.0/Hardware/Bluetooth_Mate_4.0.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Bluetooth_Mate_4.0/Hardware/Bluetooth_Mate_4.0.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

