
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SOPA"
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

    newPart['name'].append('Type-c plug lipo')
    newPart['gitRepo'].append('https://github.com/solderparty/type-c_plug_lipo')
    newPart['gitName'].append('type-c_plug_lipo')
    newPart['kicadBoard'].append('type-c_plug_lipo.kicad_pcb')
    newPart['kicadSchem'].append('type-c_plug_lipo.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

