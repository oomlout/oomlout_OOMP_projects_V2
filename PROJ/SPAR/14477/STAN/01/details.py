
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14477"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14477"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic Shield for Photon')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_Shield_for_Photon')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_Shield_for_Photon')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_Shield_for_Photon/Hardware/Qwiic_Shield_for_Photon.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_Shield_for_Photon/Hardware/Qwiic_Shield_for_Photon.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

