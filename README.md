# Jogo de Mesa Cidade Dorme - Versão em Python
## [Autor: Lucas Barbosa Nascimento](https://github.com/Lucasbnas435) 

O projeto consiste numa adaptação do clássico jogo de mesa conhecido como "Cidade Dorme", "Máfia" ou "Noite na Vila" para uma versão computacional implementada em Python.

## Dinâmica do Jogo
Para que o jogo ocorra, um dos participantes deve assumir o papel de narrador. No início da partida, são sorteadas cartas com os personagens que cada pessoa (excluindo o narrador) deve interpretar: cidadão, mafioso, doutor ou xerife. O objetivo é descobrir quem é o assassino e eliminá-lo. 

Após a divisão de papéis, começam as rodadas. Elas são jogadas da seguinte forma:

1. O narrador declara "Cidade dorme!" e todos fecham os olhos
2. O narrador anuncia que o mafioso pode agir
3. O mafioso seleciona alguém para matar e comunica ao narrador, fechando os olhos ao fim de sua ação
4. O narrador anuncia que o doutor pode agir
5. O doutor escolhe alguém para tentar salvar, fechando os olhos ao fim de sua ação. Se a pessoa escolhida for a mesma que o mafioso selecionou, ela deixa de morrer
6. O narrador anuncia que o xerife pode agir
7. O xerife aponta quem ele acha que é o mafioso; o narrador responde se o palpite está correto ou não
8. O narrador declara "Cidade acorda!" e todos abrem os olhos. Em sequência, ele anuncia quem morreu naquela noite ou revela apenas que um participante foi salvo pelo doutor
9. Todos os jogadores discutem entre si para tentar descobrir quem é o mafioso. Finalizando-se a discussão, uma pessoa é acusada
10. O acusado deve fazer um breve pronunciamento defendendo-se
11. Os acusadores, tendo ouvido a defesa, votam se desejam eliminar o acusado ou não
12. Caso o acusado seja eliminado, o narrador revela se ele era o mafioso ou não. Caso o acusado não seja eliminado, retorna-se à etapa 9, e outra pessoa será acusada

Caso o mafioso seja eliminado, o jogo termina com __vitória da cidade__. Se restar o mafioso sozinho ou acompanhado de apenas mais um participante, o jogo é encerrado com __derrota da cidade__.

## Funcionalidades
- Implementação de todas as regras do jogo de mesa
- O próprio computador atua como narrador
- O usuário joga com mais sete players computadorizados
- Caso o usuário seja eliminado, há a possibilidade de continuar assistindo ao decorrer do jogo (ele atuará como espectador)

## Como Executar a Aplicação?
1. É necessário ter Python 3 instalado na máquina
2. Clone este repositório, digitando no terminal:
```sh
git clone https://github.com/Lucasbnas435/Cidade-Dorme-Python
```
3. Entre no diretório do projeto
```sh
cd Cidade-Dorme-Python
```
4. Entre na pasta src
```sh
cd src
```
5. Execute o programa
```sh
python cidade_dorme.py
```

## Contatos
Muito obrigado por acessar esse projeto!

Vamos nos conectar?

- GitHub: https://github.com/Lucasbnas435
- LinkedIn: https://linkedin.com/in/lucasbnas
- E-mail: lucasbnas435@gmail.com
