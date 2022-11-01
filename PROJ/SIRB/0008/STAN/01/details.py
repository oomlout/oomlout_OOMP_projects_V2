
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0008"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0008"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('QFN16 Breakout Board (sirboard)')
    newPart['gitRepo'].append('https://github.com/sirboard/BreakoutBoards')
    newPart['gitName'].append('BreakoutBoards')
    newPart['kicadBoard'].append('QFN16/QFN16.kicad_pcb')
    newPart['kicadSchem'].append('QFN16/QFN16.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

