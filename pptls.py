reglas = {"🗿": ["✂️", "🦎"],
          "📄": ["🗿", "🖖"],
          "✂️": ["📄", "🦎"],
          "🦎": ["🖖", "📄"],
          "🖖": ["🗿", "✂️"]}


def juego(jugadas):
    puntuacion_p1 = 0
    puntuacion_p2 = 0

    for juga in jugadas:
        juego_p1 = juga[0]
        juego_p2 = juga[1]

        if juego_p1 != juego_p2:
            if juego_p1 in reglas[juego_p2]:
                puntuacion_p2 += 1
            else:
                puntuacion_p1 += 1

    return print("Tie" if puntuacion_p1 == puntuacion_p2
                 else "Player 1" if puntuacion_p1 > puntuacion_p2 else "Player 2")


juego([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")])
juego([("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿")])
juego([("🖖", "🗿"), ("✂️", "📄"), ("🗿", "🗿"), ("🦎", "🖖")])
