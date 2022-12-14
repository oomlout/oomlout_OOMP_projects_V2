
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('WAV Trigger')
    newPart['gitRepo'].append('https://github.com/sparkfun/WAV_Trigger')
    newPart['gitName'].append('WAV_Trigger')
    newPart['eagleBoard'].append('/hardware/wavtrigger.brd')
    newPart['eagleSchem'].append('/hardware/wavtrigger.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

