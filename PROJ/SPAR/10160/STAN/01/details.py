
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10160"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10160"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('DeadOn RTC')
    newPart['gitRepo'].append('https://github.com/sparkfun/DeadOn_RTC')
    newPart['gitName'].append('DeadOn_RTC')
    newPart['eagleBoard'].append('/Hardware/DeadOn RTC - DS3234 Breakout-v11.brd')
    newPart['eagleSchem'].append('/Hardware/DeadOn RTC - DS3234 Breakout-v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

