
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13630"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13630"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Photon Weather Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Photon_Weather_Shield')
    newPart['gitName'].append('Photon_Weather_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Photon_Weather_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Photon_Weather_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

