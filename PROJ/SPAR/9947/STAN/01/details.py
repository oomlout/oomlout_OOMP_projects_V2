
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9947"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9947"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB Host Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_Host_Shield')
    newPart['gitName'].append('USB_Host_Shield')
    newPart['eagleBoard'].append('/Hardware/USBHostShield-v13.brd')
    newPart['eagleSchem'].append('/Hardware/USBHostShield-v13.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

