
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18576"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18576"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun MicroMod Main Board Double')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_MicroMod_Main_Board_Double')
    newPart['gitName'].append('SparkFun_MicroMod_Main_Board_Double')
    newPart['eagleBoard'].append('/Hardware/Main Board - Double.brd')
    newPart['eagleSchem'].append('/Hardware/Main Board - Double.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

