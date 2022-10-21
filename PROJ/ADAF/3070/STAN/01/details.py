
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3070"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3070"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit RFM LoRa Radio Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-RFM-LoRa-Radio-Breakout-PCB')
    newPart['gitName'].append('Adafruit-RFM-LoRa-Radio-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit RFM+LoRa Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit RFM+LoRa Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

