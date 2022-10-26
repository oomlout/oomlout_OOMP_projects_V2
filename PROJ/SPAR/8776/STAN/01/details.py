
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8776"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8776"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Button Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Button_Board')
    newPart['gitName'].append('LilyPad_Button_Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LilyPad-Button.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LilyPad-Button.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

