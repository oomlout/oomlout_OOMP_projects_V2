
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16400"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16400"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Machine Learning Carrier')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Machine_Learning_Carrier')
    newPart['gitName'].append('MicroMod_Machine_Learning_Carrier')
    newPart['eagleBoard'].append('/Hardware/MachineLearning-MM-Carrier.brd')
    newPart['eagleSchem'].append('/Hardware/MachineLearning-MM-Carrier.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

