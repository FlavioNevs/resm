<h1>Analise de dados por limiar de chuva</h1>
<hr>

O codigo é de execução simples e utiliza os proprios argumentos do terminal para o seu funcionamento.

Argumentos:

    format
        -ae     #Referencia o arquivo de entrada
        -as     #Referencia o arquivo de Saida
    
    calc
        -m      #Faz calculo por município
        -b      #Faz calculo por bairro/estação
        -ae     #Referencia o arquivo de entrada
        -as     #Referencia o arquivo de Saida
        -lA     #Referencia o Limiar A
        -lB     #Referencia o Limiar B

Exemplo:

    python main.py format -ae resm.csv  -as resm_mod.csv
    python main.py calc -b -as resm.csv -lA 10 -lB 20 -as resm_10_20.csv
