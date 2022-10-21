
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10661"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10661"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('VoiceBox Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/VoiceBox_Shield')
    newPart['gitName'].append('VoiceBox_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_VoiceBox_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_VoiceBox_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

