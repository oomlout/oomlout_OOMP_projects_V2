
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0006"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0006"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroUSB Breakout Board (sirboard)')
    newPart['gitRepo'].append('https://github.com/sirboard/BreakoutBoards')
    newPart['gitName'].append('BreakoutBoards')
    newPart['kicadBoard'].append('MicroUSB/MicroUSB.kicad_pcb')
    newPart['kicadSchem'].append('MicroUSB/MicroUSB.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

