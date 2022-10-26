
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13629"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13629"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Photon IMU Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Photon_IMU_Shield')
    newPart['gitName'].append('Photon_IMU_Shield')
    newPart['eagleBoard'].append('/Hardware/Photon-IMU-Shield.brd')
    newPart['eagleSchem'].append('/Hardware/Photon-IMU-Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

