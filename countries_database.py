#database based on the countries in the UN
countries = {
  "1":"Argentina",
  "2":"Australia",
  "3":"Belarus",
  "4":"Belgium",
  "5":"Brazil",
  "6":"Cambodia",
  "7":"Chad",
  "8":"China",
  "9":"Colombia",
  "10":"Costa_Rica",
  "11":"Cuba",
  "12":"Dominican_Republic",
  "13":"Egypt",
  "14":"Ethiopia",
  "15":"Finland",
  "16":"France",
  "17":"Germany",
  "18":"Guatemala",
  "19":"Haiti",
  "20":"Honduras",
  "21":"Iceland",
  "22":"India",
  "23":"Ireland",
  "24":"Italy",
  "25":"Jamaica",
  "26":"Kazakhstan",
  "27":"Liechtenstein",
  "28":"Madagascar",
  "29":"Mexico",
  "30":"Netherlands",
  "31":"Oman",
  "32":"Pakistan",
  "33":"Panama",
  "34":"Papua_New_Guinea",
  "35":"Peru",
  "36":"Poland",
  "37":"Romania",
  "38":"Russia",
  "39":"Saudi_Arabia",
  "40":"South_Africa",
  "41":"South_Sudan",
  "42":"Spain",
  "43":"Sri_Lanka",
  "44":"Switzerland",
  "45":"Sweden",
  "46":"Turkey",
  "47":"Turkmenistan",
  "48":"Ukraine",
  "49":"United_Arab_Emirates",
  "50":"United_Kingdom",
  "51":"United_States",
  "52":"Venezuela",
  "53":"Vietnam",
  "54":"Yemen"
}

#database to link the country to its respective ascii art file
country_img = {
  "Argentina":"banner (1)",
  "Australia":"banner (2)",
  "Belarus":"banner (3)",
  "Belgium":"banner (4)",
  "Brazil":"banner (5)",
  "Cambodia":"banner (6)",
  "Chad":"banner (7)",
  "China":"banner (8)",
  "Colombia":"banner (9)",
  "Costa_Rica":"banner (10)",
  "Cuba":"banner (11)",
  "Dominican_Republic":"banner (12)",
  "Egypt":"banner (13)",
  "Ethiopia":"banner (14)",
  "Finland":"banner (15)",
  "France":"banner (16)",
  "Germany":"banner (17)",
  "Guatemala":"banner (18)",
  "Haiti":"banner (19)",
  "Honduras":"banner (20)",
  "Iceland":"banner (21)",
  "India":"banner (22)",
  "Ireland":"banner (23)",
  "Italy":"banner (24)",
  "Jamaica":"banner (25)",
  "Kazakhstan":"banner (26)",
  "Liechtenstein":"banner (27)",
  "Madagascar":"banner (28)",
  "Mexico":"banner (29)",
  "Netherlands":"banner (30)",
  "Oman":"banner (31)",
  "Pakistan":"banner (32)",
  "Panama":"banner (33)",
  "Papua_New_Guinea":"banner (34)",
  "Peru":"banner (35)",
  "Poland":"banner (36)",
  "Romania":"banner (37)",
  "Russia":"banner (38)",
  "Saudi_Arabia":"banner (39)",
  "South_Africa":"banner (40)",
  "South_Sudan":"banner (41)",
  "Spain":"banner (42)",
  "Sri_Lanka":"banner (43)",
  "Switzerland":"banner (44)",
  "Sweden":"banner (45)",
  "Turkey":"banner (46)",
  "Turkmenistan":"banner (47)",
  "Ukraine":"banner (48)",
  "United_Arab_Emirates":"banner (49)",
  "United_Kingdom":"banner (50)",
  "United_States":"banner (51)",
  "Venezuela":"banner (52)",
  "Vietnam":"banner (53)",
  "Yemen":"banner (54)"
}

#database to link the countries (lat longs) to a number that can be used to later called that tuple
countries_latlongs = {
  1 : ("Argentina", -38.416097, -63.616672),
  2 : ("Australia", -25.274398, 133.775136),
  3 : ("Belarus", 53.709807, 27.953389),
  4 : ("Belgium", 50.503887, 4.469936),
  5 : ("Brazil", -14.235004, -51.92528),
  6 : ("Cambodia", 12.565679, 104.990963),
  7 : ("Chad", 15.454166, 18.732207),
  8 : ("China", 35.86166, 104.195397),
  9 : ("Colombia", 4.570868, -74.297333),
  10 : ("Costa_Rica", 9.748917, -83.753428),
  11 : ("Cuba", 21.521757, -77.781167),
  12 : ("Dominican_Republic", 18.735693, -70.162651),
  13 : ("Egypt", 26.820553, 30.802498),
  14 : ("Ethiopia", 9.145, 40.489673),
  15 : ("Finland", 61.92411, 25.748151),
  16 : ("France", 46.227638, 2.213749),
  17 : ("Germany", 51.165691, 10.451526),
  18 : ("Guatemala", 15.783471, -90.230759),
  19 : ("Haiti", 18.971187, -72.285215),
  20 : ("Honduras", 15.199999, -86.241905),
  21 : ("Iceland", 64.963051, -19.020835),
  22 : ("India", 20.593684, 78.96288),
  23 : ("Ireland", 53.41291, -8.24389),
  24 : ("Italy", 41.87194, 12.56738),
  25 : ("Jamaica", 18.109581, -77.297508),
  26 : ("Kazakhstan", 48.019573, 66.923684),
  27 : ("Liechtenstein", 47.166, 9.555373),
  28 : ("Madagascar", -18.766947, 46.869107),
  29 : ("Mexico", 23.634501, -102.552784),
  30 : ("Netherlands", 52.132633, 5.291266),
  31 : ("Oman", 21.4735, 55.9754),
  32 : ("Pakistan", 30.3753, 69.3451),
  33 : ("Panama", 8.538, 80.7821),
  34 : ("Papua_New_Guinea", 6.315, 143.9555),
  35 : ("Peru", -9.189967, -75.015152),
  36 : ("Poland", 51.919438, 19.145136),
  37 : ("Romania", 45.943161, 24.96676),
  38 : ("Russia", 61.52401, 105.318756),
  39 : ("Saudi_Arabia", 23.885942, 45.079162),
  40 : ("South_Africa", -30.559482, 22.937506),
  41 : ("South_Sudan", 6.877, 31.307),
  42 : ("Spain", 40.463667, -3.74922),
  43 : ("Sri_Lanka", 7.873054, 80.771797),
  44 : ("Switzerland", 46.818188, 8.227512),
  45 : ("Sweden", 60.128161, 18.643501),
  46 : ("Turkey", 38.963745, 35.243322),
  47 : ("Turkmenistan", 38.969719, 59.556278),
  48 : ("Ukraine", 48.379433, 31.16558),
  49 : ("United_Arab_Emirates", 23.424076, 53.847818),
  50 : ("United_Kingdom", 55.378051, -3.435973),
  51 : ("United_States", 37.09024, -95.712891),
  52 : ("Venezuela", 6.42375, -66.58973),
  53 : ("Vietnam", 14.058324, 108.277199),
  54 : ("Yemen", 15.552727, 48.516388)
}