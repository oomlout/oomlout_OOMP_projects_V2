
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13310"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13310"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Ludus ProtoShield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Ludus_ProtoShield')
    newPart['gitName'].append('Ludus_ProtoShield')
    newPart['eagleBoard'].append('/hardware/ludusProtoShield.brd')
    newPart['eagleSchem'].append('/hardware/ludusProtoShield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

