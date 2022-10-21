
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13819"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13819"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Arduino ProtoShield Bare PCB')
    newPart['gitRepo'].append('https://github.com/sparkfun/Arduino_ProtoShield_Bare_PCB')
    newPart['gitName'].append('Arduino_ProtoShield_Bare_PCB')
    newPart['eagleBoard'].append('/Hardware/SparkFun_ProtoShield_Kit_rev40.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_ProtoShield_Kit_rev40.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

