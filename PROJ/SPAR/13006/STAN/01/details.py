
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13006"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13006"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Decade Resistance Box')
    newPart['gitRepo'].append('https://github.com/sparkfun/Decade_Resistance_Box')
    newPart['gitName'].append('Decade_Resistance_Box')
    newPart['eagleBoard'].append('/Hardware/SparkFun_decade_resistance_box.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_decade_resistance_box.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

