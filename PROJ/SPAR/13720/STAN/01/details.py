
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13720"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13720"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MP3 Trigger')
    newPart['gitRepo'].append('https://github.com/sparkfun/MP3_Trigger')
    newPart['gitName'].append('MP3_Trigger')
    newPart['eagleBoard'].append('/Hardware/mp3-trigger.brd')
    newPart['eagleSchem'].append('/Hardware/mp3-trigger.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

