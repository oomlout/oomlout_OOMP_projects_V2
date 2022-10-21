
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9266"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9266"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Arduino 328 Main Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Arduino_328_Main_Board')
    newPart['gitName'].append('LilyPad_Arduino_328_Main_Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LilyPad_Main_Board.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LilyPad_Main_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

