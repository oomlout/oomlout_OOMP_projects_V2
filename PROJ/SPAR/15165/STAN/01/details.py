
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15165"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15165"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic MP3 Trigger')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_MP3_Trigger')
    newPart['gitName'].append('Qwiic_MP3_Trigger')
    newPart['eagleBoard'].append('/Hardware/Qwiic MP3 Trigger.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic MP3 Trigger.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

