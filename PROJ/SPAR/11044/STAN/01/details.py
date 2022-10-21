
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11044"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11044"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Mono Audio Amp Breakout TPA2005D1')
    newPart['gitRepo'].append('https://github.com/sparkfun/Mono_Audio_Amp_Breakout-TPA2005D1')
    newPart['gitName'].append('Mono_Audio_Amp_Breakout-TPA2005D1')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Mono_Audio_Amp-TPA2005D1.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Mono_Audio_Amp-TPA2005D1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

