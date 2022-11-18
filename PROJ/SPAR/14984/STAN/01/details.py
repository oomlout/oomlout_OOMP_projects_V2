
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14984"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14984"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SAMD21 ProRF 1W')
    newPart['gitRepo'].append('https://github.com/sparkfun/SAMD21_ProRF_1W')
    newPart['gitName'].append('SAMD21_ProRF_1W')
    newPart['eagleBoard'].append('/Hardware/SAMD21_Pro_RF_1W.brd')
    newPart['eagleSchem'].append('/Hardware/SAMD21_Pro_RF_1W.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

