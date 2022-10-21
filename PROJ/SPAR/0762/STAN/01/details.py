
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0762"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0762"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB Bit Whacker 18F2553')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_Bit_Whacker-18F2553')
    newPart['gitName'].append('USB_Bit_Whacker-18F2553')
    newPart['eagleBoard'].append('/Hardware/USB_Bit_Whacker-18F2553.brd')
    newPart['eagleSchem'].append('/Hardware/USB_Bit_Whacker-18F2553.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

