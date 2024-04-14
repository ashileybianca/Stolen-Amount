from sys import argv, exit

''' Algoritmos e Estruturas de Dados II
    - Trabalho I
    - Integrantes: Ashiley Bianca e Bernardo Nilson
'''

def read_text_file(file_path):
    # Lê o arquivo de texto para teste.
    with open(file_path) as file:
        text = file.readlines()
    
    text = remove_empty_lines(text) # limpa todos os \n do texto
    return text

def remove_empty_lines(text):
    # Remove os '\n'.
    return [line.rstrip('\n') for line in text if line.strip()]

def build_matrix(text):
    # Constrói a matriz de caracteres.
    matrix = []
    for line in text:
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)
    return matrix

def find_start_position(matrix):
    # Retorna a posição inicial para iniciar a caminhada na matriz.
    for row_index, row in enumerate(matrix):
        if row[0] == '-': # Sempre estará na coluna 0, e será um '-', devemos verificar em qual linha.
            return row_index
    return -1

def move(line, column, direction):
    # Definição de como os movimentos devem ser executados.
    if direction['up']:
        return line - 1, column
    elif direction['down']:
        return line + 1, column
    elif direction['right']:
        return line, column + 1
    else:
        return line, column - 1

def calculate_stolen_amount(matrix):
    # Função principal que realiza todo o algoritmo.
    stolen_amount = 0
    direction = {
        'up': False,
        'down': False,
        'right': True,
        'left': False
    }
    start_position_index = find_start_position(matrix)
    content_position = matrix[start_position_index][0]
    number_str = ''

    line = start_position_index
    column = 0
    
    while content_position != '#':
        while content_position != '/' and content_position != '\\' and content_position !='#':
            if content_position.isdigit():
                number_str += content_position
            else:
                if len(number_str) != 0:
                    number = int(number_str)
                    stolen_amount += number
                    number_str = ''

            line, column = move(line, column, direction)
            content_position = matrix[line][column]

        # Antes de testar '/' e '\', converta o número (se houver).
        if len(number_str) != 0:
            number = int(number_str)
            stolen_amount += number
            number_str = ''

        # Opções com '/'
        if content_position == '/':
            if direction['up']:
                direction['up'] = False
                direction['right'] = True

            elif direction['down']:
                direction['down'] = False
                direction['left'] = True

            elif direction['right']:
                direction['right'] = False
                direction['up'] = True

            elif direction['left']:
                direction['left'] = False
                direction['down'] = True

        # Opções com '\'
        if content_position == '\\':
            if direction['up']:
                direction['up'] = False
                direction['left'] = True

            elif direction['down']:
                direction['down'] = False
                direction['right'] = True

            elif direction['right']:
                direction['right'] = False
                direction['down'] = True

            elif direction['left']:
                direction['left'] = False
                direction['up'] = True

        if(content_position == '#'):
            break

        line, column = move(line, column, direction)
        content_position = matrix[line][column]

    return stolen_amount


try:
    file_path = argv[1] 
    text = read_text_file(file_path)
    if not file_path.lower().endswith('.txt'):
        raise ValueError("O arquivo fornecido não é um arquivo .txt!")
except IndexError:
    print("Você precisa fornecer o caminho de um arquivo!")
    exit()
except FileNotFoundError:
    print("Caminho não encontrado. Verifique o caminho e tente novamente.")
    exit()
except ValueError as ve:
    print(ve)
    exit()
except Exception as e:
    print(f"Erro: {e}")
    exit()

matrix = build_matrix(text)

stolen_amount = calculate_stolen_amount(matrix)

print(f"Stolen amount: {stolen_amount}")