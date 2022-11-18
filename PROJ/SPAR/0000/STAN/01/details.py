
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

    newPart['name'].append('UHF RFID Ring Antenna')
    newPart['gitRepo'].append('https://github.com/sparkfun/UHF_RFID_Ring_Antenna')
    newPart['gitName'].append('UHF_RFID_Ring_Antenna')
    newPart['eagleBoard'].append('/Hardware/RFID_Antenna.brd')
    newPart['eagleSchem'].append('/Hardware/RFID_Antenna.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

