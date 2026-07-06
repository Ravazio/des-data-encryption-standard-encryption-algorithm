# Caio Cardoso dos Santos 11202021632
# Victor Ravazio de Lima 11201920941

from collections import deque

def int_to_bit_vector(number, size):
    # Converte um inteiro em uma lista de bits com tamanho fixo.
    binary_string = format(number, f'0{size}b')
    return [int(bit) for bit in binary_string]

def PC_1(k):
    # Aplica a permutação PC-1 conforme a convenção usada no slide.
    # A entrada é uma chave de 56 bits e a saída também possui 56 bits.
    keyp = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]

    result = [0] * 56

    for i in range(56):
        b = keyp[i]
        q = (b - 1) // 8
        b_minus_q = b - q
        result[i] = k[b_minus_q - 1]

    return result

def PC_2(k):
    # Seleciona 48 bits a partir da concatenação C_r || D_r.
    keyp = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

    return [k[b - 1] for b in keyp]

def left_shift(bits, shift):
    # Realiza rotação circular à esquerda de uma lista de bits.
    shifted = deque(bits)
    shifted.rotate(shift)
    return list(shifted)

def KeySchedule(k):
    # Gera as 16 subchaves de 48 bits usadas nas 16 rodadas do DES.
    k = PC_1(k)

    c = [k[:len(k) // 2]]
    d = [k[len(k) // 2:]]
    subkeys = []

    one_shift_rounds = [1, 2, 9, 16]

    for r in range(1, 17):
        shift = -1 if r in one_shift_rounds else -2
        c.append(left_shift(c[r - 1], shift))
        d.append(left_shift(d[r - 1], shift))
        subkeys.append(PC_2(c[r] + d[r]))

    return subkeys

def IP(m):
    # Permutação inicial aplicada ao bloco de 64 bits do plaintext.
    mp = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

    return [m[b - 1] for b in mp]

def XOR(a, b):
    # Calcula o XOR bit a bit entre duas listas de mesmo tamanho.
    if len(a) != len(b):
        return a
    return [0 if a[i] == b[i] else 1 for i in range(len(a))]

def P_inverse(m):
    # Aplica a permutação inversa da IP ao final da cifra.
    mp = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

    return [m[b - 1] for b in mp]

def bitfield(n):
    # Converte um inteiro de 0 a 15 para sua representação binária em 4 bits.
    return [int(digit) for digit in '{0:04b}'.format(n)]

def S(r, i):
    # Aplica a i-ésima S-box a um bloco de 6 bits.
    lines = r[:2] # A linha é formada pelos 2 primeiros bits
    columns = r[4:] # A coluna pelos 4 últimos bits
    
    # lines = [r[0], r[5]]   # linha = bits 1 e 6
    # columns = r[1:5]       # coluna = bits 2, 3, 4 e 5

    out_lines = 0
    for bit in lines:
        out_lines = (out_lines << 1) | bit

    out_columns = 0
    for bit in columns:
        out_columns = (out_columns << 1) | bit

    if i == 1:
        table = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    elif i == 2:
        table = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
    elif i == 3:
        table = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    elif i == 4:
        table = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    elif i == 5:
        table = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    elif i == 6:
        table = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    elif i == 7:
        table = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    else:
        table = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    result = table[out_lines][out_columns]
    return bitfield(result)

def F(j, r):
    # Função f do DES:
    # 1) expande R de 32 para 48 bits
    # 2) faz XOR com a subchave
    # 3) divide em 8 blocos de 6 bits
    # 4) aplica as S-boxes
    # 5) aplica a permutação P
    e = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]

    expanded_r = [r[b - 1] for b in e]
    expanded_r = XOR(expanded_r, j)

    blocks = [expanded_r[x:x + 6] for x in range(0, len(expanded_r), 6)]

    result = []
    for i in range(8):
        result += S(blocks[i], i + 1)

    p = [16, 7, 20, 21,
         29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2, 8, 24, 14,
         32, 27, 3, 9,
         19, 13, 30, 6,
         22, 11, 4, 25]

    return [result[p[i] - 1] for i in range(len(p))]

def DES(k, m):
    # Executa a cifra DES em um bloco de 64 bits usando chave de 56 bits.
    subkeys = KeySchedule(k)
    m = IP(m)

    l = [m[:len(m) // 2]]
    r = [m[len(m) // 2:]]

    for j in range(1, 17):
        l.append(r[j - 1])
        r.append(XOR(F(subkeys[j - 1], r[j - 1]), l[j - 1]))

    # Após 16 rodadas, o algoritmo deve usar R16 || L16.
    return P_inverse(r[16] + l[16])

def DES_decrypt(k, c):
    ki = KeySchedule(k)
    ki.reverse()

    c = IP(c)

    l = [c[:len(c)//2]]
    r = [c[len(c)//2:]]

    for j in range(1, 17):
        l.append(r[j-1])
        r.append(XOR(F(ki[j-1], r[j-1]), l[j-1]))

    return P_inverse(r[16] + l[16])

def main():
    k = 0b10010010010010010010010010010010010010010010010010010010 # Chave Caso 1
    # k = 0b10111011101111011110101110111101110111101011011101110111 # Chave Caso 2
    m = 0b1001001001001001001001001001001001001001001001001001001001001001

    k_size = k.bit_length()
    m_size = m.bit_length()

    k_vector = int_to_bit_vector(k, k_size)
    m_vector = int_to_bit_vector(m, m_size)

    result = DES(k_vector, m_vector)
    result_bits = ''.join(map(str, result))
    c_size = len(result)

    print(f"Chave K = {k:0b}")
    print(f"Tamanho da chave K = {k_size}")
    print(f"Mensagem Original M = {m:0b}")
    print(f"Tamanho da mensagem M = {m_size}")
    print(f"Mensagem Cifrada C = {result_bits}")
    print("Tamanho da mensagem cifrada C = ", c_size)
    
    c_decripty = DES_decrypt(k_vector,result)
    c_decripty_size = len(c_decripty)
    c_decripty_bits = ''.join(map(str, c_decripty))
    print(f"Mensagem Decifrada = {c_decripty_bits}")
    print("Tamanho da mensagem decifrada = ", c_decripty_size)
    print("Decifração correta?", c_decripty == m_vector)

if __name__ == "__main__":
    main()
