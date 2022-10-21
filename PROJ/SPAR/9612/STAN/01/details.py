
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9612"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9612"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Audio Amplifier Kit STA540')
    newPart['gitRepo'].append('https://github.com/sparkfun/Audio_Amplifier_Kit-STA540')
    newPart['gitName'].append('Audio_Amplifier_Kit-STA540')
    newPart['eagleBoard'].append('/hardware/SparkFun_STA540_Audio_Amp.brd')
    newPart['eagleSchem'].append('/hardware/SparkFun_STA540_Audio_Amp.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

