
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19036"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19036"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic dToF Imager TMF882X')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_dToF_Imager-TMF882X')
    newPart['gitName'].append('SparkFun_Qwiic_dToF_Imager-TMF882X')
    newPart['eagleBoard'].append('/Hardware/TMF8820/SparkFun_dToF-TMF8820.brd')
    newPart['eagleSchem'].append('/Hardware/TMF8820/SparkFun_dToF-TMF8820.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

