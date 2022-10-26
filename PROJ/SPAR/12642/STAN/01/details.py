
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12642"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12642"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Sound Detector')
    newPart['gitRepo'].append('https://github.com/sparkfun/Sound_Detector')
    newPart['gitName'].append('Sound_Detector')
    newPart['eagleBoard'].append('/hardware/sound-detector.brd')
    newPart['eagleSchem'].append('/hardware/sound-detector.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

