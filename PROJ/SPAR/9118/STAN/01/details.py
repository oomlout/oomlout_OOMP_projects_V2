
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9118"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9118"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Opto Isolator Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Opto_Isolator_Breakout')
    newPart['gitName'].append('Opto_Isolator_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Opto_Isolator_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Opto_Isolator_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

