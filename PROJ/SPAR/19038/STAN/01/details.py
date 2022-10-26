
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19038"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19038"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun MicroMod Single Pair Ethernet Function Board ADIN1110')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_MicroMod_Single_Pair_Ethernet_Function_Board_ADIN1110')
    newPart['gitName'].append('SparkFun_MicroMod_Single_Pair_Ethernet_Function_Board_ADIN1110')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MicroMod_Function_ADIN1110.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MicroMod_Function_ADIN1110.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

