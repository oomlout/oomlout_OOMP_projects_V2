
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16441"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16441"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('2D Barcode Scanner')
    newPart['gitRepo'].append('https://github.com/sparkfun/2D_Barcode_Scanner')
    newPart['gitName'].append('2D_Barcode_Scanner')
    newPart['eagleBoard'].append('/Hardware/2DBarcodeScanner.brd')
    newPart['eagleSchem'].append('/Hardware/2DBarcodeScanner.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

