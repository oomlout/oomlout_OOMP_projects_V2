
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0789"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0789"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PN532 RFID NFC Shield')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PN532-RFID-NFC-Shield')
    newPart['gitName'].append('Adafruit-PN532-RFID-NFC-Shield')
    newPart['eagleBoard'].append('/Adafruit_PN532_Shield_v1.0.brd')
    newPart['eagleSchem'].append('/Adafruit_PN532_Shield_v1.0.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

