
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12898"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12898"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MIDI Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/MIDI_Shield')
    newPart['gitName'].append('MIDI_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MIDI_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MIDI_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

