
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11018"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11018"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RFM22 Shield 434MHz')
    newPart['gitRepo'].append('https://github.com/sparkfun/RFM22_Shield-434MHz')
    newPart['gitName'].append('RFM22_Shield-434MHz')
    newPart['eagleBoard'].append('/Hardware/SparkFun_RFM22_SHield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_RFM22_SHield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

