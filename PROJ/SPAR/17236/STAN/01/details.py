
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17236"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17236"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ARGOS ARTIC R2 Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/ARGOS-ARTIC-R2-Shield')
    newPart['gitName'].append('ARGOS-ARTIC-R2-Shield')
    newPart['eagleBoard'].append('/Hardware/ARTIC_R2.brd')
    newPart['eagleSchem'].append('/Hardware/ARTIC_R2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

