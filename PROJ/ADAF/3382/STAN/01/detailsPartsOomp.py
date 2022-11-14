def load(newPart,it):
    it['PROJ-ADAF-3382-STAN-01']['oompParts'] = [{'C3': {'OOMPID': 'CAPC-0805-X-UF10-V25', 'FULL': {'DESC': '', 'PART': 'C3', 'DEVICE': '0805-NO 10uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10uF', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C3,10uF,0805-NO 10uF,0805-NO,,,'}},
       'C1': {'OOMPID': 'CAPC-0805-X-UF10-V25', 'FULL': {'DESC': '', 'PART': 'C1', 'DEVICE': '0805-NO 10uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10uF', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C1,10uF,0805-NO 10uF,0805-NO,,,'}},
       'R4': {'OOMPID': 'RESE-0603-X-O102-01', 'FULL': {'DESC': '', 'PART': 'R4', 'DEVICE': '0603-NO 1K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '1K', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R4,1K,0603-NO 1K,0603-NO,,,'}},
       'C4': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C4', 'DEVICE': '0603-NO .1u', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '.1u', 'VALUENUMBER': '.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C4,.1u,0603-NO .1u,0603-NO,,,'}},
       'C15': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C15', 'DEVICE': '0603-NO .1u', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '.1u', 'VALUENUMBER': '.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C15,.1u,0603-NO .1u,0603-NO,,,'}},
       'C14': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C14', 'DEVICE': '0603-NO .1u', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '.1u', 'VALUENUMBER': '.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C14,.1u,0603-NO .1u,0603-NO,,,'}},
       'C8': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C8', 'DEVICE': '0603-NO .1u', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '.1u', 'VALUENUMBER': '.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C8,.1u,0603-NO .1u,0603-NO,,,'}},
       'C11': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C11', 'DEVICE': '0603-NO .1u', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '.1u', 'VALUENUMBER': '.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C11,.1u,0603-NO .1u,0603-NO,,,'}},
       'C16': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C16', 'DEVICE': '0603-NO .1u', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '.1u', 'VALUENUMBER': '.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C16,.1u,0603-NO .1u,0603-NO,,,'}},
       'C6': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C6', 'DEVICE': '0603-NO .1u', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '.1u', 'VALUENUMBER': '.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C6,.1u,0603-NO .1u,0603-NO,,,'}},
       'C10': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C10', 'DEVICE': '0603-NO .1u', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '.1u', 'VALUENUMBER': '.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C10,.1u,0603-NO .1u,0603-NO,,,'}},
       'C9': {'OOMPID': 'CAPC-0603-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C9', 'DEVICE': '0603-NO 1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C9,1uF,0603-NO 1uF,0603-NO,,,'}},
       'R5': {'OOMPID': 'RESE-0603-X-O103-01', 'FULL': {'DESC': '', 'PART': 'R5', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R5,10K,0603-NO 10K,0603-NO,,,'}},
       'R7': {'OOMPID': 'RESE-0603-X-O103-01', 'FULL': {'DESC': '', 'PART': 'R7', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R7,10K,0603-NO 10K,0603-NO,,,'}},
       'R3': {'OOMPID': 'RESE-0603-X-O103-01', 'FULL': {'DESC': '', 'PART': 'R3', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R3,10K,0603-NO 10K,0603-NO,,,'}},
       'IOL0': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'IOL0', 'DEVICE': '1X08_OVALWAVE 20610', 'PACKAGE': '1X08_OVALWAVE', 'PARTLETTER': 'IOL', 'VALUE': '20610', 'VALUENUMBER': '20610', 'PACKAGENUMBER': '108', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'IOL0,20610,1X08_OVALWAVE 20610,1X08_OVALWAVE,,,'}},
       'POWER0': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'POWER0', 'DEVICE': '1X08_OVALWAVE 20610', 'PACKAGE': '1X08_OVALWAVE', 'PARTLETTER': 'POWER', 'VALUE': '20610', 'VALUENUMBER': '20610', 'PACKAGENUMBER': '108', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'POWER0,20610,1X08_OVALWAVE 20610,1X08_OVALWAVE,,,'}},
       'C17': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C17', 'DEVICE': '0603-NO 0.1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C17,0.1uF,0603-NO 0.1uF,0603-NO,,,'}},
       'C13': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C13', 'DEVICE': '0603-NO 0.1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C13,0.1uF,0603-NO 0.1uF,0603-NO,,,'}},
       'C12': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C12', 'DEVICE': '0603-NO 0.1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C12,0.1uF,0603-NO 0.1uF,0603-NO,,,'}},
       'JP1': {'OOMPID': 'HEAD-I01-X-PI01-01', 'FULL': {'DESC': '', 'PART': 'JP1', 'DEVICE': '1X01_ROUND ', 'PACKAGE': '1X01_ROUND', 'PARTLETTER': 'JP', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '101', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'JP1,,1X01_ROUND ,1X01_ROUND,,,'}},
       'PC2': {'OOMPID': 'CAPE-PAND-X-UF47-V63D', 'FULL': {'DESC': '', 'PART': 'PC2', 'DEVICE': 'PANASONIC_D 47uF+/6.3V+', 'PACKAGE': 'PANASONIC_D', 'PARTLETTER': 'PC', 'VALUE': '47uF+/6.3V+', 'VALUENUMBER': '47+/6.3+', 'PACKAGENUMBER': '', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'PC2,47uF+/6.3V+,PANASONIC_D 47uF+/6.3V+,PANASONIC_D,,,'}},
       'RXLED0': {'OOMPID': 'UNMATCHED-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'RXLED0', 'DEVICE': 'CHIPLED_0805_NOOUTLINE YELLOW', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'RXLED', 'VALUE': 'YELLOW', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'RXLED0,YELLOW,CHIPLED_0805_NOOUTLINE YELLOW,CHIPLED_0805_NOOUTLINE,,,'}},
       'TXLED0': {'OOMPID': 'UNMATCHED-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'TXLED0', 'DEVICE': 'CHIPLED_0805_NOOUTLINE YELLOW', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'TXLED', 'VALUE': 'YELLOW', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'TXLED0,YELLOW,CHIPLED_0805_NOOUTLINE YELLOW,CHIPLED_0805_NOOUTLINE,,,'}},
       'R11': {'OOMPID': 'RESE-0603-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'R11', 'DEVICE': '0603-NO 330R', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '330R', 'VALUENUMBER': '330', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R11,330R,0603-NO 330R,0603-NO,,,'}},
       'LED1': {'OOMPID': 'LEDS-3535-RGB-K2812-01', 'FULL': {'DESC': '', 'PART': 'LED1', 'DEVICE': 'LED3535 WS2812B3535', 'PACKAGE': 'LED3535', 'PARTLETTER': 'LED', 'VALUE': 'WS2812B3535', 'VALUENUMBER': '28123535', 'PACKAGENUMBER': '3535', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'LED1,WS2812B3535,LED3535 WS2812B3535,LED3535,,,'}},
       'IC3': {'OOMPID': 'UNMATCHED-SO235-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'IC3', 'DEVICE': 'SOT23-5 74LVC1G125D', 'PACKAGE': 'SOT23-5', 'PARTLETTER': 'IC', 'VALUE': '74LVC1G125D', 'VALUENUMBER': '741125', 'PACKAGENUMBER': '235', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'IC3,74LVC1G125D,SOT23-5 74LVC1G125D,SOT23-5,,,'}},
       'ICSP0': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'ICSP0', 'DEVICE': '2X03_ROUND_70MIL 3x2 M', 'PACKAGE': '2X03_ROUND_70MIL', 'PARTLETTER': 'ICSP', 'VALUE': '3x2 M', 'VALUENUMBER': '32 ', 'PACKAGENUMBER': '20370', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'ICSP0,3x2 M,2X03_ROUND_70MIL 3x2 M,2X03_ROUND_70MIL,,,'}},
       'U1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'U1', 'DEVICE': 'SOT223-R NCP1117ST50T3G', 'PACKAGE': 'SOT223-R', 'PARTLETTER': 'U', 'VALUE': 'NCP1117ST50T3G', 'VALUENUMBER': '1117503', 'PACKAGENUMBER': '223', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U1,NCP1117ST50T3G,SOT223-R NCP1117ST50T3G,SOT223-R,,,'}},
       'PC1': {'OOMPID': 'CAPE-PAND-X-UF47-V25', 'FULL': {'DESC': '', 'PART': 'PC1', 'DEVICE': 'PANASONIC_D 47uF/25V', 'PACKAGE': 'PANASONIC_D', 'PARTLETTER': 'PC', 'VALUE': '47uF/25V', 'VALUENUMBER': '47/25', 'PACKAGENUMBER': '', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'PC1,47uF/25V,PANASONIC_D 47uF/25V,PANASONIC_D,,,'}},
       'F2': {'OOMPID': 'UNMATCHED-1206-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'F2', 'DEVICE': 'R1206 500mA', 'PACKAGE': 'R1206', 'PARTLETTER': 'F', 'VALUE': '500mA', 'VALUENUMBER': '500', 'PACKAGENUMBER': '1206', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'F2,500mA,R1206 500mA,R1206,,,'}},
       'L1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'L1', 'DEVICE': 'INDUCTOR_1007 10uH', 'PACKAGE': 'INDUCTOR_1007', 'PARTLETTER': 'L', 'VALUE': '10uH', 'VALUENUMBER': '10', 'PACKAGENUMBER': '1007', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'L1,10uH,INDUCTOR_1007 10uH,INDUCTOR_1007,,,'}},
       'T2': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'T2', 'DEVICE': 'SOT-23 DMP3098L-7', 'PACKAGE': 'SOT-23', 'PARTLETTER': 'T', 'VALUE': 'DMP3098L-7', 'VALUENUMBER': '3098-7', 'PACKAGENUMBER': '23', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'T2,DMP3098L-7,SOT-23 DMP3098L-7,SOT-23,,,'}},
       'TR1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'TR1', 'DEVICE': 'SOT-23 DMP3098L-7', 'PACKAGE': 'SOT-23', 'PARTLETTER': 'TR', 'VALUE': 'DMP3098L-7', 'VALUENUMBER': '3098-7', 'PACKAGENUMBER': '23', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'TR1,DMP3098L-7,SOT-23 DMP3098L-7,SOT-23,,,'}},
       'ON0': {'OOMPID': 'UNMATCHED-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'ON0', 'DEVICE': 'CHIPLED_0805_NOOUTLINE GREEN', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'ON', 'VALUE': 'GREEN', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'ON0,GREEN,CHIPLED_0805_NOOUTLINE GREEN,CHIPLED_0805_NOOUTLINE,,,'}},
       'C2': {'OOMPID': 'CAPC-0805-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C2', 'DEVICE': '0805-NO 0.1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C2,0.1uF,0805-NO 0.1uF,0805-NO,,,'}},
       'RESET0': {'OOMPID': 'BUTA-6060-X-STAN-01', 'FULL': {'DESC': '', 'PART': 'RESET0', 'DEVICE': 'EVQ-Q2 EVQQ 6mm', 'PACKAGE': 'EVQ-Q2', 'PARTLETTER': 'RESET', 'VALUE': 'EVQQ 6mm', 'VALUENUMBER': ' 6', 'PACKAGENUMBER': '2', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'RESET0,EVQQ 6mm,EVQ-Q2 EVQQ 6mm,EVQ-Q2,,,'}},
       'L0': {'OOMPID': 'UNMATCHED-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'L0', 'DEVICE': 'CHIPLED_0805_NOOUTLINE RED', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'L', 'VALUE': 'RED', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'L0,RED,CHIPLED_0805_NOOUTLINE RED,CHIPLED_0805_NOOUTLINE,,,'}},
       'X4': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X4', 'DEVICE': 'XTAL3215 32.768', 'PACKAGE': 'XTAL3215', 'PARTLETTER': 'X', 'VALUE': '32.768', 'VALUENUMBER': '32.768', 'PACKAGENUMBER': '3215', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X4,32.768,XTAL3215 32.768,XTAL3215,,,'}},
       'AD0': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'AD0', 'DEVICE': '1X06_OVALWAVE 20609', 'PACKAGE': '1X06_OVALWAVE', 'PARTLETTER': 'AD', 'VALUE': '20609', 'VALUENUMBER': '20609', 'PACKAGENUMBER': '106', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'AD0,20609,1X06_OVALWAVE 20609,1X06_OVALWAVE,,,'}},
       'SW1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SW1', 'DEVICE': 'SPDT_SMT_SSSS811101 ', 'PACKAGE': 'SPDT_SMT_SSSS811101', 'PARTLETTER': 'SW', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '811101', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW1,,SPDT_SMT_SSSS811101 ,SPDT_SMT_SSSS811101,,,'}},
       'U3': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'U3', 'DEVICE': 'SOIC8_208MIL SPI Flash', 'PACKAGE': 'SOIC8_208MIL', 'PARTLETTER': 'U', 'VALUE': 'SPI Flash', 'VALUENUMBER': ' ', 'PACKAGENUMBER': '8208', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U3,SPI Flash,SOIC8_208MIL SPI Flash,SOIC8_208MIL,,,'}},
       'X5': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X5', 'DEVICE': 'DCJACK_2MM_PTH 2.1mm', 'PACKAGE': 'DCJACK_2MM_PTH', 'PARTLETTER': 'X', 'VALUE': '2.1mm', 'VALUENUMBER': '2.1', 'PACKAGENUMBER': '2', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X5,2.1mm,DCJACK_2MM_PTH 2.1mm,DCJACK_2MM_PTH,,,'}},
       'X3': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X3', 'DEVICE': '4UCONN_20329_V2 20329', 'PACKAGE': '4UCONN_20329_V2', 'PARTLETTER': 'X', 'VALUE': '20329', 'VALUENUMBER': '20329', 'PACKAGENUMBER': '4203292', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X3,20329,4UCONN_20329_V2 20329,4UCONN_20329_V2,,,'}},
       'C7': {'OOMPID': 'CAPC-0603-X-PF22-V50', 'FULL': {'DESC': '', 'PART': 'C7', 'DEVICE': '0603-NO 22pF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '22pF', 'VALUENUMBER': '22', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C7,22pF,0603-NO 22pF,0603-NO,,,'}},
       'C5': {'OOMPID': 'CAPC-0603-X-PF22-V50', 'FULL': {'DESC': '', 'PART': 'C5', 'DEVICE': '0603-NO 22pF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '22pF', 'VALUENUMBER': '22', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C5,22pF,0603-NO 22pF,0603-NO,,,'}},
       'U2': {'OOMPID': 'VREG-SO23-X-KAP2112K-01', 'FULL': {'DESC': '', 'PART': 'U2', 'DEVICE': 'SOT23-DBV AP2112K-3.3', 'PACKAGE': 'SOT23-DBV', 'PARTLETTER': 'U', 'VALUE': 'AP2112K-3.3', 'VALUENUMBER': '2112-3.3', 'PACKAGENUMBER': '23', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U2,AP2112K-3.3,SOT23-DBV AP2112K-3.3,SOT23-DBV,,,'}},
       'D1': {'OOMPID': 'DIOD-S123-X-KMBR120-01', 'FULL': {'DESC': '', 'PART': 'D1', 'DEVICE': 'SOD-123 MBR120', 'PACKAGE': 'SOD-123', 'PARTLETTER': 'D', 'VALUE': 'MBR120', 'VALUENUMBER': '120', 'PACKAGENUMBER': '123', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D1,MBR120,SOD-123 MBR120,SOD-123,,,'}},
       'X2': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X2', 'DEVICE': '2X05_1.27MM_BOX_POSTS 2x5 0.05 SWD', 'PACKAGE': '2X05_1.27MM_BOX_POSTS', 'PARTLETTER': 'X', 'VALUE': '2x5 0.05 SWD', 'VALUENUMBER': '25 0.05 ', 'PACKAGENUMBER': '205127', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X2,2x5 0.05 SWD,2X05_1.27MM_BOX_POSTS 2x5 0.05 SWD,2X05_1.27MM_BOX_POSTS,,,'}},
       'R1': {'OOMPID': 'RESA-06038-X-O1003X4-01', 'FULL': {'DESC': '', 'PART': 'R1', 'DEVICE': 'RESPACK_4X0603 100K', 'PACKAGE': 'RESPACK_4X0603', 'PARTLETTER': 'R', 'VALUE': '100K', 'VALUENUMBER': '100', 'PACKAGENUMBER': '40603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R1,100K,RESPACK_4X0603 100K,RESPACK_4X0603,,,'}},
       'R2': {'OOMPID': 'RESA-06038-X-O102X4-01', 'FULL': {'DESC': '', 'PART': 'R2', 'DEVICE': 'RESPACK_4X0603 1K', 'PACKAGE': 'RESPACK_4X0603', 'PARTLETTER': 'R', 'VALUE': '1K', 'VALUENUMBER': '1', 'PACKAGENUMBER': '40603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R2,1K,RESPACK_4X0603 1K,RESPACK_4X0603,,,'}},
       'FB2': {'OOMPID': 'FERB-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'FB2', 'DEVICE': '0805-NO FERRITE', 'PACKAGE': '0805-NO', 'PARTLETTER': 'FB', 'VALUE': 'FERRITE', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'FB2,FERRITE,0805-NO FERRITE,0805-NO,,,'}},
       'IOH0': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'IOH0', 'DEVICE': '1X10_OVALWAVE 20611', 'PACKAGE': '1X10_OVALWAVE', 'PARTLETTER': 'IOH', 'VALUE': '20611', 'VALUENUMBER': '20611', 'PACKAGENUMBER': '110', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'IOH0,20611,1X10_OVALWAVE 20611,1X10_OVALWAVE,,,'}}}]
