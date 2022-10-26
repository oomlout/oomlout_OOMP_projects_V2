
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0759"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0759"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LED Matrix Serial Interface RedGreen')
    newPart['gitRepo'].append('https://github.com/sparkfun/LED_Matrix_Serial_Interface_RedGreen')
    newPart['gitName'].append('LED_Matrix_Serial_Interface_RedGreen')
    newPart['eagleBoard'].append('/Hardware/RG_Medium_Matrix-v11.brd')
    newPart['eagleSchem'].append('/Hardware/RG_Medium_Matrix-v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

