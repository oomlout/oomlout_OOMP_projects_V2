
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15801"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15801"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Power Delivery Board USB C')
    newPart['gitRepo'].append('https://github.com/sparkfun/Power_Delivery_Board-USB-C')
    newPart['gitName'].append('Power_Delivery_Board-USB-C')
    newPart['eagleBoard'].append('/Hardware/SparkFun_STUSB4500_USB-PD.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_STUSB4500_USB-PD.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

