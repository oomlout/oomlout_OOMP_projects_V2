
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9598"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9598"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MIDI Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/MIDI_Breakout')
    newPart['gitName'].append('MIDI_Breakout')
    newPart['eagleBoard'].append('/Hardware/MIDI_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/MIDI_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

