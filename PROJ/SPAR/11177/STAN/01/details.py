
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11177"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11177"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Sparkpunk')
    newPart['gitRepo'].append('https://github.com/sparkfun/Sparkpunk')
    newPart['gitName'].append('Sparkpunk')
    newPart['eagleBoard'].append('/hardware/sparkpunk.brd')
    newPart['eagleSchem'].append('/hardware/sparkpunk.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

