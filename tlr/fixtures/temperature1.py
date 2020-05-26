raw_data = [
    b'\x1cT#01 61.01,\r\nT#03 88.07,90.78,90.17,29.48,14.41\r\n \r\n \xae$\xe2\x02\xe0D\x143P\x02\xe0',
    b'T#01 56.92,\r\nT#03 88.10,90.62,90.42,29.68,14.39\r\n \r\n C \xfc',
    b'T#01 63.51,\r\nT#03 87.98,90.36,90.15,29.30,14.41\r\n \r\n \x03\x82\x01\x80$\x9f\xd8\xbc\x0f\x08',
    b'T#01 56.05,\r\nT#03 87.99,90.66,90.52,29.00,14.40\r\n \r\n \x080"',
    b'T#01 59.20,\r\nT#03 88.17,91.09,90.62,28.79,14.41\r\n \r\n \x803\x06\x18\xf8',
    b'T#01 52.21,\r\nT#03 87.93,90.57,90.56,28.65,14.40\r\n \r\n \xf83\x0b\x1c',
    b'T#01 49.17,\r\nT#03 87.75,90.50,90.40,28.24,14.41\r\n \r\n :\x02@\x8c\x06',
    b'T#01 45.93,\r\nT#03 87.86,91.08,90.75,27.81,14.42\r\n \r\n \x01\x80\xa1s\x86\xe7\x03\xfc',
    b'T#01 50.86,\r\nT#03 87.79,90.61,90.53,27.23,14.43\r\n \r\n \x86\x16 \x80\xf0\xc7\xf2\xc0',
    b'\x1e\x80\xf8T#01 47.12,\r\nT#03 87.54,90.59,90.41,26.66,14.42\r\n \r\n \xf1\x17a\x80\x02\xfe',
    b'T#01 50.26,\r\nT#03 87.60,90.97,90.42,26.95,14.40\r\n \r\n \xc0\xf3[\xd3\x81\xfc9\xf5\xb8\x06\x80\xfe',
    b'T#01 57.21,\r\nT#03 87.64,90.55,90.13,25.40,14.42\r\n \r\n \x04\x08\x93\x98\xd9\xfc',
    b'T#01 54.55,\r\nT#03 87.86,90.88,90.43,25.55,14.40\r\n \r\n \x01\x80\t\x18\xc6!`\xfe',
    b'#01 53.39,\r\nT#03 87.89,90.84,90.12,25.71,14.41\r\n \r\n \x01(\x12 \xfe',
    b'T#01 52.59,\r\nT#03 88.06,90.75,90.29,26.29,14.40\r\n \r\n \xf2\x83l\x1e<\x90\x04',
    b'\xfeT#01 54.47,\r\nT#03 87.93,90.83,90.04,26.48,14.41\r\n \r\n k|^y\xfe',
    b'T#01 55.85,\r\nT#03 87.83,90.89,90.51,26.45,14.42\r\n \r\n \xc4\xd6>4\xfa',
    b'T#01 52.55,\r\nT#03 87.59,90.84,90.53,25.37,14.42\r\n \r\n \x02:\\@\x84G\x01\x84',
    b'T#01 54.72,\r\nT#03 87.76,90.86,90.25,25.36,14.40\r\n \r\n \x90\x80B\xc8;\x80\x0e\x80',
    b'T#01 54.70,\r\nT#03 87.78,90.64,90.08,25.54,14.40\r\n \r\n \x88P\xc2\x06',
    b'T#01 55.10,\r\nT#03 87.96,90.90,90.54,26.46,14.41\r\n \r\n @\xf0kT\xfc',
    b'T#01 53.83,\r\nT#03 87.90,90.91,90.32,25.77,14.42\r\n \r\n \x12\x0e"\xf2 \xbb\x0f\x80',
    b'T#01 54.64,\r\nT#03 87.99,90.50,90.26,26.15,14.43\r\n \r\n ',
    b'T#01 53.13,\r\nT#03 87.85,91.07,90.40,25.94,14.43\r\n \r\n \x80\xf8',
    b'T#01 60.26,\r\nT#03 87.62,91.09,90.31,25.16,14.42\r\n \r\n \x18A\x04',
    b'T#01 56.29,\r\nT#03 87.71,91.03,90.17,24.70,14.40\r\n \r\n "\xc8H\xc0',
    b'T#01 66.20,\r\nT#03 87.77,91.03,90.26,24.44,14.40\r\n \r\n  ',
    b'T#01 57.08,\r\nT#03 87.82,91.13,90.22,24.22,14.40\r\n \r\n \x01\x02\x80@\x04',
    b'T#01 61.81,\r\nT#03 87.69,91.07,90.28,24.03,14.40\r\n \r\n \xf3',
    b'T#01 59.01,\r\nT#03 87.73,90.70,90.07,23.99,14.42\r\n \r\n @\xfc',
    b'T#01 56.05,\r\nT#03 87.69,91.02,90.36,24.32,14.40\r\n \r\n \xa0\x8f\x0b\x07\x01',
    b'T#01 63.64,\r\nT#03 87.72,90.99,90.34,24.45,14.41\r\nT#01 64.58,\r\n \r\n \xfe',
    b'\xfcT#01 67.45,\r\nT#03 87.80,90.83,90.22,24.52,14.42\r\n \r\n \x02\x04\xfe ,@\xa3\x03',
    b'T#01 60.04,\r\nT#03 87.69,90.80,90.57,24.98,14.41\r\n \r\n \xe0\x01\x14',
    b'T#01 59.57,\r\nT#03 87.72,90.96,90.57,25.91,14.42\r\n \r\n \x01\xe4s\xe10D\x03\xe0',
    b'T#01 61.67,\r\nT#03 87.73,91.05,90.40,26.04,14.42\r\n \r\n \xe0\xfa\xe2\xc8\x84\x1e',
    b'\x12\xf8T#01 85.78,\r\nT#03 87.71,91.21,90.41,25.67,14.39\r\n \r\n 2\x011\x95\x89\x80\r\xf0',
    b'T#01 69.74,\r\nT#03 87.91,90.97,90.49,25.24,14.42\r\n \r\n \xf0',
    b'T#01 65.01,\r\nT#03 87.93,90.61,90.60,25.28,14.41\r\n \r\n \x01\xf3HB',
    b'T#01 63.63,\r\nT#03 87.97,90.90,90.92,26.12,14.40\r\n \r\n \xfe',
    b'T#01 61.84,\r\nT#03 88.17,91.13,90.78,26.92,14.42\r\n \r\n \x80H\xf0',
    b'T#01 65.72,\r\nT#03 87.72,90.93,90.51,26.14,14.40\r\n \r\n \xfe1\x8e',
    b'T#01 61.01,\r\nT#03 87.61,90.94,90.65,25.93,14.40\r\n \r\n \x02\x1cH\xe0',
    b'T#01 60.10,\r\nT#03 87.62,90.97,90.60,25.87,14.39\r\n \r\n \xf1',
    b'T#01 61.83,\r\nT#03 87.83,91.03,90.29,25.60,14.43\r\n \r\n \xf8\xe8',
    b'T#01 65.53,\r\nT#03 88.13,90.71,90.49,25.44,14.42\r\n \r\n \xc7a"\x12\x04',
    b'T#01 67.88,\r\nT#03 87.83,91.02,90.20,25.28,14.42\r\n \r\n 0\x07@\x12D',
    b'T#01 77.61,\r\nT#03 87.68,91.06,90.27,24.85,14.42\r\n \r\n  \x800\xfb\x02\xdc\x03\x01\x1e',
    b'T#01 67.28,\r\nT#03 87.94,91.08,90.61,24.95,14.40\r\n \r\n \xc0|\xdb\xe8g<',
    b'T#01 63.90,\r\nT#03 87.86,90.98,90.53,24.97,14.43\r\n \r\n \xc7\x02\x80',
    b'T#01 60.11,\r\nT#03 87.76,90.91,90.52,25.06,14.40\r\n \r\n ',
    b'T#01 66.12,\r\nT#03 87.65,90.85,90.69,25.25,14.42\r\n \r\n \xe0\x02\x80X\t\x04@',
    b'T#01 71.97,\r\nT#03 87.81,90.91,90.32,25.65,14.42\r\n \r\n \xc8\x06\x047',
    b'T#01 66.58,\r\nT#03 87.79,91.06,90.35,25.46,14.43\r\n \r\n `\x80\x88\xa4\xfc',
    b'T#01 58.96,\r\nT#03 87.32,90.92,90.27,25.17,14.39\r\n \r\n \x08\xfa',
    b'T#01 58.30,\r\nT#03 87.23,90.91,90.43,24.80,14.41\r\n \r\n  ',
    b'T#01 56.55,\r\nT#03 87.35,90.98,90.50,24.71,14.39\r\n \r\n \xf8<-\x0c',
    b'T#01 58.05,\r\nT#03 87.40,90.91,90.18,24.76,14.41\r\n \r\n \x05',
    b'T#01 76.65,\r\nT#03 87.64,91.03,90.22,24.38,14.42\r\n \r\n `\x81\xc2\xc0#\x0c\x1c',
    b'T#01 65.58,\r\nT#03 87.69,90.56,90.21,24.26,14.40\r\n \r\n \xc8',
    b'T#01 62.54,\r\nT#03 87.65,90.73,90.48,24.64,14.42\r\n \r\n \x0e7\x124\r\xfe',
    b'T#01 62.07,\r\nT#03 87.48,90.98,90.17,25.01,14.42\r\n \r\n \x80\xfea\x92\xc4\xae',
    b'T#01 63.46,\r\nT#03 87.52,91.04,90.37,24.83,14.40\r\n \r\n \x80\xc0',
    b'T#01 60.82,\r\nT#03 87.18,90.87,90.26,24.67,14.39\r\n \r\n \x03?h\x04\xb1\x98\t\x80\x0f\x81\x01\x80',
    b'T#01 54.87,\r\nT#03 87.27,90.85,90.50,24.82,14.41\r\n \r\n \xfc(\x04B\x1c\xf0',
    b'T#01 73.36,\r\nT#03 87.56,90\xfc\x04\x01\x12\x12\xf5\x1e0\x01\x80',
    b'T#01 71.44,\r\nT#03 87.76,91.00,90.31,24.82,14.14\r\n \r\n \xc0t',
    b'T#01 64.59,\r\nT#03 87.24,91.05,90.08,24.17,14.42\r\n \r\n \x02\xe0',
    b'T#01 72.30,\r\nT#03 87.32,91.08,90.14,23.47,14.42\r\n \r\n @H\x80\x01\xa0\x19\x15\x03',
    b'T#01 65.38,\r\nT#03 87.48,90.94,90.24,23.25,14.44\r\n \r\n \x03\x10\x06\x85l0\x18',
    b'T#01 64.02,\r\nT#03 87.45,90.98,90.18,22.97,14.42\r\n \r\n \x80\xfe\x1b',
    b'\x01\xf9T#01 87.72,\r\nT#03 87.60,91.12,90.06,22.60,14.27\r\n \r\n \x80\xf8\x8c\x10\x8b',
    b'T#01 80.09,\r\nT#03 87.47,91.07,89.97,22.08,14.09\r\nT#01 86.17,\r\nT#03 87.47,91.09,90.05,21.94,14.04\r\n \r\n \xfcM\x06D\x06',
    b'T#01 67.42,\r\nT#03 87.45,91.03,90.00,21.38,14.42\r\n \r\n \xfd9P\x0c\\\x04',
    b'T#01 72.79,\r\nT#03 87.40,91.07,90.09,20.90,14.13\r\n \r\n \xc1\x03',
    b'T#01 72.22,\r\nT#03 87.66,91.27,90.00,20.44,13.91\r\n \r\n \x10\x10\x80\x0c\xd0t\xc4\x17\x0c\x80',
    b'T#01 71.30,\r\nT#03 87.56,91.18,90.11,20.04,13.76\r\n \r\n \x01\xea',
    b'T#01 83.55,\r\nT#03 87.52,90.96,89.86,19.28,13.64\r\n \r\n \xf4',
    b'T#01 77.06,\r\nT#03 87.75,91.30,90.21,18.97,13.49\r\n \r\n \xa0\x8a&\x02',
    b'T#01 79.01,\r\nT#03 87.55,91.02,90.12,18.57,13.39\r\n \r\n \x0c\x03\x03\xc0\xe1\x80 \xfc',
    b'T#01 91.21,\r\nT#03 87.67,91.03,90.01,18.39,13.28\r\n \r\n \xe6\x19\xd0\x01\xd0',
    b'T#01 89.87,\r\nT#03 88.16,91.20,90.12,18.07,13.16\r\n \r\n \xe0\xc4\x90\xc2\x03\xf0',
    b'T#01 89.64,\r\nT#03 87.91,90.82,89.80,17.45,13.08\r\n \r\n \x02\x02\x13\xc0c\xc8\x19\xfc',
    b'T#01 88.11,\r\nT#03 87.94,90.98,89.85,17.33,13.01\r\n \r\n \x80\r\x18\xfe',
    b'T#01 89.66,\r\nT#03 87.88,91.42,89.75,17.03,12.96\r\n \r\n  \xc0x\x80\x08\xbd\x0f',
    b'T#01 92.55,\r\nT#03 87.94,90.80,89.64,16.70,12.93\r\n \r\n \xfev\xa9\x04',
    b'T#01 88.17,\r\nT#03 87.94,91.15,89.74,16.60,12.93\r\n \r\n \x050\x89\xc1\x81\xe7V\x06&',
    b'T#01 92.07,\r\nT#03 87.76,90.92,89.62,16.64,12.93\r\n \r\n \xfc\x01<\xe0\x08\x04',
    b'T#01 89.57,\r\nT#03 87.67,90.97,89.57,16.57,12.93\r\n \r\n \x01"\x80\x04\xfe',
    b'T#01 88.74,\r\nT#03 88.18,91.11,90.09,16.61,12.93\r\n \r\n \x03\x060\xfe\x8f\x97\x0e\x170\x01\xc0',
    b'T#01 88.81,\r\nT#03 87.98,90.89,89.86,16.19,12.95\r\n \r\n \xf0\x85\x0e8\xe8\x03',
    b'T#01 95.93,\r\nT#03 87.88,90.96,90.01,16.06,12.96\r\n \r\n \xfa',
    b'\xf8T#01 92.55,\r\nT#03 87.87,90.92,90.17,15.88,12.96\r\n \r\n \xc9\x08,',
    b'T#01 93.25,\r\nT#03 87.74,90.88,89.86,15.81,12.96\r\n \r\n \xfe%m\x03\x91\x0f',
    b'\x0c\xc0T#01 94.89,\r\nT#03 87.81,91.07,89.78,15.67,12.96\r\n \r\n \x01\xfa0\x08',
    b'T#01 92.07,\r\nT#03 87.87,90.94,89.96,15.63,12.96\r\n \r\n \xfe\x0b\xe0\xc3',
    b'T#01 97.30,\r\nT#03 87.75,91.06,90.04,15.38,12.96\r\n \r\n \x02@',
    b'T#01 95.69,\r\nT#03 87.68,91.04,89.88,15.24,12.96\r\n \r\n \x900\xe4',
    b'T#01 95.21,\r\nT#03 87.78,90.99,89.73,15.18,12.96\r\n \r\n C\xfe\x1cD\n\x89\x81',
    b'T#01 91.75,\r\nT#03 87.90,90.96,89.65,15.18,12.96\r\n \r\n @\xf2,A',
]

