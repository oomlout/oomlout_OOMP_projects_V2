
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14840"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14840"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Bluetooth HC1x')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Bluetooth_HC1x')
    newPart['gitName'].append('Qwiic_Bluetooth_HC1x')
    newPart['eagleBoard'].append('/Hardware/Qwiic-Bluetooth-HC1X.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic-Bluetooth-HC1X.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

