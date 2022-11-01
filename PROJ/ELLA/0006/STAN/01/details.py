
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ELLA"
    oColor = "0006"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0006"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('disaster01')
    newPart['gitRepo'].append('https://github.com/electrolama/disaster01')
    newPart['gitName'].append('disaster01')
    newPart['eagleBoard'].append('disaster01.brd')
    newPart['eagleSchem'].append('disaster01.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

