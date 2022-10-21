
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16294"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16294"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Thermocouple Amplifer')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Thermocouple_Amplifer')
    newPart['gitName'].append('Qwiic_Thermocouple_Amplifer')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Qwiic_Thermocouple_Amplifier_PCC/SparkFun_Qwiic_Thermocouple_Amplifier_PCC.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Qwiic_Thermocouple_Amplifier_PCC/SparkFun_Qwiic_Thermocouple_Amplifier_PCC.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

