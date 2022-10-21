
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3449"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3449"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DotStar FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DotStar-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-DotStar-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit DotStar Wing.brd')
    newPart['eagleSchem'].append('/Adafruit DotStar Wing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

