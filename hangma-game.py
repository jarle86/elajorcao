import random
import os

def clear_screen():
  """Clears the screen depending on the OS."""
  # For Windows
  if os.name == 'nt':
    os.system('cls')
  # For Mac and Linux
  else:
    os.system('clear')

def draw_hangman(number_failed):
    
    HANGMANPICS = [r"""
    +---+
    |   |
        |
        |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
        |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========""", r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========="""]
    print(HANGMANPICS[number_failed])

def pick_word():
    word_list= [
    "mesa", "silla", "cama", "armario", "estante", "sofá", "alfombra",
    "cortina", "lámpara", "espejo", "cuadro", "televisor", "computadora",
    "teléfono", "celular", "tablet", "reloj", "calendario", "cuaderno",
    "bolígrafo", "lápiz", "goma", "sacapuntas", "carpeta",
    "mochila", "libro", "revista", "periódico", "plato", "vaso", "cuchara",
    "tenedor", "cuchillo", "servilleta", "mantel", "olla", "sartén",
    "cacerola", "tapa", "vaso medidor", "cuchara medidora", "tabla",
    "cuchillo", "rallador", "exprimidor", "batidora", "tostadora",
    "cafetera", "licuadora", "microondas", "nevera", "lavadora", "secadora",
    "plancha", "aspiradora", "escoba", "fregona", "cubo", "bayeta",
    "jabón", "detergente", "esponja", "cepillo", "toalla", "ropa",
    "zapatos", "bolso", "sombrero", "bufanda", "guantes", "gafas",
    "joyas", "llaves", "monedas", "billete", "tarjeta",
    "carnet", "pasaporte", "billete", "billete", "entrada", "entrada",
    "libro", "carné", "carné", "tarjeta", "sello", "sobre", "carta",
    "paquete", "regalo", "fotografía", "música", "película", "libro",
    "videojuego", "aplicación", "herramienta", "juguete", "mascota",
    "planta", "comida", "bebida", "medicina", "producto", "material",
    "equipo", "instrumento"]

    get_numbe = random.randrange(0,100)

    word = word_list[get_numbe]

    return word

word = pick_word()

def evaluate_word(p):
    if p in word:
        return True
    return False

list_correct = []
list_wrong = []
i = [0]
clear_screen()

'''def word_constructor(i = i, list_correct = list_correct):
        for i,b in word[i]:
             print(b)'''


def word_constructor(i=i,word = word):
    for b in i:
        word_guessed = word[b]
        print(word_guessed)

#while loop here
while len(word) <= len(list_correct) or len(list_wrong) < 7:
    #get the beggining and the end of the picked word
    word_set = word[0] + ((len(word)-2) * '_') + word[-1]
    print(word_set)
    p = str(input("guess a letter: "))

    print(len(word), len(list_correct), len(list_wrong))

    if evaluate_word(p):
        i.append(word.index(p))
        i = list(dict.fromkeys(i))
        print(i)
        list_correct.append(p)
    else:
        list_wrong.append(p)
        draw_hangman(len(list_wrong) -1)
    word_constructor(i, word)

print(word)