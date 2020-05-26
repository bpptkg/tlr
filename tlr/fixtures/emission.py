raw_data = [
    'TLR0101256 +635.00 +712.00 +669.75 +29.53 +30.01 +29.81 +74.01 +74.44 +74.28 +12.05 \r\n \x16\xfd\xd1=e\x04\x15\x04\x188',
    'TLR0101256 +627.00 +705.00 +665.50 +31.52 +31.74 +31.60 +74.87 +75.39 +75.19 +12.05 \r\n \x04\xf0A\x01\x13 ',
    'TLR0101256 +619.00 +689.00 +652.25 +27.30 +27.76 +27.55 +74.04 +74.56 +74.37 +12.06 \r\n  \x14\x86t\xca\x0e\xa0\x19\x01',
    'TLR0101256 +593.00 +671.00 +631.50 +25.48 +25.70 +25.59 +73.83 +74.35 +74.11 +12.06 \r\n \x1c\xc2: \x13\xba\xa8"l\x01\xc0',
    'TLR0101256 +591.00 +657.00 +622.00 +25.50 +25.88 +25.71 +74.58 +75.51 +75.02 +12.06 \r\n \xe0\x18\x04',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n \x80\xf5\xf8\xcd\xc52C@TLR0101256 +610.00 +681.00 +642.25 +31.08 +32.03 +31.70 +75.83 +76.20 +76.03 +12.05 \r\n \x01\x08,\x84\xec .\x03\xc3\x08\x0e',
    'TLR0101256 +610.00 +681.00 +642.25 +31.08 +32.03 +31.70 +75.83 +76.20 +76.03 +12.05 \r\n \t\x05\xa0\x99\xb8\x01\x01',
    'TLR0101256 +610.00 +681.00 +642.25 +31.08 +32.03 +31.70 +75.83 +76.20 +76.03 +12.05 \r\n \x1e\x810',
    'TLR0101256 +610.00 +681.00 +642.25 +31.08 +32.03 +31.70 +75.83 +76.20 +76.03 +12.05 \r\n C\x02N\x1e\xd8LE\x8e`$\x08',
    'TLR0101256 +645.00 +761.00 +698.50 +37.16 +37.59 +37.31 +84.19 +85.01 +84.64 +12.05 \r\n _\x8br\xe5\x1f\x07p\x05N\x85',
    'TLR0101256 +686.00 +768.00 +719.50 +34.46 +34.64 +34.55 +80.91 +81.63 +81.33 +12.06 \r\n $AH\x94!\x84\x85\x10*\x14\x02',
    'TLR0101256 +672.00 +748.00 +705.75 +31.71 +31.89 +31.80 +80.16 +81.29 +80.68 +12.05 \r\n \x0e\xf0\x13io\x80Ax\x03',
    'TLR0101256 +671.00 +755.00 +706.75 +31.77 +31.95 +31.83 +79.53 +80.31 +79.95 +12.05 \r\n \x01J4\x90a\x82\x1cAF\xe3',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n \x01`\x812n\x88L\xd3\xc0\x02\x80TLR0101256 +675.00 +736.00 +700.75 +30.84 +31.02 +30.93 +77.97 +78.57 +78.33 +12.05 \r\n \x03\x9f\x92DAd\x8a',
    'TLR0101256 +665.00 +741.00 +696.25 +31.48 +31.81 +31.65 +78.40 +79.01 +78.77 +12.06 \r\n K\xe8\x02(>\xa0(>',
    'TLR0101256 +683.00 +757.00 +716.00 +33.09 +33.54 +33.34 +78.14 +78.63 +78.46 +12.05 \r\n \xfeI\x01\xc9\x1a\xc4\np',
    'TLR0101256 +683.00 +757.00 +716.00 +33.09 +33.54 +33.34 +78.14 +78.63 +78.46 +12.05 \r\n h\xcc $\x8f\xe1\x9c\xc0-\xf0\t',
    'TLR0101256 +706.00 +798.00 +750.25 +38.09 +40.29 +38.68 +80.02 +83.80 +81.22 +12.05 \r\n \\\x01',
    'TLR0101256 +684.00 +777.00 +722.25 +35.22 +35.56 +35.40 +84.14 +85.12 +84.64 +12.05 \r\n %\xf4"@\x84\xe3\x05',
    'TLR0101256 +692.00 +778.00 +730.75 +34.32 +34.47 +34.37 +81.91 +82.53 +82.28 +12.05 \r\n \x03`\x9013\x06\xee<\xfe',
    '#System Restart HELO MERAPI \r\nT#01 Termocouple_1 T#02 Termocoup \r\n 4\xf0\x04\x08\x08D\x9eTLR0101256 +684.00 +753.00 +712.75 +31.22 +31.46 +31.33 +80.19 +80.65 +80.50 +12.05 \r\n \xe0H\x16\xd4',
    'TLR0101256 +670.00 +734.00 +696.75 +28.96 +29.10 +29.01 +80.48 +81.15 +80.88 +12.06 \r\n \x10\x07)',
    'TLR0101256 +644.00 +709.00 +671.25 +25.83 +26.04 +25.91 +80.94 +81.58 +81.28 +12.06 \r\n \x13\xb5\x93\x89!\xdd\x87\xf0\x1c\x1b\x08',
    'TLR0101256 +614.00 +682.00 +645.00 +24.42 +24.58 +24.48 +81.32 +82.25 +81.79 +12.06 \r\n \x05\x98;\x05\xc8\x01\x83$',
    'TLR0101256 +569.00 +707.00 +626.25 +38.59 +38.94 +38.79 +85.37 +86.08 +85.77 +12.05 \r\n \xe0P\xc1\x19\xbd\x81(`R\x02\x02',
    'TLR0101256 +386.00 +649.00 +493.75 +40.98 +41.31 +41.15 +87.17 +87.99 +87.61 +12.06 \r\n \x89\x08',
    'TLR0101256 +681.00 +772.00 +724.50 +38.31 +38.85 +38.49 +81.80 +83.09 +82.37 +12.05 \r\n H!B\x8c\xf8',
    'TLR0101256 +689.00 +761.00 +718.25 +34.75 +34.99 +34.85 +80.13 +81.03 +80.60 +12.05 \r\n $\xa15\x12\x04',
    'TLR0101256 +672.00 +750.00 +708.00 +32.90 +33.21 +33.04 +79.21 +80.48 +79.74 +12.06 \r\n \x01',
    '\x88\xfaTLR0101256 +670.00 +737.00 +699.25 +30.40 +30.70 +30.55 +78.86 +79.87 +79.34 +12.05 \r\n \x04+\x86\xfe\x8dp\x1a>',
    'TLR0101256 +652.00 +715.00 +681.25 +27.59 +27.83 +27.70 +79.21 +80.74 +80.26 +12.06 \r\n 0\xf4\x80\xc00\x02\xb0\xf1\x01',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n \xb9\xf3|TLR0101256 +629.00 +710.00 +660.50 +28.32 +28.48 +28.40 +81.32 +81.72 +81.57 +12.06 \r\n x&!\x8eCz\x01\x80B\xb6\x04',
    'TLR0101256 +621.00 +690.00 +654.00 +28.10 +28.50 +28.34 +81.06 +81.60 +81.44 +12.06 \r\n \xba1\x08^\x07\xe9\x80bHK\xfc',
    'TLR0101256 +616.00 +691.00 +649.25 +28.21 +28.70 +28.50 +80.65 +81.35 +81.05 +12.05 \r\n 4\x80\x08\x16\x12s\x80-]h\x8b\x8c',
    'TLR0101256 +611.00 +685.00 +646.25 +28.36 +29.10 +28.83 +80.45 +80.91 +80.72 +12.05 \r\n \xd0',
    'TLR0101256 +460.00 +642.00 +558.75 +37.63 +38.53 +38.21 +85.77 +86.61 +86.31 +12.05 \r\n @\xfc\xe0}R\xc8\xfc#\xf8',
    'TLR0101256 +25.00 +642.00 +426.00 +38.30 +42.89 +39.52 +86.24 +89.92 +87.35 +12.05 \r\n \x02\xf73\x8b\xa9\xfe',
    'TLR0101256 +25.00 +642.00 +426.00 +38.30 +42.89 +39.52 +86.24 +89.92 +87.35 +12.05 \r\n \xe2\xfe',
    'TLR0101256 +701.00 +770.00 +725.50 +35.46 +35.93 +35.64 +84.81 +85.34 +85.10 +12.06 \r\n \x80\x8f\xf6\n@\xae2\r\xac\x01\xf3',
    'TLR0101256 +692.00 +756.00 +715.50 +31.16 +31.32 +31.21 +84.14 +84.70 +84.43 +12.05 \r\n `\x86$\x80`\x081\xe4',
    'TLR0101256 +653.00 +741.00 +689.25 +28.90 +29.30 +29.11 +84.33 +84.89 +84.62 +12.05 \r\n \x06x\x81x\xb2X_!\xe2',
    'TLR0101256 +637.00 +711.00 +668.75 +26.15 +26.51 +26.33 +84.56 +86.47 +85.25 +12.06 \r\n \x1d\xc0\x17\x06/\x1ff.',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n \x1e\x80\xf0\t\xb3D"\xc0\tTLR0101256 +622.00 +699.00 +654.75 +28.60 +29.36 +29.09 +85.26 +86.08 +85.70 +12.05 \r\n \x08\x80',
    'TLR0101256 +617.00 +692.00 +652.00 +28.16 +28.40 +28.25 +82.14 +82.59 +82.38 +12.06 \r\n ,G6\xa6\x08P\xa6\xc5\x02\xa0',
    'TLR0101256 +593.00 +666.00 +625.50 +24.20 +24.44 +24.32 +82.05 +82.45 +82.32 +12.05 \r\n \x03F\x92\x902',
    'TLR0101256 +571.00 +634.00 +599.75 +23.90 +24.33 +24.14 +84.14 +85.06 +84.69 +12.05 \r\n \xcc;:\xb0\xe5\xc0\xe498\xf5',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n \xf0TLR0101256 +416.00 +574.00 +492.75 +27.52 +28.52 +28.16 +89.48 +89.84 +89.71 +12.05 \r\n \x01\xe2]9\x08\x04\x01',
    'TLR0101256 +416.00 +574.00 +492.75 +27.52 +28.52 +28.16 +89.48 +89.84 +89.71 +12.05 \r\n \xe7\xf3\x88',
    'TLR0101256 +416.00 +574.00 +492.75 +27.52 +28.52 +28.16 +89.48 +89.84 +89.71 +12.05 \r\n Lt\xe0;\xe4\x8b',
    'TLR0101256 +416.00 +574.00 +492.75 +27.52 +28.52 +28.16 +89.48 +89.84 +89.71 +12.05 \r\n \xf8xF\xfa',
    'TLR0101256 +602.00 +783.00 +711.50 +37.95 +41.51 +38.87 +83.71 +87.12 +84.85 +12.05 \r\n \x17\xa0',
    'TLR0101256 +705.00 +734.00 +714.25 +27.50 +28.04 +27.68 +84.28 +84.73 +84.50 +12.06 \r\n 2\xe4\xe0\n\xb3\x15\xca\xad\xfe',
    'TLR0101256 +649.00 +690.00 +672.50 +23.14 +23.37 +23.24 +86.10 +87.14 +86.59 +12.07 \r\n \x90\x08T\x98X"\xac\t\xc4\xf8',
    'TLR0101256 +601.00 +650.00 +620.50 +21.94 +22.44 +22.22 +89.92 +90.41 +90.19 +12.05 \r\n \xfe',
    'TLR0101256 +577.00 +645.00 +607.75 +23.95 +24.09 +24.02 +87.26 +88.58 +87.81 +12.06 \r\n \x88$\x07',
    'TLR0101256 +554.00 +637.00 +588.00 +23.41 +23.83 +23.63 +87.17 +87.76 +87.54 +12.06 \r\n \x0e\x84\x8f)\x80\t\x0e\x10\xbay8',
    'TLR0101256 +547.00 +628.00 +582.75 +23.05 +23.22 +23.10 +86.41 +87.62 +86.94 +12.06 \r\n \x16\x03\x04!\xb0\x16\xf0@\x04',
    '.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n l@\x1cd\x02\xf8TLR0101256 +371.00 +519.00 +445.25 +27.24 +28.03 +27.74 +90.90 +91.28 +91.11 +12.05 \r\n \xe0a\x92("\x10\x18\x06\xfa',
    'TLR0101256 +21.00 +249.00 +115.25 +34.90 +36.24 +35.80 +92.27 +92.87 +92.61 +12.05 \r\n !F*\xfa\x04Q\x1d\xdc"\td',
    'TLR0101256 +21.00 +249.00 +115.25 +34.90 +36.24 +35.80 +92.27 +92.87 +92.61 +12.05 \r\n  \x19g\xaa9\xb0\x10\xea\x12\x87\x08',
    'TLR0101256 +21.00 +249.00 +115.25 +34.90 +36.24 +35.80 +92.27 +92.87 +92.61 +12.05 \r\n \x90\xe2\xb6daTo8P\xfe',
    'TLR0101256 +692.00 +761.00 +720.50 +34.85 +36.43 +35.29 +82.67 +85.46 +84.61 +12.06 \r\n \x01\xe0\x8e\x8eE\x01Qw\x08',
    'TLR0101256 +628.00 +678.00 +648.25 +25.91 +26.57 +26.30 +88.55 +88.96 +88.82 +12.06 \r\n (\xa5\x10pH\x01',
    'TLR0101256 +558.00 +622.00 +585.25 +21.50 +21.80 +21.65 +87.17 +87.54 +87.42 +12.04 \r\n \xa1\x1e\r\x1c\x08\x06\xaf\x01\xf2',
    '\xb6+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n \x0fPxN!\x10\xcc\x82\xb0\x01\x80TLR0101256 +567.00 +643.00 +601.00 +27.44 +27.72 +27.57 +85.01 +85.46 +85.33 +12.06 \r\n \xb6\xcd\x03\x10|6\xe2 \xc8]\x03\x04\x17',
    'TLR0101256 +566.00 +664.00 +605.50 +29.53 +31.12 +30.61 +86.78 +87.26 +87.04 +12.06 \r\n \xa0\x99\x02@\x08\x04',
    'TLR0101256 +366.00 +546.00 +453.75 +36.80 +37.73 +37.40 +89.15 +89.59 +89.37 +12.05 \r\n \x8f\xf8! \n\x0b',
    'TLR0101256 +488.00 +652.00 +566.50 +39.16 +39.46 +39.28 +87.03 +87.96 +87.50 +12.05 \r\n \x08\x8d\x16k\xcaPH\n\xb1',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n ^x\x1a\xc6 \x90\xceH\xf0\x06TLR0101256 +623.00 +696.00 +652.75 +33.07 +33.46 +33.20 +83.38 +84.16 +83.80 +12.05 \r\n @\xb0\x15\x18\x87\x0c\x80\xcb\x87H\x9a\xdc\x10',
    'TLR0101256 +605.00 +679.00 +638.00 +29.76 +29.95 +29.81 +83.66 +84.11 +83.90 +12.05 \r\n \x12\r\xc0\xf9\xf2',
    'TLR0101256 +585.00 +648.00 +612.25 +24.94 +25.26 +25.07 +81.63 +82.03 +81.85 +12.04 \r\n \xcb\x08@pdX\x177',
    'TLR0101256 +560.00 +626.00 +590.25 +23.50 +23.65 +23.58 +82.73 +83.57 +83.17 +12.04 \r\n \x04\xa8\x98.\x0e&%\xf1\x02\xf8',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n r\x03\xa4(\x14SH\x898TLR0101256 +536.00 +613.00 +570.75 +23.29 +24.41 +24.03 +87.88 +88.38 +88.14 +12.07 \r\n ',
    'TLR0101256 +561.00 +636.00 +594.00 +28.43 +28.64 +28.51 +84.14 +85.40 +84.67 +12.05 \r\n \x15\n\xcd\x07\xcb\xc4\x04',
    "\x17\xe5\xfe\xbb\x033_\xf8\xee\xff\xfbTLR0101256 +580\x0e 0 +646.`\xc1\x02Z\xb2\x02\xbar\x82\x82\x02Z\x92B\xe4\t\x13'\x08m\xfb\xcf|\xca\xc0,\xe3\xb7~\xee\xfb\xb1?\xb9y\x85\xd2c",
    'TLR0101256 +557.00 +615.00 +585.50 +24.49 +24.65 +24.57 +82.05 +82.56 +82.40 +12.06 \r\n \x10\xd0\x0e2=\xe0\x04',
    'TLR0101256 +535.00 +630.00 +574.75 +30.86 +31.93 +31.55 +87.03 +87.51 +87.29 +12.05 \r\n \x0f\x16<\xe9',
    'TLR0101256 +535.00 +630.00 +574.75 +30.86 +31.93 +31.55 +87.03 +87.51 +87.29 +12.05 \r\n \x02\\\x03\x18B',
    'TLR0101256 +535.00 +630.00 +574.75 +30.86 +31.93 +31.55 +87.03 +87.51 +87.29 +12.05 \r\n lS\xcc\x04(;\x10\n\x1a\xfc',
    'TLR0101256 +461.00 +638.00 +537.25 +37.89 +38.59 +38.11 +87.71 +88.27 +87.98 +12.05 \r\n \x01\x81j\xd9r\x92\x90\x0c\x01 ',
    'TLR0101256 +591.00 +696.00 +635.00 +33.89 +34.08 +34.00 +87.06 +87.74 +87.47 +12.05 \r\n \x01\xe0 _\x8e\x12\xa4',
    '#System Restart HELO MERAPI \r\nT#01 Termocouple_1 T#02 Termocoup \r\n  \x18\x10\xc0\xf8T\xf0<\x03\xa0TLR0101256 +625.00 +710.00 +662.75 +32.04 +32.17 +32.07 +86.36 +86.81 +86.67 +12.05 \r\n M\xcf\x02\x04\r~\t',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n \x03x\x02\x8f\xbb \x81X2TLR0101256 +631.00 +717.00 +668.75 +31.58 +31.81 +31.67 +84.64 +85.34 +85.05 +12.06 \r\n \x81\x18\nS\xd8P\x8c2\xc9',
    'TLR0101256 +637.00 +716.00 +671.50 +31.27 +31.45 +31.32 +84.53 +85.06 +84.84 +12.06 \r\n \x91*\x91F\x82\x030\xd0x\x16\x01',
    'TLR0101256 +639.00 +715.00 +673.00 +31.56 +31.88 +31.72 +84.44 +85.15 +84.87 +12.05 \r\n \x90\x88\xe0(',
    'TLR0101256 +651.00 +731.00 +683.25 +31.44 +31.63 +31.51 +83.29 +83.99 +83.68 +12.05 \r\n \x06b\x05d@K\xc9\x0c',
    'TLR0101256 +644.00 +727.00 +680.75 +31.33 +31.53 +31.40 +82.93 +83.63 +83.34 +12.05 \r\n \x9e\t',
    'TLR0101256 +658.00 +738.00 +693.25 +34.20 +35.08 +34.75 +84.64 +85.06 +84.93 +12.05 \r\n /\x9b$\xc6l\xf0',
    'TLR0101256 +502.00 +691.00 +583.25 +39.22 +39.40 +39.30 +87.54 +88.04 +87.89 +12.05 \r\n \x1ca\x89\xc8& K',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n \x88\x04\xc4\x85\x18\x88\xc3\x82\x08TLR0101256 +675.00 +752.00 +709.00 +35.75 +36.33 +35.97 +82.64 +84.11 +83.25 +12.05 \r\n \x04\xc8\xb3\x88\x06h\x07\xf7b\xa2\xf8',
    'TLR0101256 +620.00 +699.00 +654.00 +27.37 +27.54 +27.44 +83.77 +84.25 +84.08 +12.06 \r\n \xc2\x06\xe8\x08\xcc>@$\x020@\x08=\x0c\x8e\x94\x14T4\r\x10L\xa16\x19P\x832\x81$\x95*\xe5\x10c\xb0EA\x82\xa7P@`\x86\x080\n\xc0 \x04\t!\xfc bx\x0f \x02\xe6',
    'TLR0101256 +605.00 +677.00 +640.25 +26.10 +26.27 +26.16 +84.02 +84.56 +84.34 +12.06 \r\n \x80\x8f L\x04\x01',
    'TLR0101256 +602.00 +684.00 +637.00 +27.88 +28.07 +27.95 +83.32 +84.81 +83.93 +12.06 \r\n \x8a4',
    'TLR0101256 +603.00 +683.00 +635.50 +27.68 +27.88 +27.76 +82.53 +82.84 +82.69 +12.05 \r\n &J\x1d\xe1\x13',
    '+00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 +00.00 \r\n  TLR0101256 +605.00 +683.00 +638.25 +29.45 +29.91 +29.71 +84.16 +84.61 +84.48 +12.05 \r\n \x04\xf9\x08\x80@0',
    'TLR0101256 +615.00 +689.00 +646.50 +30.00 +30.30 +30.15 +82.19 +83.04 +82.64 +12.05 \r\n \x80\x0c',
    'TLR0101256 +597.00 +667.00 +625.75 +24.98 +25.54 +25.30 +83.32 +83.77 +83.58 +12.06 \r\n x\x960s\xa9\x10/\xa3\x05',
    'TLR0101256 +589.00 +668.00 +629.25 +29.00 +29.60 +29.36 +83.32 +84.02 +83.71 +12.05 \r\n \x04\xe4U>p\x18',
    'TLR0101256 +121.00 +347.00 +220.50 +35.81 +36.94 +36.54 +89.97 +90.46 +90.28 +12.05 \r\n \x10\x01:\x08\x89\x18\xcbs',
    'TLR0101256 +121.00 +347.00 +220.50 +35.81 +36.94 +36.54 +89.97 +90.46 +90.28 +12.05 \r\n \x87I\x99\x82\x12',
]

