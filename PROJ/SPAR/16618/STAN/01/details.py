
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16618"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16618"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic Humidity AHT20')
    newPart['gitRepo'].append('https://github.com/sparkfunX/Qwiic_Humidity_AHT20')
    newPart['gitName'].append('Qwiic_Humidity_AHT20')
    newPart['eagleBoard'].append('Hardware/Qwiic EEPROM.brd')
    newPart['eagleSchem'].append('Hardware/Qwiic EEPROM.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

