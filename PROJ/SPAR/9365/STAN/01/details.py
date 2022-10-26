
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9365"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9365"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('AD Stereo Converter PCM1803A')
    newPart['gitRepo'].append('https://github.com/sparkfun/AD_Stereo_Converter-PCM1803A')
    newPart['gitName'].append('AD_Stereo_Converter-PCM1803A')
    newPart['eagleBoard'].append('/Hardware/PCM1803A_Breakout-v11.brd')
    newPart['eagleSchem'].append('/Hardware/PCM1803A_Breakout-v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

