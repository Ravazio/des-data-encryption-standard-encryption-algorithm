# Implementação do DES em Python

Projeto em **Python** que implementa uma versão educacional do algoritmo **DES (Data Encryption Standard)**, incluindo geração de subchaves, cifragem e decifragem de blocos binários.

## Sobre o projeto

Este programa reproduz a estrutura clássica do DES com foco didático, implementando manualmente as principais etapas do algoritmo em nível de bits. O código trabalha com vetores binários e executa o fluxo completo de criptografia e descriptografia, permitindo observar o funcionamento interno do algoritmo sem depender de bibliotecas externas.

A implementação inclui permutações, expansão de blocos, aplicação de S-boxes, XOR entre blocos, geração de subchaves e as 16 rodadas da rede de Feistel usada pelo DES. Ao final, o programa também verifica se a mensagem decifrada corresponde à mensagem original.

## Funcionalidades

- Conversão de inteiros para vetores de bits 
- Geração de subchaves com **Key Schedule** 
- Permutação inicial (**IP**) 
- Permutação final inversa (**IP⁻¹**, implementada como `P_inverse`) 
- Expansão do bloco direito de 32 para 48 bits 
- Operação XOR bit a bit 
- Aplicação das **8 S-boxes** do DES 
- Função `F` da rede de Feistel 
- Cifragem de um bloco de 64 bits 
- Decifragem do bloco cifrado com subchaves em ordem inversa 

## Estrutura do algoritmo

O arquivo implementa os principais componentes do DES em funções separadas:

| Função | Papel |
|---|---|
| `int_to_bit_vector` | Converte números inteiros em listas de bits  |
| `PC_1` | Aplica a permutação inicial da chave para o key schedule  |
| `PC_2` | Seleciona 48 bits da concatenação das metades da chave  |
| `left_shift` | Realiza rotações circulares nas metades da chave  |
| `KeySchedule` | Gera as 16 subchaves usadas nas rodadas  |
| `IP` | Aplica a permutação inicial ao bloco de entrada  |
| `P_inverse` | Aplica a permutação final inversa  |
| `S` | Aplica uma S-box a um bloco de 6 bits  |
| `F` | Executa a função de rodada do DES  |
| `DES` | Realiza a cifragem do bloco  |
| `DES_decrypt` | Realiza a decifragem do bloco  |

## Como funciona

O programa recebe uma chave e uma mensagem em formato binário, converte ambas em vetores de bits e executa a cifra DES em 16 rodadas. Em seguida, usa o mesmo bloco cifrado como entrada para a função de decifragem, invertendo a ordem das subchaves para reconstruir a mensagem original.

No `main()`, o código define exemplos fixos de chave e mensagem, imprime os tamanhos dos blocos e mostra a mensagem cifrada, a mensagem decifrada e a confirmação de que a decifragem foi bem-sucedida.

## Execução

### Pré-requisitos

- Python 3
- Nenhuma biblioteca externa além da biblioteca padrão 

### Rodar o programa

```bash
python des.py
```

## Exemplo de saída esperada

A execução imprime informações como:

- chave utilizada;
- tamanho da chave;
- mensagem original;
- mensagem cifrada;
- mensagem decifrada;
- verificação final indicando se a decifragem recuperou corretamente a mensagem original.

## Objetivo educacional

Esta implementação é adequada para estudo de **criptografia clássica**, **redes de Feistel** e manipulação de bits em Python. Como o algoritmo foi escrito de forma explícita e modular, o projeto facilita a inspeção de cada etapa do DES e serve como material prático para disciplinas de segurança, criptografia ou teoria da computação.

## Autores

- **Caio Cardoso dos Santos** — RA 11202021632 
- **Victor Ravazio de Lima** — RA 11201920941 
