
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14973"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14973"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('BufferSaver')
    newPart['gitRepo'].append('https://github.com/sparkfun/BufferSaver')
    newPart['gitName'].append('BufferSaver')
    newPart['eagleBoard'].append('/Hardware/BufferSaver.brd')
    newPart['eagleSchem'].append('/Hardware/BufferSaver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

