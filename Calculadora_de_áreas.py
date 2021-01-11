# Calculadora de áreas com cada programa de cada tipo de área

# O que a variável final e tipo_de_area2 recebe, não importa, por isso eu coloquei'oi' e 'olá'

final = ('olá')
tipo_de_area2 = ('oi')
tipo_de_area2 = str(tipo_de_area2)

peso = 2
peso = int(peso)

print('Lhe darei algumas opções de tipos de areas!')
print('Você escolhe uma das opções e depois responde as perguntas sobre as medidas das suas figuras')
print('Esses são os tipos de áreas que você poderá escolher:')
print(' ')
print('OBS:Lembre-se de que você não pode errar a ortografia ou o programa não fará os seus calculos :( ')
print(' ')
print(' ')
print('Quadrado')
print('Retângulo')
print('Triângulo')
print('Trapézio')
print('Losango')
print('Paralelogramo')
print('Círculo')
print(' ')
print(' ')
tipo_de_area = input('Qual é o tipo de área que você quer? ')

if tipo_de_area.lower() == ('quadrado'):
  lado = input('Qual é o valor do lado do quadrado? ')
  lado = float(lado)
  area_do_quadrado = lado * lado 
  print(' ')
  print('Essa é a área do quadrado', area_do_quadrado)

if tipo_de_area.lower() == ('retângulo'):
  base = input('Qual é o valor da base do retângulo? ')
  altura = input('Qual é o valor da altura do retângulo? ')
  base = float(base)
  altura = float(altura)
  area_do_retangulo = base * altura
  print(' ')
  print('Essa é a área do retângulo', area_do_retangulo)

if tipo_de_area.lower() == ('triângulo'):
  base2 = input('Qual é o valor da base do triângulo? ')
  altura2 = input('Qual é o valor da altura do triângulo? ')
  base2 = float(base2)
  altura2 = float(altura2)
  area_do_triangulo = (base2 * altura2) / peso
  print(' ')
  print('Essa é a área do triângulo', area_do_triangulo)

if tipo_de_area.lower() == ('trapézio'):
  base_menor = input('Qual é o valor da base menor? ')
  base_maior = input('Qual é o valor da base maior? ')
  altura3 = input('Qual é a altura? ')
  base_menor = float(base_menor)
  base_maior = float(base_maior)
  altura3 = float(altura3)
  area_do_trapezio = (base_maior + base_menor) * ( altura3) / (peso)
  print(' ')
  print('Essa é a área do trapézio', area_do_trapezio)

if tipo_de_area.lower() == ('losango'):
  diagonal_menor = input('Qual é o valor da diagonal menor? ')
  diagonal_maior = input('Qual é o valor da diagonal maior? ')
  diagonal_maior = float(diagonal_maior)
  diagonal_menor = float(diagonal_menor)
  area_do_losango = (diagonal_maior * diagonal_menor) /(peso)
  print(' ')
  print('Essa é a área do losango', area_do_losango)
  
if tipo_de_area.lower() == ('paralelogramo'):
  base3 = input('Qual é o valor da base? ')
  altura4 = input('Qual é o valor da altura? ')
  base3 = float(base3)
  altura4 = float(altura4)
  area_do_paralelogramo = base3 * altura4
  print(' ')
  print("Essa é a área do paralelogramo", area_do_paralelogramo)

if tipo_de_area.lower() == ('círculo'):
  valor_de_pi = float(3.14)
  raio = input('Qual é o valor do raio? ')
  raio = float(raio)
  raio_ao_quadrado = (raio)**(peso)
  area_do_circulo = (valor_de_pi * raio_ao_quadrado)
  print(' ')
  print('Essa é a área do círculo', area_do_circulo)

