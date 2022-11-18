
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16770"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16770"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic PT100 ADS122C04')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_PT100_ADS122C04')
    newPart['gitName'].append('Qwiic_PT100_ADS122C04')
    newPart['eagleBoard'].append('/Hardware/Qwiic_PT100.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_PT100.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

