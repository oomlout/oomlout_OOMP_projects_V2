
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11343"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11343"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('IOIO OTG')
    newPart['gitRepo'].append('https://github.com/sparkfun/IOIO-OTG')
    newPart['gitName'].append('IOIO-OTG')
    newPart['eagleBoard'].append('/Hardware/IOIO-OTG.brd')
    newPart['eagleSchem'].append('/Hardware/IOIO-OTG.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

