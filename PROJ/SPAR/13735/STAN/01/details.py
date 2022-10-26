
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13735"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13735"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Tri Color LED')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Tri-Color_LED')
    newPart['gitName'].append('LilyPad_Tri-Color_LED')
    newPart['eagleBoard'].append('/Hardware/SparkFun_LilyPad_Tricolor-LED.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_LilyPad_Tricolor-LED.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

