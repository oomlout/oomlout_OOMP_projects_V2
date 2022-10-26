
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19035"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19035"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic RFID Tag')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_RFID_Tag')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_RFID_Tag')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_RFID_Tag/Hardware/Qwiic_RFID_Tag.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_RFID_Tag/Hardware/Qwiic_RFID_Tag.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

