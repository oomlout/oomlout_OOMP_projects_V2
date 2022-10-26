
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11568"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11568"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Papilio Audio Wing')
    newPart['gitRepo'].append('https://github.com/sparkfun/Papilio_Audio_Wing')
    newPart['gitName'].append('Papilio_Audio_Wing')
    newPart['eagleBoard'].append('/Hardware/Papilio-Audio_Wing.brd')
    newPart['eagleSchem'].append('/Hardware/Papilio-Audio_Wing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

