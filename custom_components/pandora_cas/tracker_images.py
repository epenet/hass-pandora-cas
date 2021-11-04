from collections import defaultdict
from typing import Final, Optional


def from_path(path: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        + '<svg version="1.1" width="512" height="512" xmlns="http://www.w3.org/2000/svg" '
        + 'xmlns:svg="http://www.w3.org/2000/svg"><path transform="rotate({rotation} 256 256)" '
        + 'style="fill:{fill};fill-opacity:1" d="'
        + path
        + '"/></svg>'
    )


class ImagesDefaultDict(defaultdict):
    def get_image(
        self,
        car_type: str,
        fill: Optional[str] = None,
        rotation: Optional[float] = None,
    ) -> str:
        base_code, base_rotation = self[car_type]
        return base_code.format(
            fill=(fill or "#000000"),
            rotation=(float(rotation or 0.0) - base_rotation) % 360,
        )


TRANSPORT_TYPE_CAR: Final = "car"
TRANSPORT_TYPE_MOTO: Final = "moto"
TRANSPORT_TYPE_TRUCK: Final = "truck"

TRANSPORT_TYPE_DEFAULT: Final = TRANSPORT_TYPE_CAR

IMAGE_REGISTRY: Final = ImagesDefaultDict(
    lambda: IMAGE_REGISTRY[TRANSPORT_TYPE_DEFAULT],
    {
        TRANSPORT_TYPE_CAR: (
            from_path(
                "m 217.13642,146.13435 c -0.0357,6e-4 -0.14981,0.0181 -0.24,0.02 -0.87778,0.0194 -3.99768,"
                "0.0945 -5.7,0.48 -1.90342,0.43104 -3.80556,1.01751 -5.48,2.02 -2.50472,1.49965 -4.61679,"
                "3.64138 -6.56,5.82 -1.62169,1.81818 -2.86241,3.94371 -4.2,5.98 -0.53772,0.81863 -1.23176,"
                "1.58394 -1.52,2.52 -0.0398,0.12911 -0.093,0.24477 -0.12,0.38 -31.25675,0.0882 -62.51305,"
                "0.31019 -93.759999,1.02 -18.762206,0.62707 -37.167472,10.05239 -47.439992,25.98 -4.401784,"
                "5.13425 -7.214072,11.19834 -8.48,17.76 -7.317976,19.75288 -4.191064,41.28355 -4.86,61.9 "
                "-0.621408,16.44047 2.831368,32.97476 10.28,47.6 8.660096,13.64969 21.606544,25.82672 "
                "38.159996,28.3 23.190605,4.82131 47.075915,2.08365 70.579995,2.88 11.85404,-0.0263 23.70564,"
                "-0.0182 35.56,-0.02 0.0203,0.0847 0.0548,0.15807 0.08,0.24 0.28824,0.93606 0.98228,1.70139 "
                "1.52,2.52 1.33759,2.03628 2.57831,4.16185 4.2,5.98 1.94321,2.17863 4.05528,4.32039 6.56,5.82 "
                "1.67444,1.00252 3.57658,1.58899 5.48,2.02 1.70232,0.38547 4.82222,0.46069 5.7,0.48 0.39521,"
                "0.0811 0.81989,0.0108 1.1,-0.2 0.28011,-0.21079 0.36846,-0.41857 0.44,-0.9 0.0715,-0.48141 "
                "-6e-4,-0.68937 -0.32,-1.9 -0.31915,-1.21063 -1.08197,-3.31953 -1.9,-5.24 -0.81803,-1.92046 "
                "-2.17583,-4.55649 -3.08,-6.22 -0.57813,-1.06366 -1.04799,-1.86772 -1.5,-2.6 15.42148,0.007 "
                "30.83838,0.007 46.26,0.02 0.0542,0.0712 0.11147,0.14771 0.18,0.22 0.35576,0.37523 0.87286,"
                "0.87216 1.86,1.22 0.98715,0.34784 1.03685,0.25022 4.04,0.4 3.00315,0.14979 10.61173,0.0969 "
                "12.84002,-0.04 2.22829,-0.13693 2.62509,-0.17186 3.72,-0.6 0.88435,-0.3458 1.54445,-0.51239 "
                "1.68,-1.18 23.49574,0.006 47.00493,-0.021 70.50003,-0.12 0.86375,0.29284 1.05882,0.21734 "
                "3.92,0.36 3.00288,0.14979 10.63168,0.0969 12.85997,-0.04 1.8375,-0.11291 2.43552,-0.16667 "
                "3.2,-0.42 19.41229,-0.12141 38.82912,-0.30509 58.24,-0.58 13.57414,0.032 27.06349,-8.42931 "
                "31.62003,-21.48 11.63763,-28.70999 11.42835,-60.54084 10.24,-91.04 -1.52,-19.91366 -4.08928,"
                "-40.86446 -14.88,-58.06 -9.66841,-13.69542 -28.30093,-14.09957 -43.48006,-14.04 -14.29447,"
                "-0.14953 -28.58432,-0.20843 -42.88,-0.24 -0.4857,-0.0644 -1.07834,-0.11966 -2.05997,-0.18 "
                "-2.22829,-0.13683 -9.85709,-0.18976 -12.85997,-0.04 -1.97113,0.0983 -2.63309,0.0978 -3.16006,"
                "0.18 -18.30637,-0.005 -36.61344,0.0394 -54.91994,0.04 -5.43936,0.0294 -10.88083,0.0422 "
                "-16.32006,0.06 -0.11418,-0.70563 -0.79635,-0.86663 -1.69997,-1.22 -1.09491,-0.42816 -1.49171,"
                "-0.4631 -3.72,-0.6 -2.22829,-0.13689 -9.83687,-0.18982 -12.84002,-0.04 -3.00315,0.14976 "
                "-3.05285,0.0522 -4.04,0.4 -0.98714,0.34784 -1.50424,0.84477 -1.86,1.22 -0.0889,0.0938 "
                "-0.17716,0.18699 -0.24,0.28 -15.42082,0.0197 -30.8389,0.0388 -46.26,0.06 0.47103,-0.75771 "
                "0.95512,-1.58712 1.56,-2.7 0.90417,-1.66355 2.26197,-4.29949 3.08,-6.22 0.81803,-1.92045 "
                "1.58085,-4.02937 1.9,-5.24 0.3194,-1.21069 0.39154,-1.41853 0.32,-1.9 -0.0715,-0.48141 "
                "-0.15989,-0.68925 -0.44,-0.9 -0.19148,-0.14425 -0.45165,-0.21013 -0.72,-0.22 -0.0456,-0.002 "
                "-0.0939,-0.002 -0.14,0 z m 52.58,17.08 c 0.56925,-0.006 1.21616,-0.006 1.84,0.02 -0.88726,"
                "0.002 -1.77272,-0.002 -2.66,0 0.28238,-0.011 0.57178,-0.0172 0.82,-0.02 z m 161.62002,7.32 c "
                "3.98362,-0.10006 8.47507,0.49707 10.90003,1.74 5.93658,3.04302 9.49709,7.73067 10.88,14.34 "
                "0.45127,2.15734 1.52666,5.29191 2.37997,6.98 2.53837,5.02162 4.8743,12.28169 4.66003,14.46 l "
                "-0.20006,2.02 -1.97997,-1.86 c -1.08813,-1.02017 -2.95002,-3.95264 -4.12,-6.52 -6.77248,"
                "-14.86119 -15.81574,-23.51737 -29.6,-28.36 -1.19942,-0.42138 -1.19046,-0.46785 -0.0602,-1.3 "
                "1.2583,-0.92616 4.04166,-1.42217 7.14003,-1.5 z m -214.34002,1.26 c 1.28877,-0.008 2.76232,"
                "-0.003 4.4,0 10.91785,0.021 29.10184,0.26157 48.16,0.66 l 13.59999,0.28 5.30003,8.32 c "
                "2.91123,4.56694 5.37677,8.74014 5.48,9.28 0.18515,0.96863 0.13594,0.96669 -4.10003,0.9 "
                "-2.3609,-0.0372 -8.51539,-0.213 -13.65997,-0.4 -14.53322,-0.52824 -36.94353,-2.85729 "
                "-51.10002,-5.3 l -5.66,-0.96 -1.82,-2.84 c -1.00208,-1.55534 -2.8663,-4.27453 -4.14,-6.06 "
                "-1.27368,-1.78547 -2.38732,-3.43261 -2.48,-3.66 -0.0463,-0.11365 2.15371,-0.19541 6.02,-0.22 "
                "z m -127.579995,0.46 c 1.03944,5e-5 2.21927,-0.006 3.559996,0 14.445959,0.0595 17.025159,"
                "1.16889 11.499999,4.9 -3.1921,2.15562 -23.743005,14.63843 -32.059991,19.48 -7.071624,4.11661 "
                "-9.857224,6.48779 -13.02,11.08 -1.273056,1.84842 -3.206832,3.77177 -4.32,4.3 -2.067376,"
                "0.98104 -5.291528,1.26847 -6.02,0.54 -0.2256,-0.2256 -0.42,-2.03475 -0.42,-4.02 0,-3.85553 "
                "1.171272,-6.73686 5.4,-13.4 3.47964,-5.48282 10.249448,-13.16521 14.26,-16.18 2.051664,"
                "-1.54227 6.009864,-3.7001 8.8,-4.78 4.407076,-1.70571 5.043876,-1.92031 12.319996,-1.92 z m "
                "217.499985,0.82 c 1.64902,-0.004 4.24409,0.059 8.26003,0.16 33.70726,0.84835 55.6313,1.59333 "
                "55.89997,1.88 0.45107,0.48013 1.70003,8.21307 1.70003,10.54 0,3.62553 0.2832,3.52308 "
                "-12.21997,4.18 -8.3664,0.43955 -40.07334,1.42795 -47.62003,1.48 -0.73446,0.005 -1.54112,"
                "-1.45207 -4.66003,-8.4 -2.07354,-4.61928 -3.91565,-8.75175 -4.08,-9.18 -0.17735,-0.46263 "
                "-0.0282,-0.65358 2.72,-0.66 z m 84.34003,4.84 c 0.72762,-0.0236 1.62912,0.0285 2.77997,0.12 "
                "4.51046,0.35861 15.21165,1.87641 15.80006,2.24 1.26336,0.78093 -5.23923,3.08808 -13.2,4.7 "
                "-5.92525,1.19971 -6.61395,1.27001 -8.08,0.68 -1.36211,-0.54802 -1.63193,-2.19514 -0.78003,"
                "-4.76 0.7241,-2.18021 1.29715,-2.90916 3.48,-2.98 z m -238.72002,3.74 c 1.92495,0 55.0127,"
                "11.67285 64.22,14.12 6.20751,1.64986 17.61444,5.50446 25.34,8.56 17.578,6.95228 26.56977,"
                "9.32 35.44002,9.32 6.75187,0 7.14182,0.17929 12.68,6.1 l 5.69997,6.1 0,30.24 0,30.26 -5.56,"
                "5.94 -5.53997,5.92 -10.76,0.64 c -8.48659,0.49582 -13.21812,1.58867 -22.44002,5.18 -22.9803,"
                "8.94935 -37.94438,13.3134 -65.84,19.26 -15.56638,3.31834 -29.53522,6.31725 -31.04,6.66 "
                "-2.20387,0.50201 -3.18789,-0.27063 -5.08,-4 -2.90944,-5.73456 -9.30603,-25.69652 -11.14,"
                "-34.78 -4.04471,-20.03301 -3.72723,-55.65604 0.64,-73.22 4.07268,-16.37935 11.41631,-36.3 "
                "13.38,-36.3 z m 285.20002,6.3 c 3.39469,-0.16631 4.42317,2.7662 8.12,9.7 10.05459,18.8585 "
                "13.09901,35.10049 12.16,65 -0.7367,23.45759 -2.7319,32.47286 -10.86003,49 -7.08256,14.40155 "
                "-7.26835,14.50003 -17.71994,9.52 -4.73773,-2.25733 -11.80845,-5.30076 -15.70003,-6.76 "
                "-3.89158,-1.45924 -7.08,-2.87539 -7.08,-3.14 0,-0.26461 1.92986,-4.29313 4.28,-8.96 7.37645,"
                "-14.64765 9.7945,-26.29157 9.72,-46.82 -0.0746,-20.54911 -2.2448,-30.75562 -9.68,-45.52 "
                "-2.45971,-4.88434 -4.29261,-9.02499 -4.08,-9.2 0.21267,-0.17501 7.53171,-3.42994 16.25997,"
                "-7.24 7.88019,-3.43972 11.93971,-5.45064 14.58003,-5.58 z m -387.220011,110.9 c 0.488216,"
                "-0.0427 1.092504,0.0414 1.84,0.22 3.658824,0.87423 4.193248,1.29611 7.28,5.54 3.662152,5.035 "
                "5.749016,6.70139 14.84,11.96 13.471746,7.79265 31.589331,19.14478 32.239991,20.2 1.39475,"
                "2.26194 -0.26505,2.64016 -12.719999,2.78 -10.283886,0.11546 -12.234546,-0.0221 -15.039996,"
                "-1.04 -9.37962,-3.40338 -16.845044,-9.75316 -23.879996,-20.32 -5.177544,-7.77691 -6.403456,"
                "-10.62042 -6.42,-14.86 -0.01216,-3.10701 0.395344,-4.35201 1.86,-4.48 z m 409.439981,3.22 "
                "0.18003,1.84 c 0.21709,2.13231 -2.36992,10.22075 -4.56,14.22 -0.81773,1.49331 -1.90208,"
                "4.67187 -2.4,7.06 -2.11981,10.16655 -9.97318,16.47352 -20.26003,16.3 -2.05351,-0.0346 "
                "-4.57319,-0.25391 -5.6,-0.5 -1.02669,-0.24609 -2.40218,-0.75186 -3.05997,-1.12 -1.11949,"
                "-0.62647 -1.07507,-0.7076 0.64,-1.4 7.98688,-3.22453 12.3808,-5.8991 16.6,-10.06 5.0361,"
                "-4.96646 8.20346,-9.57455 12.29997,-17.94 1.55609,-3.17773 3.56461,-6.37662 4.48,-7.1 l 1.68,"
                "-1.3 z m -147.92,18.66 8.72,0.1 c 10.58528,0.11951 31.39923,0.84934 42.66003,1.48 6.70989,"
                "0.3758 8.35859,0.59064 8.8,1.16 0.75008,0.96743 0.67104,4.78806 -0.21997,9.44 l -0.76006,3.9 "
                "-1.95994,0.3 c -1.89913,0.28723 -24.57369,0.96055 -51.92,1.54 -9.47449,0.20075 -13.39897,"
                "0.14826 -13.28,-0.18 0.0927,-0.25608 1.91987,-4.35166 4.05997,-9.1 l 3.89997,-8.64 z m -25.76,"
                "0.18 c 4.69472,-0.008 7.74003,0.17931 7.74003,0.62 0,0.57002 -9.58381,16.05708 -10.62003,"
                "17.16 -0.51059,0.54346 -11.65154,0.83563 -60.17999,1.56 l -12.7,0.2 1.78,-2.46 c 0.9853,"
                "-1.35083 2.97553,-4.28071 4.42,-6.5 1.60182,-2.46103 2.9892,-4.11686 3.54,-4.24 4.92828,"
                "-1.1018 23.75501,-3.61132 35.48,-4.74 10.33749,-0.99511 22.71554,-1.58634 30.53999,-1.6 z m "
                "104.58003,5.28 c 1.80902,0.0252 4.37696,0.46624 7.88,1.26 8.77434,1.98822 13.20595,3.94811 "
                "10.28,4.56 -2.82042,0.58983 -11.11066,1.60575 -15.22003,1.86 l -4.41997,0.26 -0.88,-1.44 c "
                "-0.48224,-0.79289 -1.00243,-2.20768 -1.16,-3.14 -0.39418,-2.3334 0.50496,-3.40202 3.52,-3.36 z"
            ),
            -90,
        ),
        TRANSPORT_TYPE_MOTO: (
            from_path(
                "m 166.45839,357.80288 c -12.12657,-5.98218 -18.97322,-18.13056 -13.95378,-24.75899 2.00481,"
                "-2.64746 2.04448,-3.47629 0.49849,-10.4145 -2.04796,-9.19091 -4.18095,-9.9973 -3.19028,"
                "-1.20609 0.91583,8.12704 -1.66807,14.82192 -6.04333,15.6583 -6.17126,1.17971 -12.53174,"
                "-11.82675 -7.99981,-16.35869 1.99505,-1.99504 1.61304,-5.68001 -0.50458,-4.8674 -5.43876,"
                "2.08705 -18.55806,-10.10204 -30.67983,-28.50451 -9.136305,-13.87013 -9.136305,-13.87013 "
                "-18.157173,-13.51018 -6.038693,0.24095 -10.424608,-0.23705 -13.267085,-1.44591 -2.540925,"
                "-1.08061 -9.202446,-1.9685 -16.587351,-2.21086 -13.714286,-0.45008 -14.532153,-0.91071 "
                "-17.153796,-9.66099 -1.00582,-3.3571 -1.00582,-5.70414 0,-9.06124 2.621643,-8.75029 3.43951,"
                "-9.21091 17.153796,-9.66099 7.384905,-0.24236 14.046426,-1.13025 16.587351,-2.21086 2.842477,"
                "-1.20887 7.228392,-1.68686 13.267085,-1.44591 9.020868,0.35995 9.020868,0.35995 18.157173,"
                "-13.51018 12.12177,-18.40246 25.24107,-30.59155 30.67983,-28.5045 2.11762,0.81261 2.49963,"
                "-2.87236 0.50458,-4.86741 -4.53193,-4.53193 1.82855,-17.5384 7.99981,-16.35869 4.37526,"
                "0.83638 6.95916,7.53127 6.04333,15.65831 -0.99067,8.79121 1.14232,7.98482 3.19028,-1.2061 "
                "1.54599,-6.9382 1.50632,-7.76703 -0.49849,-10.41449 -5.06009,-6.6821 1.99135,-19.03515 "
                "14.16266,-24.81081 6.83992,-3.24576 8.18142,-2.6302 7.4972,3.44019 -0.84243,7.47401 -10.53807,"
                "26.76487 -13.22747,26.31793 -1.5136,-0.25154 -2.40128,1.01686 -3.37632,4.82439 -0.72756,"
                "2.84112 -1.55038,5.84409 -1.82848,6.67328 -1.51636,4.52112 22.88526,1.70625 25.37702,-2.92738 "
                "2.78313,-5.17549 3.38539,-19.75551 0.85093,-20.60033 -2.89873,-0.96625 -1.77507,-6.53273 "
                "1.23248,-6.10559 5.03637,0.71528 6.77995,26.11785 2.17364,31.66812 -2.01772,2.4312 -2.45527,"
                "10.04884 -0.66265,11.53659 1.10452,0.91667 1.35449,0.53971 0.99456,-1.49987 -0.45186,-2.56053 "
                "5.54356,-13.302 7.29722,-13.07379 0.41283,0.0537 1.27434,0.0977 1.91448,0.0977 0.64014,0 "
                "3.91653,-5.10616 7.28089,-11.34702 7.29966,-13.54085 8.58325,-14.85279 12.69766,-12.97814 "
                "4.25196,1.93733 3.79815,4.64624 -3.07178,18.33618 -6.19699,12.34893 -6.48996,18.99606 "
                "-0.85278,19.34834 2.72249,0.17014 5.05345,0.84824 12.1736,3.54146 5.82844,2.20462 7.25817,"
                "2.38645 8.09517,1.02951 2.27191,-3.6833 26.62596,-2.9435 37.72519,1.14598 16.34431,6.02203 "
                "30.58336,8.02249 40.57363,5.70025 1.65838,-0.38549 6.00033,-0.9743 9.64878,-1.30846 3.64844,"
                "-0.33416 7.99041,-0.86777 9.64878,-1.18578 10.36676,-1.98796 59.41462,-3.13681 66.33543,"
                "-1.55378 1.65838,0.37932 5.4576,1.08336 8.44269,1.56451 5.06784,0.81686 15.93453,3.39397 "
                "20.73332,4.91705 1.87293,0.59445 1.96037,0.25276 0.79262,-3.09708 -4.71881,-13.53635 6.75162,"
                "-24.11928 13.27992,-12.2524 2.87554,5.22708 2.87554,5.22708 -0.40866,11.93429 -3.28419,"
                "6.70721 -3.28419,6.70721 0.37645,9.5721 9.03907,7.07414 9.03907,49.2139 0,56.28804 -3.66064,"
                "2.86488 -3.66064,2.86488 -0.37645,9.57209 3.2842,6.70721 3.2842,6.70721 0.40866,11.93429 "
                "-6.5283,11.86688 -17.99873,1.28397 -13.27992,-12.2524 1.16775,-3.34984 1.08031,-3.69153 "
                "-0.79262,-3.09708 -4.79879,1.52309 -15.66548,4.10019 -20.73332,4.91705 -2.98509,0.48116 "
                "-6.78431,1.18519 -8.44269,1.56452 -6.92081,1.58303 -55.96867,0.43418 -66.33543,-1.55378 "
                "-1.65837,-0.31802 -6.00034,-0.85162 -9.64878,-1.18578 -3.64845,-0.33416 -7.9904,-0.92297 "
                "-9.64878,-1.30846 -9.99027,-2.32225 -24.22932,-0.32178 -40.57363,5.70025 -11.09923,4.08947 "
                "-35.45328,4.82928 -37.72519,1.14598 -0.837,-1.35694 -2.26673,-1.17512 -8.09517,1.02951 "
                "-7.12015,2.69322 -9.45111,3.37133 -12.1736,3.54146 -5.63718,0.35228 -5.34421,6.99941 0.85278,"
                "19.34834 6.86993,13.68994 7.32374,16.39885 3.07178,18.3362 -4.11441,1.87465 -5.398,0.5627 "
                "-12.69766,-12.97815 -3.36436,-6.24086 -6.64075,-11.34703 -7.28089,-11.34703 -0.64014,0 "
                "-1.50165,0.0439 -1.91448,0.0977 -1.75366,0.2282 -7.74908,-10.51326 -7.29721,-13.07378 0.35992,"
                "-2.03959 0.10999,-2.41656 -0.99457,-1.49988 -1.79262,1.48774 -1.35507,9.10539 0.66265,"
                "11.53659 4.60631,5.55027 2.86273,30.95285 -2.17364,31.66813 -3.00755,0.42713 -4.13121,"
                "-5.13934 -1.23248,-6.1056 2.53446,-0.84481 1.9322,-15.42485 -0.85093,-20.60034 -2.49176,"
                "-4.63362 -26.89338,-7.44849 -25.37702,-2.92738 0.2781,0.8292 1.10092,3.83218 1.82848,6.67329 "
                "0.97504,3.80753 1.86272,5.07594 3.37632,4.82439 2.6894,-0.44694 12.38504,18.84392 13.22747,"
                "26.31794 0.68334,6.06255 -0.8862,6.75268 -7.70608,3.38837 z m 3.24784,-9.24235 c -0.5853,"
                "-1.49255 -2.20098,-5.15608 -3.59038,-8.14118 -3.10106,-6.66253 -1.99847,-1.84899 1.26787,"
                "5.53515 2.40777,5.44315 4.24236,7.50169 2.32251,2.60603 z m 12.66296,-47.90297 c 0.64165,"
                "-0.64164 3.32538,-1.61514 5.96382,-2.16334 2.94771,-0.61243 4.94427,-1.76046 5.1787,-2.97774 "
                "0.33034,-1.71536 -0.15402,-1.80975 -3.61192,-0.70386 -6.6895,2.13939 -11.79912,4.88465 "
                "-11.12418,5.97672 0.83976,1.35878 2.15113,1.31069 3.59358,-0.13178 z m 5.93023,-12.90197 c "
                "-1.15813,-1.76754 -4.20565,-5.21134 -6.77225,-7.65289 -7.26491,-6.91094 -7.26491,-41.30958 0,"
                "-48.22052 6.03277,-5.73884 9.52082,-10.9174 7.23162,-10.7365 -18.71667,1.47909 -18.71667,"
                "68.21443 0,69.69352 1.26027,0.0996 1.15254,-0.62353 -0.45937,-3.08361 z M 98.561445,265.64624 "
                "c -1.380187,-3.98816 -2.509431,-8.33237 -2.509431,-9.6538 0,-1.32143 1.129244,-5.66564 "
                "2.509431,-9.6538 3.176945,-9.18006 2.542035,-11.37435 -1.332904,-4.60657 -4.284687,7.48342 "
                "-4.284687,21.03732 0,28.52074 3.874939,6.76778 4.509849,4.57349 1.332904,-4.60657 z m "
                "-47.135078,0.61317 c 0,-0.98671 -2.170978,-3.1645 -4.824394,-4.83953 -6.265048,-3.95495 "
                "-6.265048,-6.89993 0,-10.85488 2.653416,-1.67503 4.824394,-3.86533 4.824394,-4.86733 0,"
                "-1.54702 -0.492303,-1.49925 -3.263729,0.31665 -1.79505,1.17617 -3.558969,2.00279 -3.919821,"
                "1.83696 -0.360849,-0.16584 -0.656091,0.26101 -0.656091,0.94856 0,0.68755 -0.768888,1.72529 "
                "-1.70864,2.30609 -2.214271,1.36849 -2.214271,8.40453 0,9.77302 0.939752,0.5808 1.70864,"
                "1.70248 1.70864,2.49264 0,0.79015 1.020738,1.58645 2.268308,1.76955 1.247569,0.1831 2.848665,"
                "0.91328 3.557991,1.6226 1.707321,1.70733 2.013342,1.63067 2.013342,-0.50433 z m 8.849268,"
                "0.0619 c 0.448224,-1.16805 -1.473493,-2.93877 -5.901454,-5.43776 -3.61136,-2.03812 -6.56611,"
                "-4.23914 -6.56611,-4.89115 0,-0.65201 2.95475,-2.85304 6.56611,-4.89116 4.427961,-2.49899 "
                "6.349678,-4.26971 5.901454,-5.43776 -0.785639,-2.04735 -2.357433,-2.24819 -3.472642,-0.44375 "
                "-0.437925,0.70858 -1.583634,0.98617 -2.54602,0.61687 -0.962386,-0.36931 -1.433991,-0.16049 "
                "-1.048013,0.46404 0.385976,0.62453 -1.476114,2.38223 -4.137977,3.90601 -7.70596,4.41125 "
                "-7.70596,7.16024 0,11.5715 2.661863,1.52377 4.523953,3.28148 4.137977,3.906 -0.385978,"
                "0.62453 0.08563,0.83335 1.048013,0.46404 0.962386,-0.3693 2.108095,-0.0917 2.54602,0.61687 "
                "1.115209,1.80445 2.687003,1.6036 3.472642,-0.44375 z m 3.814766,0.52597 c -0.409976,-0.66335 "
                "-1.288153,-1.2061 -1.951508,-1.2061 -0.663354,0 -0.870665,0.54275 -0.46069,1.2061 0.409978,"
                "0.66336 1.288155,1.2061 1.951509,1.2061 0.663355,0 0.870666,-0.54274 0.460689,-1.2061 z m "
                "2.388668,-2.71372 c -0.434022,-1.49255 -1.963144,-3.73579 -3.398047,-4.98499 -2.608917,"
                "-2.27127 -2.608917,-2.27127 0.104799,-1.42635 2.230627,0.69451 2.713722,0.38657 2.713722,"
                "-1.72982 0,-2.1164 -0.483095,-2.42434 -2.713722,-1.72983 -2.713722,0.84493 -2.713722,0.84493 "
                "-0.104818,-1.42634 10.334302,-8.99684 3.595578,-8.00439 -12.850707,1.89259 -2.235059,1.34501 "
                "-2.381103,1.21148 7.829595,7.1585 9.962506,5.80247 9.410458,5.65518 8.419162,2.24624 z m "
                "-2.388668,-18.99605 c 0.409977,-0.66335 0.202666,-1.2061 -0.460689,-1.2061 -0.663354,0 "
                "-1.541531,0.54275 -1.951509,1.2061 -0.409975,0.66335 -0.202664,1.2061 0.46069,1.2061 "
                "0.663355,0 1.541532,-0.54275 1.951508,-1.2061 z M 193.3298,215.64015 c -0.39281,-1.02364 "
                "-1.9524,-1.86451 -3.46578,-1.8686 -1.51336,-0.004 -4.33678,-0.83408 -6.27425,-1.84445 "
                "-1.95632,-1.02019 -3.98224,-1.37746 -4.55621,-0.8035 -1.05789,1.0579 3.99193,3.91422 "
                "10.49109,5.93404 4.2215,1.31197 4.77362,1.1063 3.80515,-1.41749 z m -23.62357,-52.21578 c "
                "1.91985,-4.89568 0.0853,-2.83712 -2.32251,2.60603 -3.26634,7.38412 -4.36893,12.19766 "
                "-1.26787,5.53514 1.3894,-2.9851 3.00508,-6.64862 3.59038,-8.14117 z m 274.34886,116.76066 c "
                "-0.43399,-0.70219 -0.50002,-1.74438 -0.14681,-2.31598 1.78985,-2.89606 2.92204,-22.61653 "
                "1.82722,-31.82692 -0.65054,-5.47268 -1.30458,-11.03581 -1.45344,-12.36251 -0.31093,-2.771 "
                "4.10143,-2.9241 13.28721,-0.46105 21.02031,5.63635 21.02031,40.09255 0,45.48947 -9.40066,"
                "2.4136 -12.71172,2.77547 -13.51423,1.47699 z"
            ),
            -90,
        ),
        TRANSPORT_TYPE_TRUCK: (
            from_path(
                "m 311,341.3273 c -2.93395,-1.09019 -4,-3.76024 -4,-10.01843 0,-6.47655 0.77489,"
                "-8.002 5.58775,-11.00006 1.84931,-1.15199 1.8433,-1.19313 -0.18276,-1.25 -4.15299,"
                "-0.11658 -5.67313,-3.30755 -5.23866,-10.99663 0.21834,-3.86402 0.96644,-7.59624 "
                "1.66245,-8.29383 0.86673,-0.8687 5.66201,-1.37094 15.21835,-1.59393 C 337.03787,"
                "297.87128 338,297.71613 338,295.92442 338,294.13211 337.17623,294 326,294 h -12 v "
                "-2.5 -2.5 h 12 c 10,0 12,-0.25 12,-1.5 0,-1.27531 -2.58388,-1.50018 -17.25,"
                "-1.50123 l -17.25,-10e-4 0.31329,18.63793 c 0.17345,10.31835 -0.0924,19.04358 "
                "-0.59545,19.54668 -0.51236,0.51236 -17.1006,0.90875 -38.0292,0.90875 h -37.12046 l"
                " 0.58971,2.94855 C 229.87251,334.11256 224.93462,340 218.62639,340 c -1.36012,0 "
                "-3.85747,-1.165 -5.54966,-2.58889 C 210.63355,335.35531 210,334.03854 210,"
                "331.01642 v -3.8058 l -3.75,0.87083 c -2.0625,0.47896 -17.36071,0.88157 -33.99602,"
                "0.89469 -28.3043,0.0223 -30.64412,0.16163 -36.44722,2.16991 -5.63234,1.94919 "
                "-8.20955,2.14081 -28.09434,2.08885 -21.054925,-0.055 -22.224688,-0.16276 "
                "-30.55278,-2.81395 C 69.502366,327.98331 67.863367,327.0145 63,322.05117 "
                "56.701253,315.62296 49.070316,304.57956 45.424616,296.61631 c -8.962454,-19.57658 "
                "-8.962454,-61.65604 0,-81.23262 3.6457,-7.96325 11.276637,-19.00665 17.575384,"
                "-25.43486 4.863367,-4.96333 6.502366,-5.93214 14.15964,-8.36978 8.328092,-2.65119 "
                "9.497855,-2.75893 30.55278,-2.81395 19.88479,-0.052 22.462,0.13966 28.09434,"
                "2.08885 5.8031,2.00828 8.14292,2.14758 36.44722,2.16991 16.63531,0.0131 31.93352,"
                "0.41573 33.99602,0.89469 l 3.75,0.87083 v -3.8058 c 0,-3.02212 0.63355,-4.33889 "
                "3.07673,-6.39469 C 214.76892,173.165 217.26627,172 218.62639,172 c 6.30823,0 "
                "11.24612,5.88744 10.0315,11.96054 l -0.58971,2.94855 h 37.12046 c 20.9286,0 "
                "37.51684,0.39639 38.0292,0.90875 0.5031,0.5031 0.7689,9.22833 0.59545,19.54668 l "
                "-0.31329,18.63793 17.25,-0.001 c 14.66612,-0.001 17.25,-0.22592 17.25,-1.50123 0,"
                "-1.25 -2,-1.5 -12,-1.5 h -12 v -2.5 -2.5 h 12 c 11.17623,0 12,-0.13211 12,"
                "-1.92442 0,-1.79171 -0.96213,-1.94686 -13.95287,-2.25 -9.55634,-0.22299 -14.35162,"
                "-0.72523 -15.21835,-1.59393 -0.69601,-0.69759 -1.44411,-4.42981 -1.66245,-8.29383 "
                "-0.43447,-7.68908 1.08567,-10.88005 5.23866,-10.99663 2.02606,-0.0569 2.03207,"
                "-0.098 0.18276,-1.25 C 307.77489,188.69313 307,187.16768 307,180.69113 307,"
                "169.85845 304.82817,170.5 341.5,170.5 c 36.67183,0 34.5,-0.64155 34.5,10.19113 "
                "0,6.47655 -0.77489,8.002 -5.58775,11.00006 -1.84931,1.15199 -1.8433,1.19313 "
                "0.18276,1.25 4.15299,0.11658 5.67313,3.30755 5.23866,10.99663 -0.21834,3.86402 "
                "-0.96644,7.59624 -1.66245,8.29383 -0.86673,0.8687 -5.66201,1.37094 -15.21835,"
                "1.59393 C 345.96213,214.12872 345,214.28387 345,216.07558 345,217.86789 345.82377,"
                "218 357,218 h 12 v 2.5 2.5 h -12 c -10,0 -12,0.25 -12,1.5 0,1.30348 4.38889,1.5 "
                "33.5,1.5 29.11111,0 33.5,-0.19652 33.5,-1.5 0,-1.25 -2,-1.5 -12,-1.5 h -12 v -2.5 "
                "-2.5 h 12 c 11.17623,0 12,-0.13211 12,-1.92442 0,-1.79171 -0.96213,-1.94686 "
                "-13.95287,-2.25 -9.55634,-0.22299 -14.35162,-0.72523 -15.21835,-1.59393 -0.69601,"
                "-0.69759 -1.44411,-4.42981 -1.66245,-8.29383 -0.43447,-7.68908 1.08567,-10.88005 "
                "5.23866,-10.99663 2.02606,-0.0569 2.03207,-0.098 0.18276,-1.25 C 381.77489,"
                "188.69313 381,187.16768 381,180.69113 381,169.85845 378.82817,170.5 415.5,170.5 c "
                "36.67183,0 34.5,-0.64155 34.5,10.19113 0,6.47655 -0.77489,8.002 -5.58775,11.00006 "
                "-1.84931,1.15199 -1.8433,1.19313 0.18276,1.25 4.15299,0.11658 5.67313,3.30755 "
                "5.23866,10.99663 -0.21834,3.86402 -0.96644,7.59624 -1.66245,8.29383 -0.86673,"
                "0.8687 -5.66201,1.37094 -15.21835,1.59393 C 419.96213,214.12872 419,214.28387 "
                "419,216.07558 419,217.86789 419.82377,218 431,218 h 12 v 2.5 2.5 h -12 c -10,0 "
                "-12,0.25 -12,1.5 0,1.27233 2.48813,1.5 16.39315,1.5 h 16.39315 l 1.10943,-6.25 c "
                "0.61018,-3.4375 2.03735,-13.675 3.17149,-22.75 1.93551,-15.48731 2.22688,"
                "-16.63779 4.74742,-18.74503 2.65935,-2.22329 7.18536,-3.08207 7.18536,-1.36338 "
                "0,0.49038 1.125,1.17395 2.5,1.51905 l 2.5,0.62746 V 192.5 205.9619 l -2.5,0.62746 "
                "-2.5,0.62746 V 256 304.78318 l 2.5,0.62746 2.5,0.62746 V 319.5 332.9619 l "
                "-2.5,0.62746 c -1.375,0.3451 -2.5,1.02867 -2.5,1.51905 0,1.71869 -4.52601,0.85991 "
                "-7.18536,-1.36338 -2.52054,-2.10724 -2.81191,-3.25772 -4.74742,-18.74503 -1.13414,"
                "-9.075 -2.56131,-19.3125 -3.17149,-22.75 L 451.7863,286 H 435.39315 C 421.48813,"
                "286 419,286.22767 419,287.5 c 0,1.25 2,1.5 12,1.5 h 12 v 2.5 2.5 h -12 c "
                "-11.17623,0 -12,0.13211 -12,1.92442 0,1.79171 0.96213,1.94686 13.95287,2.25 "
                "9.55634,0.22299 14.35162,0.72523 15.21835,1.59393 0.69601,0.69759 1.44411,4.42981 "
                "1.66245,8.29383 0.43447,7.68908 -1.08567,10.88005 -5.23866,10.99663 -2.02606,"
                "0.0569 -2.03207,0.098 -0.18276,1.25 4.81286,2.99806 5.58775,4.52351 5.58775,"
                "11.00006 0,10.83268 2.17183,10.19113 -34.5,10.19113 -36.67183,0 -34.5,0.64155 "
                "-34.5,-10.19113 0,-6.47655 0.77489,-8.002 5.58775,-11.00006 1.84931,-1.15199 "
                "1.8433,-1.19313 -0.18276,-1.25 -4.15299,-0.11658 -5.67313,-3.30755 -5.23866,"
                "-10.99663 0.21834,-3.86402 0.96644,-7.59624 1.66245,-8.29383 0.86673,-0.8687 "
                "5.66201,-1.37094 15.21835,-1.59393 C 411.03787,297.87128 412,297.71613 412,"
                "295.92442 412,294.13211 411.17623,294 400,294 h -12 v -2.5 -2.5 h 12 c 10,0 12,"
                "-0.25 12,-1.5 0,-1.30348 -4.38889,-1.5 -33.5,-1.5 -29.11111,0 -33.5,0.19652 -33.5,"
                "1.5 0,1.25 2,1.5 12,1.5 h 12 v 2.5 2.5 h -12 c -11.17623,0 -12,0.13211 -12,"
                "1.92442 0,1.79171 0.96213,1.94686 13.95287,2.25 9.55634,0.22299 14.35162,0.72523 "
                "15.21835,1.59393 0.69601,0.69759 1.44411,4.42981 1.66245,8.29383 0.43447,7.68908 "
                "-1.08567,10.88005 -5.23866,10.99663 -2.02606,0.0569 -2.03207,0.098 -0.18276,1.25 "
                "4.81286,2.99806 5.58775,4.52351 5.58775,11.00006 0,10.77727 1.96968,10.16065 "
                "-33.16834,10.38346 C 326.14925,341.79812 311.825,341.63385 311,341.3273 Z m "
                "-86.58889,-6.40403 c 3.13061,-3.72052 3.24713,-5.81673 0.51631,-9.28841 C "
                "222.33043,322.33332 216.97766,322.02234 214,325 c -2.97766,2.97766 -2.66668,"
                "8.33043 0.63486,10.92742 3.71065,2.9188 6.73685,2.60797 9.77625,-1.00415 z m "
                "-9.75612,-0.75201 C 212.42969,331.71233 212.5682,328.4318 215,326 c 2.40261,"
                "-2.40261 4.78621,-2.53847 7.77749,-0.4433 2.58184,1.8084 3.02042,6.78824 0.79394,"
                "9.01473 -2.00162,2.00162 -6.94357,1.77983 -8.91644,-0.40017 z m 6.76322,-0.77825 c"
                " 1.98211,-0.7606 2.06356,-4.74828 0.12978,-6.35318 -3.26945,-2.71341 -8.22157,"
                "2.23871 -5.50816,5.50816 1.29632,1.56198 2.86695,1.80875 5.37838,0.84502 z m "
                "4.81407,-33.14443 0.26772,-14.25142 -3.20541,10e-4 -3.20541,0.001 -0.29459,"
                "17.30728 c -0.27908,16.39617 -0.19462,17.31475 1.60449,17.44908 1.0445,0.078 "
                "2.3945,0.64157 3,1.25239 1.27939,1.29063 1.43483,-0.5544 1.8332,-21.76017 z M "
                "66.105304,317.25 C 63.716602,312.62155 53,298.43011 53,299.89532 53,302.03918 "
                "66.153548,321 67.640786,321 c 0.219924,0 -0.471043,-1.6875 -1.535482,-3.75 z m "
                "89.467346,-4.5352 c 8.19779,-4.15705 8.7655,-5.23683 8.11287,-15.43051 -0.30931,"
                "-4.83136 -1.06304,-12.38429 -1.67495,-16.78429 -1.4333,-10.30637 -1.4333,-38.69363"
                " 0,-49 0.61191,-4.4 1.36564,-11.95293 1.67495,-16.78429 0.49102,-7.66943 0.32456,"
                "-9.04748 -1.31156,-10.85808 -3.66605,-4.05701 -11.28915,-7.04094 -19.40948,"
                "-7.59752 l -7.68082,-0.52645 -0.68858,2.74352 c -0.37872,1.50894 -1.51397,4.60636 "
                "-2.52278,6.88317 -1.00882,2.27681 -2.36833,6.71948 -3.02115,9.8726 -0.65282,"
                "3.15312 -1.56212,5.96481 -2.02065,6.2482 -0.45854,0.28339 -1.13466,3.32857 "
                "-1.50248,6.76706 -0.36782,3.43848 -1.27817,10.07679 -2.02299,14.75179 -0.74482,"
                "4.675 -1.35422,10.525 -1.35422,13 0,2.475 0.6094,8.325 1.35422,13 0.74482,4.675 "
                "1.65517,11.31331 2.02299,14.75179 0.36782,3.43849 1.04394,6.48367 1.50248,6.76706 "
                "0.45853,0.28339 1.36783,3.09508 2.02065,6.2482 0.65282,3.15312 2.01233,7.59579 "
                "3.02115,9.8726 1.00881,2.27681 2.14406,5.37423 2.52278,6.88317 l 0.68858,2.74352 "
                "7.68082,-0.52645 c 5.41803,-0.37136 9.13243,-1.26256 12.60817,-3.02509 z M 256.25,"
                "286.2596 c -3.4375,-0.19527 -9.0625,-0.19527 -12.5,0 -3.4375,0.19527 -0.625,"
                "0.35504 6.25,0.35504 6.875,0 9.6875,-0.15977 6.25,-0.35504 z m 31.04159,0.001 c "
                "-3.41463,-0.19467 -9.26463,-0.19611 -13,-0.003 -3.73538,0.19293 -0.94159,0.35221 "
                "6.20841,0.35396 7.15,0.002 10.20621,-0.1561 6.79159,-0.35078 z M 262,268.92385 v "
                "-10.07614 l -7.75,0.46133 c -4.2625,0.25373 -13.6,1.76021 -20.75,3.34772 l -13,"
                "2.88638 -0.29569,6.72843 L 219.90862,279 H 240.95431 262 Z m 42,0.0761 v -10 h -16"
                " -16 v 10 10 h 16 16 z m 34,3.18856 c 0,-6.91891 -0.38414,-7.76665 -5.40979,"
                "-11.93856 -0.95988,-0.79682 -4.784,-1.25 -10.548,-1.25 L 313,259 v 10 10 h 12.5 "
                "12.5 v -6.81144 z m 16.77957,-0.89286 c -4.23737,-4.23737 -8.03062,-7.37798 "
                "-8.42946,-6.97914 -0.77962,0.77962 -1.33137,12.68923 -0.64551,13.93344 0.22739,"
                "0.4125 4.09575,0.75 8.59635,0.75 h 8.18292 z M 370.67792,269 l -0.0311,-10 h "
                "-9.32338 C 353.53887,259 352,259.25777 352,260.56171 352,262.09574 368.45311,279 "
                "369.94619,279 c 0.41959,0 0.74886,-4.5 0.73173,-10 z m 25.82193,0.57676 C "
                "401.72493,264.39397 406,259.87768 406,259.54055 c 0,-0.33714 -4.3735,-0.48418 "
                "-9.71888,-0.32676 l -9.71888,0.28621 -0.10921,9.75 c -0.0601,5.3625 0.0384,9.75 "
                "0.21873,9.75 0.18037,0 4.60301,-4.24046 9.82809,-9.42324 z M 411.75788,272 c "
                "0.42165,-10.62798 -0.47233,-10.73715 -9.98321,-1.21909 l -8.27467,8.28091 9,"
                "-0.28091 9,-0.28091 z m 17.56033,3.57347 c -0.71765,-4.42235 3.19416,-8.88234 "
                "7.15987,-8.16322 L 439,267.86756 V 256 244.13244 l -2.52192,0.45731 c -3.96571,"
                "0.71912 -7.87752,-3.74087 -7.15987,-8.16322 L 429.87426,233 H 424.43713 419 v "
                "6.06574 c 0,7.32372 0.96561,9.34958 5.47674,11.49025 3.66536,1.73932 5.04196,"
                "4.23436 4.05389,7.34751 -0.33228,1.04693 -2.15653,2.64016 -4.05389,3.54051 C "
                "419.96561,263.58468 419,265.61054 419,272.93426 V 279 h 5.43713 5.43713 z M 455,"
                "256 v -23 h -3 -3 v 23 23 h 3 3 z m -275.5,18 c 0,-1.56144 -0.646,-2.59702 "
                "-1.75302,-2.81021 -1.97949,-0.38122 -3.26679,2.01323 -2.35699,4.38412 0.95373,"
                "2.4854 4.11001,1.27672 4.11001,-1.57391 z m 0.31822,-17.45908 c 0.35755,-4.27462 "
                "-0.68249,-5.91397 -3.151,-4.96671 -2.0112,0.77177 -2.35474,7.98411 -0.41722,"
                "8.75912 2.36422,0.94569 3.25072,0.004 3.56822,-3.79241 z M 262,243 v -10 h "
                "-21.04569 -21.04569 l 0.29569,6.72843 0.29569,6.72843 12.75423,2.60913 c 7.01482,"
                "1.43502 13.05232,2.90723 13.41666,3.27157 0.36435,0.36434 3.96244,0.66244 7.99578,"
                "0.66244 H 262 Z m 42,0 v -10 h -16 -16 v 10 10 h 16 16 z m 28.59021,8.75 C "
                "337.61586,247.57809 338,246.73035 338,239.81144 V 233 H 325.5 313 v 10 10 h "
                "9.04221 c 5.764,0 9.58812,-0.45318 10.548,-1.25 z M 370.67792,243 c 0.0171,-5.5 "
                "-0.31214,-10 -0.73173,-10 C 368.45311,233 352,249.90426 352,251.43829 352,"
                "252.74223 353.53887,253 361.32339,253 h 9.32338 l 0.0311,-10 z M 406,252.42324 C "
                "406,251.83077 387.26134,233 386.67176,233 c -0.28394,0 -0.0716,19.07799 0.21983,"
                "19.75 C 387.12485,253.2879 406,252.96514 406,252.42324 Z m 5.54002,-5.72669 c "
                "0.31797,-1.26689 0.43905,-4.75439 0.26906,-7.75 L 411.5,233.5 l -9,-0.28628 -9,"
                "-0.28627 7.97654,8.03627 c 4.3871,4.41996 8.31602,8.03628 8.73095,8.03628 0.41492,"
                "0 1.01456,-1.03655 1.33253,-2.30345 z m -56.51499,-6.23463 7.47497,-7.53808 -8.5,"
                "0.28808 -8.5,0.28808 -0.0489,6 c -0.0513,6.29671 0.3196,8.5 1.43092,8.5 0.36742,"
                "0 4.03177,-3.39214 8.14301,-7.53808 z M 179.5,238 c 0,-2.85063 -3.15628,-4.05931 "
                "-4.11001,-1.57391 -0.9098,2.37089 0.3775,4.76534 2.35699,4.38412 C 178.854,"
                "240.59702 179.5,239.56144 179.5,238 Z m 47.10699,-13.58179 C 226.27314,223.54823 "
                "226,215.24992 226,205.97752 v -16.85891 l -2.6783,1.38951 c -1.47306,0.76424 "
                "-2.93556,1.22975 -3.25,1.03448 -0.31443,-0.19528 -0.43914,7.47775 -0.27711,"
                "17.05117 L 220.08918,226 h 3.5624 c 2.8376,0 3.4389,-0.32183 2.95541,-1.58179 z M "
                "256.25,225.2596 c -3.4375,-0.19527 -9.0625,-0.19527 -12.5,0 -3.4375,0.19527 "
                "-0.625,0.35504 6.25,0.35504 6.875,0 9.6875,-0.15977 6.25,-0.35504 z m 31.04159,"
                "0.001 c -3.41463,-0.19467 -9.26463,-0.19611 -13,-0.003 -3.73538,0.19293 -0.94159,"
                "0.35221 6.20841,0.35396 7.15,0.002 10.20621,-0.1561 6.79159,-0.35078 z M "
                "66.123119,194.5 l 1.95316,-4 -3.143535,3.5 C 61.17009,198.18933 53,210.57891 "
                "53,212.09549 53,213.69448 63.861979,199.13073 66.123119,194.5 Z m 158.804301,"
                "-8.13486 c 2.73082,-3.47168 2.6143,-5.56789 -0.51631,-9.28841 -3.0394,-3.61212 "
                "-6.0656,-3.92295 -9.77625,-1.00415 -3.30154,2.59699 -3.61252,7.94976 -0.63486,"
                "10.92742 2.97766,2.97766 8.33043,2.66668 10.92742,-0.63486 z M 215,186 c -3.99017,"
                "-3.99017 -1.34575,-10 4.40017,-10 3.57614,0 5.59983,2.122 5.59983,5.87187 0,"
                "5.38221 -6.19043,7.9377 -10,4.12813 z m 6.8,-1.2 c 2.16489,-2.16489 1.43839,"
                "-5.70206 -1.31299,-6.39262 -4.50491,-1.13066 -7.09087,2.84591 -3.91558,6.02119 "
                "1.87901,1.87902 3.59881,2.00119 5.22857,0.37143 z"
            ),
            -90,
        ),
    },
)

if __name__ == "__main__":

    def main():
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument("type", choices=IMAGE_REGISTRY.keys())
        parser.add_argument("-o", "--output", type=argparse.FileType("w"), default="-")
        parser.add_argument("-r", "--rotation", type=float, default=0.0)
        parser.add_argument("-f", "--fill", type=str, default="#000000")
        args = parser.parse_args()
        args.output.write(IMAGE_REGISTRY.get_image(args.type, args.rotation, args.fill))

    main()