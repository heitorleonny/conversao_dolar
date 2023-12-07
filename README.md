# Conversão do Dólar em Tempo Real
 Esse projeto foi desenvolvido no ínicio dos meus estudos sobre API. Criei um site utilizando Python, Django, HTML e CSS (bem básicos) para que o usuário possa consultar o preço do dólar em tempo real e fazer conversões. Explicando de forma bem geral o programa consulta uma API que atualiza o valor do dólar de 30 em 30 segundos e a partir daí pega esses dados para realizar suas ações.
 

## Índice

1. [Visão Geral](#visão-geral)
2. [Configuração](#configuração)
   - [Instalação](#instalação)
   - [Configuração do Ambiente](#configuração-do-ambiente)
3. [Estrutura de Diretórios](#estrutura-de-diretórios)
4. [Referências e Links Úteis](#referências-e-links-úteis)

## Visão Geral

O propósito desse site é o estudo de APIS a partir do consumo de uma API com preço de moedas, onde o usuário pode realizar conversões de dólar para real.
![image](https://github.com/heitorleonny/conversao_dolar/assets/108541219/d6e8229d-a22d-4a74-b08c-def657f0c4b7)
![image](https://github.com/heitorleonny/conversao_dolar/assets/108541219/94e47820-1b67-4b46-ba89-16eb127c440a)

## Configuração

### Instalação

1. Para poder instalar o projeto e roda-lo é necessário ter instalado em sua máquina o python, git e alguma IDE de sua preferência.
2. Escolha a pasta onde deseja ter o repositório e abra seu terminal nessa pasta.
3. Efetue o clone com o seguinte comando ```https://github.com/heitorleonny/conversao_dolar.git```

### Configuração do Ambiente

Com o repositório clonado será necessário efetuar alguns passos para conseguir rodar o projeto:
1. Abra o repositório em alguma IDE (se estiver utilizando o VSCODE pode usar o atalho no terminal ```code .```)
2. Já na sua IDE abra um terminal e crie um ambiente virtual com o comando ```python -m venv env``` (caso queira pode substituir env pelo nome que preferir).
3. Sempre que você for rodar o site vai precisar ativar o ambiente virtual, podemos fazer isso com o seguinte comando ```env\Scripts\Activate``` no Windows. Se estiver usando Linux utilize ```source env/bin/activate```
4. Agora instale as dependencias do arquivo com o comando ```pip install -r requirements.txt```
5. Tudo certo!!! Agora é só rodar o projeto utilizando ```python manage.py runserver```


## Dúvidas e contribuições

O projeto é totalmente Open Source, logo você pode clona-lo e adicionar alterações que contribuam com o projeto que eu irei análisar e aceitar!😊
Caso tenha alguma dúvida pode entrar em contato comigo pelo meu [Linkedin](https://www.linkedin.com/in/heitor-leonny-24b564240/) ou [Instagram](https://www.instagram.com/heitor.leonny/)!

## Referências e Links Úteis

- [Django Official Documentation](https://docs.djangoproject.com/)





