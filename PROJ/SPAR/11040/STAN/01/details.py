
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11040"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11040"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LED RingCoder Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/LED_RingCoder_Breakout')
    newPart['gitName'].append('LED_RingCoder_Breakout')
    newPart['eagleBoard'].append('/Hardware/LED-RingCoder.brd')
    newPart['eagleSchem'].append('/Hardware/LED-RingCoder.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

