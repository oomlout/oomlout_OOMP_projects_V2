
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0194"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0194"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Ice Tube Clock')
    newPart['gitRepo'].append('https://github.com/adafruit/Ice-Tube-Clock')
    newPart['gitName'].append('Ice-Tube-Clock')
    newPart['eagleBoard'].append('/pcb/icetube.brd')
    newPart['eagleSchem'].append('/pcb/icetube.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

