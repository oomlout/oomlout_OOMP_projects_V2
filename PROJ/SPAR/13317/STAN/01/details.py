
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13317"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13317"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Sparkfun Big Red Box Proto Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/Sparkfun_Big_Red_Box_Proto_Board')
    newPart['gitName'].append('Sparkfun_Big_Red_Box_Proto_Board')
    newPart['eagleBoard'].append('/Hardware/Big_Red_Box_Proto_Board.brd')
    newPart['eagleSchem'].append('/Hardware/Big_Red_Box_Proto_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

