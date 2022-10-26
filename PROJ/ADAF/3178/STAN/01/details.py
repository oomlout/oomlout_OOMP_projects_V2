
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3178"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3178"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather M0 RFM LoRa PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-M0-RFM-LoRa-PCB')
    newPart['gitName'].append('Adafruit-Feather-M0-RFM-LoRa-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather M0 RFMxx.brd')
    newPart['eagleSchem'].append('/Adafruit Feather M0 RFMxx.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

