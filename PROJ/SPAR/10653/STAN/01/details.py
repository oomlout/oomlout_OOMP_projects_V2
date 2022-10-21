
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10653"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10653"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Voice Recorder Breakout ISD1932')
    newPart['gitRepo'].append('https://github.com/sparkfun/Voice_Recorder_Breakout-ISD1932')
    newPart['gitName'].append('Voice_Recorder_Breakout-ISD1932')
    newPart['eagleBoard'].append('/Hardware/ISD1932 Breakout-v21.brd')
    newPart['eagleSchem'].append('/Hardware/ISD1932 Breakout-v21.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

