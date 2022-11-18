
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17046"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17046"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Chirp 101 Ultrasonic Rangefinder')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Chirp_101_Ultrasonic_Rangefinder')
    newPart['gitName'].append('Qwiic_Chirp_101_Ultrasonic_Rangefinder')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Chirp_101.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Chirp_101.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

