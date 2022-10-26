
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0152"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0152"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('nRF2401A Transceiver Chip Antenna')
    newPart['gitRepo'].append('https://github.com/sparkfun/nRF2401A_Transceiver-Chip_Antenna')
    newPart['gitName'].append('nRF2401A_Transceiver-Chip_Antenna')
    newPart['eagleBoard'].append('/Hardware/nRF2401A-Chip-v11.brd')
    newPart['eagleSchem'].append('/Hardware/nRF2401A-Chip-v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

