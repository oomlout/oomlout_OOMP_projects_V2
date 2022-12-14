
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14867"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14867"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('QWIIC RFID ID XXLA')
    newPart['gitRepo'].append('https://github.com/sparkfun/QWIIC_RFID_ID-XXLA')
    newPart['gitName'].append('QWIIC_RFID_ID-XXLA')
    newPart['eagleBoard'].append('/Hardware/Qwiic RFID - IDXXLA.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic RFID - IDXXLA.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

