
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14631"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14631"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad USB Plus Standalone')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_USB_Plus_Standalone')
    newPart['gitName'].append('LilyPad_USB_Plus_Standalone')
    newPart['eagleBoard'].append('/Hardware/LilyPad_USB_Plus_Standalone.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_USB_Plus_Standalone.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

