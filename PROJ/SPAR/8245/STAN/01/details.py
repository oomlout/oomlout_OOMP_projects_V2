
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8245"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8245"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Serial USB Adapter Nike iPod')
    newPart['gitRepo'].append('https://github.com/sparkfun/Serial_USB_Adapter-Nike_iPod')
    newPart['gitName'].append('Serial_USB_Adapter-Nike_iPod')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Serial_USB_Adapter-iPodNike.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Serial_USB_Adapter-iPodNike.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

