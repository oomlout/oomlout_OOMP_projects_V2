
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "PDP7"
    oColor = "0004"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0004"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('<built-in method capitalize of str object at 0x000001DF6EA7C350>')
    newPart['gitRepo'].append('https://github.com/pdp7/rotary-encoder-breakout')
    newPart['gitName'].append('rotary-encoder-breakout')
    newPart['kicadBoard'].append('rotary-encoder-breakout.kicad_pcb')
    newPart['kicadSchem'].append('rotary-encoder-breakout.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