clean_data = [
    [['635.00', '712.00', '669.75', '29.53', '30.01', '29.81', '74.01', '74.44', '74.28', '12.05'], ],
    [['627.00', '705.00', '665.50', '31.52', '31.74', '31.60', '74.87', '75.39', '75.19', '12.05'], ],
    [['619.00', '689.00', '652.25', '27.30', '27.76', '27.55', '74.04', '74.56', '74.37', '12.06'], ],
    [['593.00', '671.00', '631.50', '25.48', '25.70', '25.59', '73.83', '74.35', '74.11', '12.06'], ],
    [['591.00', '657.00', '622.00', '25.50', '25.88', '25.71', '74.58', '75.51', '75.02', '12.06'], ],
    [['610.00', '681.00', '642.25', '31.08', '32.03', '31.70', '75.83', '76.20', '76.03', '12.05'], ],
    [['610.00', '681.00', '642.25', '31.08', '32.03', '31.70', '75.83', '76.20', '76.03', '12.05'], ],
    [['610.00', '681.00', '642.25', '31.08', '32.03', '31.70', '75.83', '76.20', '76.03', '12.05'], ],
    [['610.00', '681.00', '642.25', '31.08', '32.03', '31.70', '75.83', '76.20', '76.03', '12.05'], ],
    [['645.00', '761.00', '698.50', '37.16', '37.59', '37.31', '84.19', '85.01', '84.64', '12.05'], ],
    [['686.00', '768.00', '719.50', '34.46', '34.64', '34.55', '80.91', '81.63', '81.33', '12.06'], ],
    [['672.00', '748.00', '705.75', '31.71', '31.89', '31.80', '80.16', '81.29', '80.68', '12.05'], ],
    [['671.00', '755.00', '706.75', '31.77', '31.95', '31.83', '79.53', '80.31', '79.95', '12.05'], ],
    [['675.00', '736.00', '700.75', '30.84', '31.02', '30.93', '77.97', '78.57', '78.33', '12.05'], ],
    [['665.00', '741.00', '696.25', '31.48', '31.81', '31.65', '78.40', '79.01', '78.77', '12.06'], ],
    [['683.00', '757.00', '716.00', '33.09', '33.54', '33.34', '78.14', '78.63', '78.46', '12.05'], ],
    [['683.00', '757.00', '716.00', '33.09', '33.54', '33.34', '78.14', '78.63', '78.46', '12.05'], ],
    [['706.00', '798.00', '750.25', '38.09', '40.29', '38.68', '80.02', '83.80', '81.22', '12.05'], ],
    [['684.00', '777.00', '722.25', '35.22', '35.56', '35.40', '84.14', '85.12', '84.64', '12.05'], ],
    [['692.00', '778.00', '730.75', '34.32', '34.47', '34.37', '81.91', '82.53', '82.28', '12.05'], ],
    [['684.00', '753.00', '712.75', '31.22', '31.46', '31.33', '80.19', '80.65', '80.50', '12.05'], ],
    [['670.00', '734.00', '696.75', '28.96', '29.10', '29.01', '80.48', '81.15', '80.88', '12.06'], ],
    [['644.00', '709.00', '671.25', '25.83', '26.04', '25.91', '80.94', '81.58', '81.28', '12.06'], ],
    [['614.00', '682.00', '645.00', '24.42', '24.58', '24.48', '81.32', '82.25', '81.79', '12.06'], ],
    [['569.00', '707.00', '626.25', '38.59', '38.94', '38.79', '85.37', '86.08', '85.77', '12.05'], ],
    [['386.00', '649.00', '493.75', '40.98', '41.31', '41.15', '87.17', '87.99', '87.61', '12.06'], ],
    [['681.00', '772.00', '724.50', '38.31', '38.85', '38.49', '81.80', '83.09', '82.37', '12.05'], ],
    [['689.00', '761.00', '718.25', '34.75', '34.99', '34.85', '80.13', '81.03', '80.60', '12.05'], ],
    [['672.00', '750.00', '708.00', '32.90', '33.21', '33.04', '79.21', '80.48', '79.74', '12.06'], ],
    [['670.00', '737.00', '699.25', '30.40', '30.70', '30.55', '78.86', '79.87', '79.34', '12.05'], ],
    [['652.00', '715.00', '681.25', '27.59', '27.83', '27.70', '79.21', '80.74', '80.26', '12.06'], ],
    [['629.00', '710.00', '660.50', '28.32', '28.48', '28.40', '81.32', '81.72', '81.57', '12.06'], ],
    [['621.00', '690.00', '654.00', '28.10', '28.50', '28.34', '81.06', '81.60', '81.44', '12.06'], ],
    [['616.00', '691.00', '649.25', '28.21', '28.70', '28.50', '80.65', '81.35', '81.05', '12.05'], ],
    [['611.00', '685.00', '646.25', '28.36', '29.10', '28.83', '80.45', '80.91', '80.72', '12.05'], ],
    [['460.00', '642.00', '558.75', '37.63', '38.53', '38.21', '85.77', '86.61', '86.31', '12.05'], ],
    [['25.00',  '642.00', '426.00', '38.30', '42.89', '39.52', '86.24', '89.92', '87.35', '12.05'], ],
    [['25.00',  '642.00', '426.00', '38.30', '42.89', '39.52', '86.24', '89.92', '87.35', '12.05'], ],
    [['701.00', '770.00', '725.50', '35.46', '35.93', '35.64', '84.81', '85.34', '85.10', '12.06'], ],
    [['692.00', '756.00', '715.50', '31.16', '31.32', '31.21', '84.14', '84.70', '84.43', '12.05'], ],
    [['653.00', '741.00', '689.25', '28.90', '29.30', '29.11', '84.33', '84.89', '84.62', '12.05'], ],
    [['637.00', '711.00', '668.75', '26.15', '26.51', '26.33', '84.56', '86.47', '85.25', '12.06'], ],
    [['622.00', '699.00', '654.75', '28.60', '29.36', '29.09', '85.26', '86.08', '85.70', '12.05'], ],
    [['617.00', '692.00', '652.00', '28.16', '28.40', '28.25', '82.14', '82.59', '82.38', '12.06'], ],
    [['593.00', '666.00', '625.50', '24.20', '24.44', '24.32', '82.05', '82.45', '82.32', '12.05'], ],
    [['571.00', '634.00', '599.75', '23.90', '24.33', '24.14', '84.14', '85.06', '84.69', '12.05'], ],
    [['416.00', '574.00', '492.75', '27.52', '28.52', '28.16', '89.48', '89.84', '89.71', '12.05'], ],
    [['416.00', '574.00', '492.75', '27.52', '28.52', '28.16', '89.48', '89.84', '89.71', '12.05'], ],
    [['416.00', '574.00', '492.75', '27.52', '28.52', '28.16', '89.48', '89.84', '89.71', '12.05'], ],
    [['416.00', '574.00', '492.75', '27.52', '28.52', '28.16', '89.48', '89.84', '89.71', '12.05'], ],
    [['602.00', '783.00', '711.50', '37.95', '41.51', '38.87', '83.71', '87.12', '84.85', '12.05'], ],
    [['705.00', '734.00', '714.25', '27.50', '28.04', '27.68', '84.28', '84.73', '84.50', '12.06'], ],
    [['649.00', '690.00', '672.50', '23.14', '23.37', '23.24', '86.10', '87.14', '86.59', '12.07'], ],
    [['601.00', '650.00', '620.50', '21.94', '22.44', '22.22', '89.92', '90.41', '90.19', '12.05'], ],
    [['577.00', '645.00', '607.75', '23.95', '24.09', '24.02', '87.26', '88.58', '87.81', '12.06'], ],
    [['554.00', '637.00', '588.00', '23.41', '23.83', '23.63', '87.17', '87.76', '87.54', '12.06'], ],
    [['547.00', '628.00', '582.75', '23.05', '23.22', '23.10', '86.41', '87.62', '86.94', '12.06'], ],
    [['371.00', '519.00', '445.25', '27.24', '28.03', '27.74', '90.90', '91.28', '91.11', '12.05'], ],
    [['21.00',  '249.00', '115.25', '34.90', '36.24', '35.80', '92.27', '92.87', '92.61', '12.05'], ],
    [['21.00',  '249.00', '115.25', '34.90', '36.24', '35.80', '92.27', '92.87', '92.61', '12.05'], ],
    [['21.00',  '249.00', '115.25', '34.90', '36.24', '35.80', '92.27', '92.87', '92.61', '12.05'], ],
    [['692.00', '761.00', '720.50', '34.85', '36.43', '35.29', '82.67', '85.46', '84.61', '12.06'], ],
    [['628.00', '678.00', '648.25', '25.91', '26.57', '26.30', '88.55', '88.96', '88.82', '12.06'], ],
    [['558.00', '622.00', '585.25', '21.50', '21.80', '21.65', '87.17', '87.54', '87.42', '12.04'], ],
    [['567.00', '643.00', '601.00', '27.44', '27.72', '27.57', '85.01', '85.46', '85.33', '12.06'], ],
    [['566.00', '664.00', '605.50', '29.53', '31.12', '30.61', '86.78', '87.26', '87.04', '12.06'], ],
    [['366.00', '546.00', '453.75', '36.80', '37.73', '37.40', '89.15', '89.59', '89.37', '12.05'], ],
    [['488.00', '652.00', '566.50', '39.16', '39.46', '39.28', '87.03', '87.96', '87.50', '12.05'], ],
    [['623.00', '696.00', '652.75', '33.07', '33.46', '33.20', '83.38', '84.16', '83.80', '12.05'], ],
    [['605.00', '679.00', '638.00', '29.76', '29.95', '29.81', '83.66', '84.11', '83.90', '12.05'], ],
    [['585.00', '648.00', '612.25', '24.94', '25.26', '25.07', '81.63', '82.03', '81.85', '12.04'], ],
    [['560.00', '626.00', '590.25', '23.50', '23.65', '23.58', '82.73', '83.57', '83.17', '12.04'], ],
    [['536.00', '613.00', '570.75', '23.29', '24.41', '24.03', '87.88', '88.38', '88.14', '12.07'], ],
    [['561.00', '636.00', '594.00', '28.43', '28.64', '28.51', '84.14', '85.40', '84.67', '12.05'], ],
    [],
    [['557.00', '615.00', '585.50', '24.49', '24.65', '24.57', '82.05', '82.56', '82.40', '12.06'], ],
    [['535.00', '630.00', '574.75', '30.86', '31.93', '31.55', '87.03', '87.51', '87.29', '12.05'], ],
    [['535.00', '630.00', '574.75', '30.86', '31.93', '31.55', '87.03', '87.51', '87.29', '12.05'], ],
    [['535.00', '630.00', '574.75', '30.86', '31.93', '31.55', '87.03', '87.51', '87.29', '12.05'], ],
    [['461.00', '638.00', '537.25', '37.89', '38.59', '38.11', '87.71', '88.27', '87.98', '12.05'], ],
    [['591.00', '696.00', '635.00', '33.89', '34.08', '34.00', '87.06', '87.74', '87.47', '12.05'], ],
    [['625.00', '710.00', '662.75', '32.04', '32.17', '32.07', '86.36', '86.81', '86.67', '12.05'], ],
    [['631.00', '717.00', '668.75', '31.58', '31.81', '31.67', '84.64', '85.34', '85.05', '12.06'], ],
    [['637.00', '716.00', '671.50', '31.27', '31.45', '31.32', '84.53', '85.06', '84.84', '12.06'], ],
    [['639.00', '715.00', '673.00', '31.56', '31.88', '31.72', '84.44', '85.15', '84.87', '12.05'], ],
    [['651.00', '731.00', '683.25', '31.44', '31.63', '31.51', '83.29', '83.99', '83.68', '12.05'], ],
    [['644.00', '727.00', '680.75', '31.33', '31.53', '31.40', '82.93', '83.63', '83.34', '12.05'], ],
    [['658.00', '738.00', '693.25', '34.20', '35.08', '34.75', '84.64', '85.06', '84.93', '12.05'], ],
    [['502.00', '691.00', '583.25', '39.22', '39.40', '39.30', '87.54', '88.04', '87.89', '12.05'], ],
    [['675.00', '752.00', '709.00', '35.75', '36.33', '35.97', '82.64', '84.11', '83.25', '12.05'], ],
    [['620.00', '699.00', '654.00', '27.37', '27.54', '27.44', '83.77', '84.25', '84.08', '12.06'], ],
    [['605.00', '677.00', '640.25', '26.10', '26.27', '26.16', '84.02', '84.56', '84.34', '12.06'], ],
    [['602.00', '684.00', '637.00', '27.88', '28.07', '27.95', '83.32', '84.81', '83.93', '12.06'], ],
    [['603.00', '683.00', '635.50', '27.68', '27.88', '27.76', '82.53', '82.84', '82.69', '12.05'], ],
    [['605.00', '683.00', '638.25', '29.45', '29.91', '29.71', '84.16', '84.61', '84.48', '12.05'], ],
    [['615.00', '689.00', '646.50', '30.00', '30.30', '30.15', '82.19', '83.04', '82.64', '12.05'], ],
    [['597.00', '667.00', '625.75', '24.98', '25.54', '25.30', '83.32', '83.77', '83.58', '12.06'], ],
    [['589.00', '668.00', '629.25', '29.00', '29.60', '29.36', '83.32', '84.02', '83.71', '12.05'], ],
    [['121.00', '347.00', '220.50', '35.81', '36.94', '36.54', '89.97', '90.46', '90.28', '12.05'], ],
    [['121.00', '347.00', '220.50', '35.81', '36.94', '36.54', '89.97', '90.46', '90.28', '12.05'], ],
]
