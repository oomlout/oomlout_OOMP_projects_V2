
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18354"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18354"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic LED Stick')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_LED_Stick')
    newPart['gitName'].append('SparkFun_Qwiic_LED_Stick')
    newPart['eagleBoard'].append('/Hardware/Qwiic LED Stick.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic LED Stick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

