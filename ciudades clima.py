# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            ("Lunes", 78),
            ("Martes", 80),
            ("Miércoles", 82),
            ("Jueves", 79),
            ("Viernes", 85),
            ("Sábado", 88),
            ("Domingo", 92)
        ],
        [   # Semana 2
            ("Lunes", 76),
            ("Martes", 79),
            ("Miércoles", 83),
            ("Jueves", 81),
            ("Viernes", 87),
            ("Sábado", 89),
            ("Domingo", 93)
        ],
        [   # Semana 3
            ("Lunes", 77),
            ("Martes", 81),
            ("Miércoles", 85),
            ("Jueves", 82),
            ("Viernes", 88),
            ("Sábado", 91),
            ("Domingo", 95)
        ],
        [   # Semana 4
            ("Lunes", 75),
            ("Martes", 78),
            ("Miércoles", 80),
            ("Jueves", 79),
            ("Viernes", 84),
            ("Sábado", 87),
            ("Domingo", 91)
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            ("Lunes", 62),
            ("Martes", 64),
            ("Miércoles", 68),
            ("Jueves", 70),
            ("Viernes", 73),
            ("Sábado", 75),
            ("Domingo", 79)
        ],
        [   # Semana 2
            ("Lunes", 63),
            ("Martes", 66),
            ("Miércoles", 70),
            ("Jueves", 72),
            ("Viernes", 75),
            ("Sábado", 77),
            ("Domingo", 81)
        ],
        [   # Semana 3
            ("Lunes", 61),
            ("Martes", 65),
            ("Miércoles", 68),
            ("Jueves", 70),
            ("Viernes", 72),
            ("Sábado", 76),
            ("Domingo", 80)
        ],
        [   # Semana 4
            ("Lunes", 64),
            ("Martes", 67),
            ("Miércoles", 69),
            ("Jueves", 71),
            ("Viernes", 74),
            ("Sábado", 77),
            ("Domingo", 80)
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            ("Lunes", 90),
            ("Martes", 92),
            ("Miércoles", 94),
            ("Jueves", 91),
            ("Viernes", 88),
            ("Sábado", 85),
            ("Domingo", 82)
        ],
        [   # Semana 2
            ("Lunes", 89),
            ("Martes", 91),
            ("Miércoles", 93),
            ("Jueves", 90),
            ("Viernes", 87),
            ("Sábado", 84),
            ("Domingo", 81)
        ],
        [   # Semana 3
            ("Lunes", 91),
            ("Martes", 93),
            ("Miércoles", 95),
            ("Jueves", 92),
            ("Viernes", 89),
            ("Sábado", 86),
            ("Domingo", 83)
        ],
        [   # Semana 4
            ("Lunes", 88),
            ("Martes", 90),
            ("Miércoles", 92),
            ("Jueves", 89),
            ("Viernes", 86),
            ("Sábado", 83),
            ("Domingo", 80)
        ]
    ]
]

# Función para convertir Fahrenheit Fº a Celsius Cº
def convertirFaC(f):
    return (f - 32) * 5.0 / 9.0

# Calculo de las ciudades
for i, ciudad in enumerate(temperaturas):
    print("Promedios de temperaturas para Ciudad {}:".format(i + 1))
    for j, semana in enumerate(ciudad):
        suma = sum(convertirFaC(dia[1]) for dia in semana)
        promedio = suma / len(semana)
        print("  Semana {}: {:.2f}°C".format(j + 1, promedio))