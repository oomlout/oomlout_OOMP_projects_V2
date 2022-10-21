
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15344"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15344"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Capacitive Touch Slider CAP1203')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Capacitive_Touch_Slider_CAP1203')
    newPart['gitName'].append('Qwiic_Capacitive_Touch_Slider_CAP1203')
    newPart['eagleBoard'].append('/Hardware/CAP1203.brd')
    newPart['eagleSchem'].append('/Hardware/CAP1203.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

