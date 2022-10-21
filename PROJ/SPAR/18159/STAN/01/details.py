
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18159"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18159"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Tsunami Super WAV Trigger Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Tsunami_Super_WAV_Trigger_Qwiic')
    newPart['gitName'].append('SparkFun_Tsunami_Super_WAV_Trigger_Qwiic')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Tsunami_Qwiic.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Tsunami_Qwiic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

