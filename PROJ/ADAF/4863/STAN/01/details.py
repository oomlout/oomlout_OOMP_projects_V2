
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4863"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4863"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CYBERDECK PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-CYBERDECK-PCB')
    newPart['gitName'].append('Adafruit-CYBERDECK-PCB')
    newPart['eagleBoard'].append('/Adafruit CyberDeck Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit CyberDeck Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