clean_data = [
    [['61.01', ], ],
    [['56.92', ], ],
    [['63.51', ], ],
    [['56.05', ], ],
    [['59.20', ], ],
    [['52.21', ], ],
    [['49.17', ], ],
    [['45.93', ], ],
    [['50.86', ], ],
    [['47.12', ], ],
    [['50.26', ], ],
    [['57.21', ], ],
    [['54.55', ], ],
    [['53.39', ], ],
    [['52.59', ], ],
    [['54.47', ], ],
    [['55.85', ], ],
    [['52.55', ], ],
    [['54.72', ], ],
    [['54.70', ], ],
    [['55.10', ], ],
    [['53.83', ], ],
    [['54.64', ], ],
    [['53.13', ], ],
    [['60.26', ], ],
    [['56.29', ], ],
    [['66.20', ], ],
    [['57.08', ], ],
    [['61.81', ], ],
    [['59.01', ], ],
    [['56.05', ], ],
    [['63.64', ], ['64.58', ], ],
    [['67.45', ], ],
    [['60.04', ], ],
    [['59.57', ], ],
    [['61.67', ], ],
    [['85.78', ], ],
    [['69.74', ], ],
    [['65.01', ], ],
    [['63.63', ], ],
    [['61.84', ], ],
    [['65.72', ], ],
    [['61.01', ], ],
    [['60.10', ], ],
    [['61.83', ], ],
    [['65.53', ], ],
    [['67.88', ], ],
    [['77.61', ], ],
    [['67.28', ], ],
    [['63.90', ], ],
    [['60.11', ], ],
    [['66.12', ], ],
    [['71.97', ], ],
    [['66.58', ], ],
    [['58.96', ], ],
    [['58.30', ], ],
    [['56.55', ], ],
    [['58.05', ], ],
    [['76.65', ], ],
    [['65.58', ], ],
    [['62.54', ], ],
    [['62.07', ], ],
    [['63.46', ], ],
    [['60.82', ], ],
    [['54.87', ], ],
    [['73.36', ], ],
    [['71.44', ], ],
    [['64.59', ], ],
    [['72.30', ], ],
    [['65.38', ], ],
    [['64.02', ], ],
    [['87.72', ], ],
    [['80.09', ], ['86.17', ], ],
    [['67.42', ], ],
    [['72.79', ], ],
    [['72.22', ], ],
    [['71.30', ], ],
    [['83.55', ], ],
    [['77.06', ], ],
    [['79.01', ], ],
    [['91.21', ], ],
    [['89.87', ], ],
    [['89.64', ], ],
    [['88.11', ], ],
    [['89.66', ], ],
    [['92.55', ], ],
    [['88.17', ], ],
    [['92.07', ], ],
    [['89.57', ], ],
    [['88.74', ], ],
    [['88.81', ], ],
    [['95.93', ], ],
    [['92.55', ], ],
    [['93.25', ], ],
    [['94.89', ], ],
    [['92.07', ], ],
    [['97.30', ], ],
    [['95.69', ], ],
    [['95.21', ], ],
    [['91.75', ], ],
]
