
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13116"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13116"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Spectrum Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Spectrum_Shield')
    newPart['gitName'].append('Spectrum_Shield')
    newPart['eagleBoard'].append('/Hardware/Spectrum_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/Spectrum_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

