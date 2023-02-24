# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    # TU C�DIGO AQU�
    group_words = {}
    for word in words: 
        first_letter = word[0]
        if first_letter not in group_words:
            group_words[first_letter] = []
        group_words[first_letter].append(word) 

    return group_words


if __name__ == '__main__':
    run(['mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco'])