
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11769"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11769"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBot Line Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBot_Line_Sensor')
    newPart['gitName'].append('RedBot_Line_Sensor')
    newPart['eagleBoard'].append('/Hardware/RedBot_Line_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/RedBot_Line_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

