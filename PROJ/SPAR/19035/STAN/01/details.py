
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

    newPart['name'].append('Qwiic RFID Tag')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_RFID_Tag')
    newPart['gitName'].append('Qwiic_RFID_Tag')
    newPart['eagleBoard'].append('/Hardware/Qwiic_RFID_Tag.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_RFID_Tag.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

