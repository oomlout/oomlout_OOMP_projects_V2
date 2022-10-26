
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15289"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15289"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator microphone')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_microphone')
    newPart['gitName'].append('gator_microphone')
    newPart['eagleBoard'].append('/hardware/gatormicrophone.brd')
    newPart['eagleSchem'].append('/hardware/gatormicrophone.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

