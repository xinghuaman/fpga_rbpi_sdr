import string

f = open('fir_decimation_kr.txt', 'w')

k =[ 0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,      0,    0,    0,    0,    0,    0,    0,    0,  -1,  -1,  -1,  -1,  -1,  -1,    0,    0,    0,      1,    1,    2,    2,    3,    3,    3,    3,    3,    2,    1,  -1,  -3,  -5,  -7,  -9,  -10,    -11,  -12,  -12,  -10,  -8,  -5,    0,    5,    11,    18,    24,    29,    34,    36,    36,      33,    28,    19,    7,  -7,  -24,  -41,  -58,  -74,  -86,  -95,  -97,  -93,  -81,  -61,    -34,    0,    39,    81,    124,    164,    198,    222,    234,    230,    210,    171,    114,    41,    -44,  -139,  -236,  -329,  -411,  -475,  -513,  -520,  -490,  -422,  -315,  -173,    0,      194,    398,    600,    783,    933,    1036,    1079,    1050,    945,    761,    504,    181,  -191,    -591,  -996,  -1375,  -1702,  -1946,  -2081,  -2087,  -1949,  -1662,  -1230,  -667,    0,      736,    1498,    2234,    2892,    3417,    3760,    3880,    3746,    3342,    2670,    1751,    624,    -653,  -2007,  -3352,  -4594,  -5639,  -6398,  -6791,  -6759,  -6266,  -5303,  -3895,  -2098,      0,    2282,    4608,    6824,    8771,    10292,    11249,    11528,    11054,    9797,    7776,      5066,    1794,  -1865,  -5695,  -9450,  -12872,  -15703,  -17705,  -18679,  -18479,  -17027,    -14325,  -10459,  -5600,    0,    6022,    12093,    17809,    22761,    26562,    28872,    29429,      28068,    24743,    19536,    12662,    4460,  -4614,  -14016,  -23143,  -31366,  -38076,    -42723,  -44857,  -44166,  -40505,  -33919,  -24652,  -13140,    0,    14003,    27996,    41051,      52241,    60706,    65710,    66700,    63357,    55628,    43748,    28243,    9911,  -10213,    -30910,  -50849,  -68668,  -83061,  -92872,  -97175,  -95355,  -87162,  -72753,  -52707,    -28007,    0,    29666,    59140,    86471,    109739,    127178,    137301,    139018,    131727,      115383,    90534,    58318,    20421,  -21002,  -63440,  -104171,  -140432,  -169591,  -189333,    -197825,  -193866,  -176997,  -147581,  -106816,  -56711,    0,    59998,    119556,    174764,      221768,    257022,    277542,    281122,    266531,    233640,    183500,    118340,    41496,    -42745,  -129357,  -212856,  -287626,  -348265,  -389944,  -408752,  -401997,  -368452,    -308528,  -224345,  -119714,    0,    128107,    256927,    378197,    483543,    564993,    615486,      629373,    602854,    534341,    424717,    277466,    98662,  -103182,  -317414,  -531677,    -732458,  -905728,  -1037652,  -1115313,  -1127431,  -1065027,  -922006,  -695608,  -386717,      0,    456147,    969824,    1526042,    2107297,    2694277,    3266681,    3804095,    4286900,      4697146,    5019374,    5241315,    5354463]


for i in range (0,320):
    if k[i] >= 0:
        f.write('    "{0:024b}",\n'.format(k[i]))
    else:
        f.write('    "{0:024b}",\n'.format(16777216+k[i]))
#f.write( "%d\n" % k[i]
