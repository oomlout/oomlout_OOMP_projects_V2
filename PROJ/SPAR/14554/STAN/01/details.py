
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14554"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14554"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Papa Soundie Audio Player')
    newPart['gitRepo'].append('https://github.com/sparkfun/Papa_Soundie_Audio_Player')
    newPart['gitName'].append('Papa_Soundie_Audio_Player')
    newPart['eagleBoard'].append('/Hardware/Papa_Soundie.brd')
    newPart['eagleSchem'].append('/Hardware/Papa_Soundie.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

