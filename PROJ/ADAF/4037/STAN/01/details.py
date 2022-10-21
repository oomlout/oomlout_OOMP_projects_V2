
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4037"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4037"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit I2S Audio Bonnet for Raspberry Pi PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-I2S-Audio-Bonnet-for-Raspberry-Pi-PCB')
    newPart['gitName'].append('Adafruit-I2S-Audio-Bonnet-for-Raspberry-Pi-PCB')
    newPart['eagleBoard'].append('/Adafruit I2S Audio UDA1334 Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit I2S Audio UDA1334 Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

