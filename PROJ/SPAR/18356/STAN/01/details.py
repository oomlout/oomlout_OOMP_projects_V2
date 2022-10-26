
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18356"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18356"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Buck Regulator AP63203')
    newPart['gitRepo'].append('https://github.com/sparkfun/Buck_Regulator_AP63203')
    newPart['gitName'].append('Buck_Regulator_AP63203')
    newPart['eagleBoard'].append('/SparkFun BabyBuck Regulator - AP63203/Hardware/SparkFun BabyBuck Regulator - AP63203.brd')
    newPart['eagleSchem'].append('/SparkFun BabyBuck Regulator - AP63203/Hardware/SparkFun BabyBuck Regulator - AP63203.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

