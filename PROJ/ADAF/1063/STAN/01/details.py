
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1063"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1063"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MAX4466 Electret Mic Amplifier PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MAX4466-Electret-Mic-Amplifier-PCBs')
    newPart['gitName'].append('Adafruit-MAX4466-Electret-Mic-Amplifier-PCBs')
    newPart['eagleBoard'].append('/Adafruit MAX4466 Mic Amp.brd')
    newPart['eagleSchem'].append('/Adafruit MAX4466 Mic Amp.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

