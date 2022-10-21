
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4074"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4074"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Radio Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Radio-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-Radio-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit LoRa Radio Bonnet with OLED.brd')
    newPart['eagleSchem'].append('/Adafruit LoRa Radio Bonnet with OLED.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

