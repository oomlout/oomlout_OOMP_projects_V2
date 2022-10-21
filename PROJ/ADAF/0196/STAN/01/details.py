
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0196"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0196"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Proto Screwshield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Proto-Screwshield-PCB')
    newPart['gitName'].append('Adafruit-Proto-Screwshield-PCB')
    newPart['eagleBoard'].append('/wings20.brd')
    newPart['eagleSchem'].append('/wings20.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

