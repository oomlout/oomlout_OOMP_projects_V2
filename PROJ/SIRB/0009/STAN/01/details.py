
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SIRB"
    oColor = "0009"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0009"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('QFN20 Breakout Board (sirboard)')
    newPart['gitRepo'].append('https://github.com/sirboard/BreakoutBoards')
    newPart['gitName'].append('BreakoutBoards')
    newPart['kicadBoard'].append('QFN20/QFN20.kicad_pcb')
    newPart['kicadSchem'].append('QFN20/QFN20.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

