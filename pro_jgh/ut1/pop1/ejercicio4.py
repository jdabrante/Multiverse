# ut1-pop1-ej4
hexcolor = 'A131F7'
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓
hex_red = hexcolor[:2]
hex_green = hexcolor[2:4]
hex_blue = hexcolor[4:6]
dec_red = int(hex_red, 16)
dec_green = int(hex_green, 16)
dec_blue = int(hex_blue, 16)
rgb_color = f'({dec_red},{dec_green},{dec_blue})'
# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert rgb_color == '(161,49,247)'