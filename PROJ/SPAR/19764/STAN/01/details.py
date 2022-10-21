
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19764"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19764"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic 6DoF ISM330DHCX')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_6DoF_ISM330DHCX')
    newPart['gitName'].append('SparkFun_Qwiic_6DoF_ISM330DHCX')
    newPart['eagleBoard'].append('/Hardware/Qwiic/SparkFun_6DoF_ISM330DHCX.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic/SparkFun_6DoF_ISM330DHCX.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

