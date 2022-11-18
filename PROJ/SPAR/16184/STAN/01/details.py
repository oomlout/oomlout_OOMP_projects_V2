
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16184"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16184"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Keyboard Explorer')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Keyboard_Explorer')
    newPart['gitName'].append('Qwiic_Keyboard_Explorer')
    newPart['eagleBoard'].append('/Hardware/Mounting_Plate.brd')
    newPart['eagleSchem'].append('/Hardware/Mounting_Plate.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

