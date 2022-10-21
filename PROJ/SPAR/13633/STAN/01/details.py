
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13633"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13633"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun LilyPad Simblee')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_LilyPad_Simblee')
    newPart['gitName'].append('SparkFun_LilyPad_Simblee')
    newPart['eagleBoard'].append('/Hardware/LilyPad-Simblee.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad-Simblee.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

