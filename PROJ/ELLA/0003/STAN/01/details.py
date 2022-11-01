
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ELLA"
    oColor = "0003"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0003"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('mcore h616 breakout')
    newPart['gitRepo'].append('https://github.com/electrolama/mcore-h616-breakout')
    newPart['gitName'].append('mcore-h616-breakout')
    newPart['eagleBoard'].append('hardware/Revision A1/mcore-h616-breakout-RevA1.brd')
    newPart['eagleSchem'].append('hardware/Revision A1/mcore-h616-breakout-RevA1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

