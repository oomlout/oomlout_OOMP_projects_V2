
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15932"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15932"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Button')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Button')
    newPart['gitName'].append('Qwiic_Button')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Button.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Button.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

