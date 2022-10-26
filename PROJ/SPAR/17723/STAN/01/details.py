
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17723"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17723"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Qwiic Carrier')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Qwiic_Carrier')
    newPart['gitName'].append('MicroMod_Qwiic_Carrier')
    newPart['eagleBoard'].append('/Hardware/Double/MM-Qwiic-Carrier-Double.brd')
    newPart['eagleSchem'].append('/Hardware/Double/MM-Qwiic-Carrier-Double.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

