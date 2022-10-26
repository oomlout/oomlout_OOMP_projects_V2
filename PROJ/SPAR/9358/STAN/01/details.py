
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9358"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9358"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Bluetooth Mate')
    newPart['gitRepo'].append('https://github.com/sparkfun/Bluetooth_Mate')
    newPart['gitName'].append('Bluetooth_Mate')
    newPart['eagleBoard'].append('/Hardware/BluetoothMate.brd')
    newPart['eagleSchem'].append('/Hardware/BluetoothMate.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

