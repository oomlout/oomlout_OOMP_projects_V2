
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13328"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13328"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Photon Wearable Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Photon_Wearable_Shield')
    newPart['gitName'].append('Photon_Wearable_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Photon_Wearable_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Photon_Wearable_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

