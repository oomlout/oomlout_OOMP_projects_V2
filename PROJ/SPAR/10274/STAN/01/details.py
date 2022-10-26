
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10274"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10274"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Arduino Simple')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Arduino_Simple')
    newPart['gitName'].append('LilyPad_Arduino_Simple')
    newPart['eagleBoard'].append('/Hardware/LilyPad-Simple-v25.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad-Simple-v25.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

