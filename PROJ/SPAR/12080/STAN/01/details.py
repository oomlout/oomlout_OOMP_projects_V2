
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12080"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12080"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('VKey Voltage Keypad')
    newPart['gitRepo'].append('https://github.com/sparkfun/VKey_Voltage_Keypad')
    newPart['gitName'].append('VKey_Voltage_Keypad')
    newPart['eagleBoard'].append('/hardware/SparkFunVKeyVoltageKeypad.brd')
    newPart['eagleSchem'].append('/hardware/SparkFunVKeyVoltageKeypad.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

