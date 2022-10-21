
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11214"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11214"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MOSFET Power Controller')
    newPart['gitRepo'].append('https://github.com/sparkfun/MOSFET_Power_Controller')
    newPart['gitName'].append('MOSFET_Power_Controller')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MOSFET_Power_Controller.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MOSFET_Power_Controller.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

