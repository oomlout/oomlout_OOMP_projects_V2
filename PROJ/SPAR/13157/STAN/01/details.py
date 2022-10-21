
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13157"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13157"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Breadboard Power Supply Stick 3.3V 1.8V')
    newPart['gitRepo'].append('https://github.com/sparkfun/Breadboard_Power_Supply_Stick_3.3V-1.8V')
    newPart['gitName'].append('Breadboard_Power_Supply_Stick_3.3V-1.8V')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Breadboard_Power_Supply-3.3-1.8SMD.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Breadboard_Power_Supply-3.3-1.8SMD.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

