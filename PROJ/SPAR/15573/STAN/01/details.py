
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15573"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15573"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Cryptographic Co Processor Breakout ATECC508A Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Cryptographic_Co-Processor_Breakout_ATECC508A_Qwiic')
    newPart['gitName'].append('SparkFun_Cryptographic_Co-Processor_Breakout_ATECC508A_Qwiic')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Cryptographic_Co-processor_ATECC508A.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Cryptographic_Co-processor_ATECC508A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

