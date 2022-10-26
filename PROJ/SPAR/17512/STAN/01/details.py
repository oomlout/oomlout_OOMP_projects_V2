
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17512"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17512"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic pHAT Extension')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_pHAT_Extension')
    newPart['gitName'].append('SparkFun_Qwiic_pHAT_Extension')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Qwiic_pHAT_Extension.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Qwiic_pHAT_Extension.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

