
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "OOML"
    oColor = "0001"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0001"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Dlsb driverboard v1')
    newPart['gitRepo'].append('https://github.com/oomlout/DLSB-DRIVERBOARD-V1')
    newPart['gitName'].append('DLSB-DRIVERBOARD-V1')
    newPart['kicadBoard'].append('DLSB-DRIVERBOARD-V1.kicad_pcb')
    newPart['kicadSchem'].append('DLSB-DRIVERBOARD-V1.kicad_sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

