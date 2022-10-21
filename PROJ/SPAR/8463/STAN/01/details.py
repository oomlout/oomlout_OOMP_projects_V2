
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8463"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8463"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Buzzer')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Buzzer')
    newPart['gitName'].append('LilyPad_Buzzer')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LilyPad_Buzzer.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LilyPad_Buzzer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

