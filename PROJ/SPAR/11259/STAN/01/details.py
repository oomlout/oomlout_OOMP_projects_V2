
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11259"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11259"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Power Supply')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Power_Supply')
    newPart['gitName'].append('LilyPad_Power_Supply')
    newPart['eagleBoard'].append('/Hardware/Lilypad_Power_Supply.brd')
    newPart['eagleSchem'].append('/Hardware/Lilypad_Power_Supply.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

