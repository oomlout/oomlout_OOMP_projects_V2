
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0364"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0364"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PN532 RFID NFC Breakout')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PN532-RFID-NFC-Breakout')
    newPart['gitName'].append('Adafruit-PN532-RFID-NFC-Breakout')
    newPart['eagleBoard'].append('/Adafruit PN532_Breakout_v1.6.brd')
    newPart['eagleSchem'].append('/Adafruit PN532_Breakout_v1.6.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

