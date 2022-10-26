
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/UHF RFID Ring Antenna')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/UHF_RFID_Ring_Antenna')
    newPart['gitName'].append('https://github.com/sparkfunX/UHF_RFID_Ring_Antenna')
    newPart['eagleBoard'].append('sourceFiles/git/UHF_RFID_Ring_Antenna/Hardware/RFID_Antenna.brd')
    newPart['eagleSchem'].append('sourceFiles/git/UHF_RFID_Ring_Antenna/Hardware/RFID_Antenna.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

