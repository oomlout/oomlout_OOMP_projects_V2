
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10406"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10406"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RFID Evaluation Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/RFID_Evaluation_Shield')
    newPart['gitName'].append('RFID_Evaluation_Shield')
    newPart['eagleBoard'].append('/Hardware/RFID_Eval_13.56MHz.brd')
    newPart['eagleSchem'].append('/Hardware/RFID_Eval_13.56MHz.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

