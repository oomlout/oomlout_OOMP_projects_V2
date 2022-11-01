
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ELLA"
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

    newPart['name'].append('Zig A Zig Ah')
    newPart['gitRepo'].append('https://github.com/electrolama/zig-a-zig-ah')
    newPart['gitName'].append('zig-a-zig-ah')
    newPart['eagleBoard'].append('zzh/Revision A/zzh.brd')
    newPart['eagleSchem'].append('zzh/Revision A/zzh.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

