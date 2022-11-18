
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "20691"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR20691"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Micro RFID Tag ST25DV64KC Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/Micro_RFID_Tag_ST25DV64KC_Qwiic')
    newPart['gitName'].append('Micro_RFID_Tag_ST25DV64KC_Qwiic')
    newPart['eagleBoard'].append('/Hardware/SparkX_Micro_NFC_RFID_Tag.brd')
    newPart['eagleSchem'].append('/Hardware/SparkX_Micro_NFC_RFID_Tag.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

