
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ELLA"
    oColor = "0007"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0007"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('nandcat')
    newPart['gitRepo'].append('https://github.com/electrolama/nandcat')
    newPart['gitName'].append('nandcat')
    newPart['eagleBoard'].append('Revision A/nand-cat.brd')
    newPart['eagleSchem'].append('Revision A/nand-cat.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

