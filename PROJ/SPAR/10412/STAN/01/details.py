
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10412"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10412"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Fabrickit LED Brick')
    newPart['gitRepo'].append('https://github.com/sparkfun/Fabrickit_LED_Brick')
    newPart['gitName'].append('Fabrickit_LED_Brick')
    newPart['eagleBoard'].append('/Hardware/Fabrickit-Bare-Brick.brd')
    newPart['eagleSchem'].append('/Hardware/Fabrickit-Bare-Brick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

