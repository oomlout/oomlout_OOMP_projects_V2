
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19895"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19895"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic 9DoF ISM330DHCX MMC5983MA')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_9DoF-ISM330DHCX-MMC5983MA')
    newPart['gitName'].append('SparkFun_Qwiic_9DoF-ISM330DHCX-MMC5983MA')
    newPart['eagleBoard'].append('/Hardware/SparkFun_9DoF_ISM330DHCX-MMC5983MA.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_9DoF_ISM330DHCX-MMC5983MA.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

