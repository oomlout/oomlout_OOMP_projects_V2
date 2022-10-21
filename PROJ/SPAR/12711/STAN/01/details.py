
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12711"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12711"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB LiPolyCharger SingleCell')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_LiPolyCharger_SingleCell')
    newPart['gitName'].append('USB_LiPolyCharger_SingleCell')
    newPart['eagleBoard'].append('/Hardware/SparkFun_USB_LiPolyCharger_SingleCell.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_USB_LiPolyCharger_SingleCell.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

