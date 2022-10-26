
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18355"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18355"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic EEPROM - 512Kbit')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_EEPROM_Breakout')
    newPart['gitName'].append('Qwiic_EEPROM_Breakout')
    newPart['eagleBoard'].append('Qwiic AHT20 Breakout.brd')
    newPart['eagleSchem'].append('Qwiic AHT20 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

