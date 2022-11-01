
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ELLA"
    oColor = "0005"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0005"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('minik')
    newPart['gitRepo'].append('https://github.com/electrolama/minik')
    newPart['gitName'].append('minik')
    newPart['eagleBoard'].append('hardware/Revision A2/minik-RevA2.brd')
    newPart['eagleSchem'].append('hardware/Revision A2/minik-RevA2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

