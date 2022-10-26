
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13058"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13058"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MiP ProMini Pack')
    newPart['gitRepo'].append('https://github.com/sparkfun/MiP_ProMini-Pack')
    newPart['gitName'].append('MiP_ProMini-Pack')
    newPart['eagleBoard'].append('/Hardware/Sparkfun_MiP_ProMini-Pack.brd')
    newPart['eagleSchem'].append('/Hardware/Sparkfun_MiP_ProMini-Pack.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

