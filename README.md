# Introdução

Case resolvendo o desafio proposto.

## Perguntas

### Faça uma exploração dos dados e mostre como a quantidade de leads varia de acordo com as outras variáveis (por exemplo, a marca ou o modelo afetam o recebimento de leads? O comportamento observado é o mesmo em todas as cidades?)

Podemos ver que os leads variam de acordo com as variáveis.

obs: os elementos das tabelas contém o seguinte formato:

```txt
[código, quantidade]
```

* cod_marca_veiculo (código da marca do veículo): foi analisado o top 5 de cada estado baseado na marca do veículo, e podemos ver que para cada estado as principais marcas variam.
![df_marca](docs/df_marca.PNG "df_marca")

* cod_modelo_veiculo (código do modelo veículo): o modelo também varia com cada estado, podemos ver que os mais cotados são:
![df_modelo](docs/df_modelo.PNG "df_modelo")

Para otimizar a análise foi agregado as cidades por estado, tendo em vista que as capitais são muito mais expressivas e que os nomes identificadores de algumas cidades são inconclusivos.
![cidades](docs/cidades.PNG "cidades")

### Proponha um modelo para determinar se um anúncio receberá lead. Que outras informações, as quais você não teve acesso, poderiam ajudar a chegar a conclusões melhores?

Seria interessante para o modelo a presença da informação:

* Sinistro (quando houve algum dano no carro, como batidas);
* Troca de pneu na compra;
* Multa, se há multa em aberto relacionada ao carro;
* Eficiência, quantos quilômetros o carro pode fazer por litro.

### Proponha um modelo para determinar a quantidade de leads que um anúncio irá receber

...