if tipo_de_area.lower() != ('quadrado'):
  if tipo_de_area.lower() != ('retângulo'):
    if tipo_de_area.lower() != ('triângulo'):
      if tipo_de_area.lower() != ('trapézio'):
        if tipo_de_area.lower() != ('losango'):
          if tipo_de_area.lower() != ('paralelogramo'):
            if tipo_de_area.lower() != ('círculo'):
              print(' ')
              tipo_de_area2 = input('Você errou, porfavor digite novamente, igual os exemplos de cima :) ')


if tipo_de_area2.lower() == ('quadrado'):
   lado = input('Qual é o valor do lado do quadrado? ')
   lado = float(lado) 
   print(' ')
   print('Essa é a área do quadrado', area_do_quadrado)

if tipo_de_area2.lower() == ('retângulo'):
   base = input('Qual é o valor da base do retângulo? ')
   altura = input('Qual é o valor da altura do retângulo? ')
   base = float(base)
   altura = float(altura)
   area_do_retangulo = base * altura
   print(' ')
   print('Essa é a área do retângulo', area_do_retangulo)

if tipo_de_area2.lower() == ('triângulo'):
   base2 = input('Qual é o valor da base do triângulo? ')
   altura2 = input('Qual é o valor da altura do triângulo? ')
   base2 = float(base2)
   altura2 = float(altura2)
   area_do_triangulo = (base2 * altura2) / peso
   print(' ')
   print('Essa é a área do triângulo', area_do_triangulo)

if tipo_de_area2.lower() == ('trapézio'):
   base_menor = input('Qual é o valor da base menor? ')
   base_maior = input('Qual é o valor da base maior? ')
   altura3 = input('Qual é o valor da altura? ')
   base_menor = float(base_menor)
   base_maior = float(base_maior)
   altura3 = float(altura3)
   area_do_trapezio = (base_maior + base_menor) * ( altura3) / (peso)
   print(' ')
   print('Essa é a área do trapézio', area_do_trapezio)

if tipo_de_area2.lower() == ('losango'):
   diagonal_menor = input('Qual é o valor da diagonal menor? ')
   diagonal_maior = input('Qual é o valor da diagonal maior? ')
   diagonal_maior = float(diagonal_maior)
   diagonal_menor = float(diagonal_menor)
   area_do_losango = (diagonal_maior * diagonal_menor) /(peso)
   print(' ')
   print('Essa é a área do losango', area_do_losango)
  
if tipo_de_area2.lower() == ('paralelogramo'):
   base3 = input('Qual é o valor da base? ')
   altura4 = input('Qual é o valor da altura? ')
   base3 = float(base3)
   altura4 = float(altura4)
   area_do_paralelogramo = base3 * altura4
   print(' ')
   print('Essa é a área do paralelogramo', area_do_paralelogramo)

if tipo_de_area2.lower() == ('círculo'):
   valor_de_pi = float(3.14)
   raio = input('Qual é o valor do raio? ')
   raio = float(raio)
   raio_ao_quadrado = (raio)**(peso)
   area_do_circulo = (valor_de_pi * raio_ao_quadrado)
   print(' ')
   print('Essa é a área do círculo', area_do_circulo)

if tipo_de_area2.lower() != ('quadrado'):
  if tipo_de_area2.lower() != ('retângulo'):
    if tipo_de_area2.lower() != ('triângulo'):
      if tipo_de_area2.lower() != ('trapézio'):
        if tipo_de_area2.lower() != ('losango'):
          if tipo_de_area2.lower() != ('paralelogramo'):
            if tipo_de_area2.lower() != ('círculo'):
              if tipo_de_area2 != ('oi'):
                final = ('Você errou duas vezes, por favor reinicie o programa para tentar novamente ')
                print(' ')
                print(' ')
                print(final)

if final == ('olá'):
  final2 = ('Você terminou o programa, se você quiser fazer outro calculo, por favor reinicie')
  print(' ')
  print(' ')
  print(final2)

# Criado por JoseRennan
# Data 10/01/2021 e 11/01/2021
# Espero que goste e em caso de uso que dê meus créditos no github
