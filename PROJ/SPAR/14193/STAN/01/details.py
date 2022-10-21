
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14193"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14193"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CCS811 Air Quality Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/CCS811_Air_Quality_Breakout')
    newPart['gitName'].append('CCS811_Air_Quality_Breakout')
    newPart['eagleBoard'].append('/Hardware/CSS811_CO2_TVOC_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/CSS811_CO2_TVOC_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

