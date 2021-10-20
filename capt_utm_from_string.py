"""
****************************************************
Nelson Buainain – Maio, 2021
nnbuainain@gmail.com
Instituto Nacional de Pesquisas da Amazônia - Manaus
****************************************************

Função feita para extrair coordenadas em formato UTM de arquivo de texto corrido

A função irá capturar coordenadas e colocar em colunas separadas por lat e long, toda vez que
aparecerem coordenadas na seguinte formatação:

E: 338.616,208 , lendo-se 'E:, espaço, uma sequencia de numeros, ponto, uma sequencia de numeros, virgula, uma sequencia de numeros'

N: 8.847.908,541 , lendo-se com uma lógica semelhante a aplica a cima

Caso as coordenadas não estejam nessa formatação, a função deverá ser adaptada.

Antes de iniciar, vá à um editor de texto (ex: Text Wrangler), abra o arquivo onde estão as coordenadas a serem extraídas
e abra a caixa de find and replace (cmd + f), marque a caixinha de 'grep' para poder usar expressões regulares
em find digite \n e em replace de um espaço em branco. Clique em 'Replace all'. Isso irá substituir
todas as ocorrências de \n ('pula uma linha') por espaço em branco, colocando todo texto em uma linha só.

Feito isso, dê inicio à função.

Para executar a função você precisa ter o python instalado. Abra um terminal na pasta onde se encontra
o arquivo .txt e digite python capt_utm_from_string.py para executar o script.py

**OBS: Possivelmente na hora de copiar e colar o texto do pdf pra txt, um cabeçalho, ou algo do tipo,
ficara dentro das coordenadas exemplo:

'E: 33 ESTE É UM CABEÇALHO ALEATÓRIO 8.616,208'

A função falhará nessas ocasiões e isso deverá ser consertado manualmente.

a linha de código 'print(len(E))' devolverá o número de ocorrências de latitude que foram encontrados
Se o número não bater com o número final de vértices descrito no texto, algo de errado ocorreu e deve
ser inspecionado manualmente. O mesmo ocorre com as longitudes.


"""

import re #importar o modulo regular expression
with open('text_public_doc.txt','r') as string: #abrir o arquivo que tem o texto em que estão as cordenadas, substituir coordenadas_rita.txt pelo nome do arquivo em que se encontram as coordenadas.
    with open('coords_results.txt', 'w+') as coords: # vou dar um nome ao arquivo em que vão ser armazenadas as coordenadas, pode substitui pelo nome que quiser

        text = string.read() #ler o arquivo de texto de entrada e armazenar todo oo texto em uma variavel chamada text

        #agora vamos buscar os padrões de repetição de texto das coords que podem ser caputaradas
        #nesse caso é E: 338.616,208
        #ou seja E: uma sequencia de numeros, ponto, seq de numeros, virgula, seq de numeros

        E = re.findall("E:\s\d*.\d*,\d*", text) #buscar a ocorrencia de E: seguido de espaço (\s), uma sequencia de numeros (\d*), o ponto (.), outra sequencia de numeros (\d*), virgula (,) e outra sequencia de numeros (\d*). Por fim, armazena todas as vezes que ele encontrar esse padrão em uma variavel chamada E
        print(E) #imprimir na tela as ocorrencias que foram capturadas
        print(len(E)) #ver o numero de ocorrencias que foram capturadas

        N = re.findall("N:\s\d*.\d*.\d*,\d*", text) #buscar basicamente o mesmo padrão acima, mas com uma seq de numeros a mais e armazenar as ocorrencias em uma variavel chamada N
        print(N)
        print(len(N))

        #agora vamos fazer um loop para armazenar o vertice de 1 a "n", o valor de E, e o valor de N em um arquivo de texto:
        for i in range(len(E)):
            coords.write(str(i+1) + ' ' + E[i] + ' ' + N[i] +'\n')

