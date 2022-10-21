
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18077"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18077"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Cryptographic Co Processor Breakout ATECC608A Qwiic')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Cryptographic_Co-Processor_Breakout_ATECC608A_Qwiic')
    newPart['gitName'].append('SparkFun_Cryptographic_Co-Processor_Breakout_ATECC608A_Qwiic')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Cryptographic_Co-processor_ATECC608A.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Cryptographic_Co-processor_ATECC608A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

