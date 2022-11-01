
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0007"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0007"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MiniUSB Breakout Board (sirboard)')
    newPart['gitRepo'].append('https://github.com/sirboard/BreakoutBoards')
    newPart['gitName'].append('BreakoutBoards')
    newPart['kicadBoard'].append('MiniUSB/MiniUSB.kicad_pcb')
    newPart['kicadSchem'].append('MiniUSB/MiniUSB.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

