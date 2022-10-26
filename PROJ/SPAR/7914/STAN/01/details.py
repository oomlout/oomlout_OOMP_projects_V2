
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "7914"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR7914"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ProtoShield Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/ProtoShield_Kit')
    newPart['gitName'].append('ProtoShield_Kit')
    newPart['eagleBoard'].append('/Hardware/Bare_PCB/Hardware/SparkFun_ProtoShield_Kit.brd')
    newPart['eagleSchem'].append('/Hardware/Bare_PCB/Hardware/SparkFun_ProtoShield_Kit.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

