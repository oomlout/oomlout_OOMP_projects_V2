
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0193"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0193"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adapter Board ICD ICD2')
    newPart['gitRepo'].append('https://github.com/sparkfun/Adapter_Board-ICD_ICD2')
    newPart['gitName'].append('Adapter_Board-ICD_ICD2')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ICD-ICD2.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ICD-ICD2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

