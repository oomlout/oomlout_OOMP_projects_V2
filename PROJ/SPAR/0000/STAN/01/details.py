
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TransmogriShield')
    newPart['gitRepo'].append('https://github.com/sparkfun/TransmogriShield')
    newPart['gitName'].append('TransmogriShield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_TransmogriShield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_TransmogriShield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

