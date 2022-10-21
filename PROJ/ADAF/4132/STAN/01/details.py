
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4132"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4132"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit GPIO Expander Bonnet PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-GPIO-Expander-Bonnet-PCBs')
    newPart['gitName'].append('Adafruit-GPIO-Expander-Bonnet-PCBs')
    newPart['eagleBoard'].append('/Adafruit GPIO Expander Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit GPIO Expander Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

