
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14006"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14006"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Lil Soundie Audio Player')
    newPart['gitRepo'].append('https://github.com/sparkfun/Lil_Soundie_Audio_Player')
    newPart['gitName'].append('Lil_Soundie_Audio_Player')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Lil_Soundie_Audio_Player.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Lil_Soundie_Audio_Player.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

