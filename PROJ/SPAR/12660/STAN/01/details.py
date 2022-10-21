
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12660"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12660"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MP3 Player Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/MP3_Player_Shield')
    newPart['gitName'].append('MP3_Player_Shield')
    newPart['eagleBoard'].append('/hardware/SparkFunMP3Shield.brd')
    newPart['eagleSchem'].append('/hardware/SparkFunMP3Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

