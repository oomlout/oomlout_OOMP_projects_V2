
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9946"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9946"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Energy Harvester Breakout LTC3588')
    newPart['gitRepo'].append('https://github.com/sparkfun/Energy_Harvester_Breakout-LTC3588')
    newPart['gitName'].append('Energy_Harvester_Breakout-LTC3588')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Energy_Harvester_Breakout-LTC3588.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Energy_Harvester_Breakout-LTC3588.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

