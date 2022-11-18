
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "21223"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR21223"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('GNSS Splitter')
    newPart['gitRepo'].append('https://github.com/sparkfun/GNSS_Splitter')
    newPart['gitName'].append('GNSS_Splitter')
    newPart['eagleBoard'].append('/Hardware/GNSS_Splitter.brd')
    newPart['eagleSchem'].append('/Hardware/GNSS_Splitter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

