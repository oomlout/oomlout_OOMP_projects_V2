
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8480"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8480"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Gainer PSoC Development Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/Gainer_PSoC_Development_Board')
    newPart['gitName'].append('Gainer_PSoC_Development_Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Gainer_PSoC_Dev_Board.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Gainer_PSoC_Dev_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

