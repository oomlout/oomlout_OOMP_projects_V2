
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15290"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15290"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Keypad')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Keypad')
    newPart['gitName'].append('Qwiic_Keypad')
    newPart['eagleBoard'].append('/Hardware/Qwiic_keypad.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_keypad.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

