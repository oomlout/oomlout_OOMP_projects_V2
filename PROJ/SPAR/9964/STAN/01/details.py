
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9964"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9964"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Electret Microphone Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Electret_Microphone_Breakout')
    newPart['gitName'].append('Electret_Microphone_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Amplified-Mic-v13.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Amplified-Mic-v13.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

