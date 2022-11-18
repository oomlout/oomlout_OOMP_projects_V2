
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18991"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18991"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkX smol Dynamic NFC RFID Tag')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkX_smol_Dynamic_NFC_RFID_Tag')
    newPart['gitName'].append('SparkX_smol_Dynamic_NFC_RFID_Tag')
    newPart['eagleBoard'].append('/Hardware/SparkX_smol_Dynamic_NFC_RFID_Tag.brd')
    newPart['eagleSchem'].append('/Hardware/SparkX_smol_Dynamic_NFC_RFID_Tag.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

