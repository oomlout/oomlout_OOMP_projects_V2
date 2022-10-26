
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14475"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14475"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Noisy Cricket 1.5W Stereo Amplifier Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Noisy_Cricket-1.5W_Stereo_Amplifier_Breakout')
    newPart['gitName'].append('Noisy_Cricket-1.5W_Stereo_Amplifier_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Noisy_Cricket.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Noisy_Cricket.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

