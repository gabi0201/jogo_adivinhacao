# Explicação do Código

## Importação do Random
- Utilizado para **gerar o número secreto** aleatoriamente.

## Variáveis de Controle
- **`tentativas_restantes`:**
  - Inicia com o valor 7 e **diminui a cada palpite**.
- **`tentativas`:**
  - **Conta o número de palpites** feitos pelo jogador durante a partida.

## Loop Principal
- **Mantém o jogo em execução** até que o jogador escolha sair, oferecendo a opção de jogar novamente ao final de cada rodada.

## Loop de Tentativas
- **Permite ao jogador fazer palpites repetidos** até que ele:
  - Acerte o número secreto.
  - Ou esgote as tentativas disponíveis.

## Feedback ao Jogador
- **Informa se:**
  - O palpite está **correto**.
  - O número secreto é **maior ou menor** que o palpite fornecido.
  - **Quantas tentativas ainda restam**, mantendo o jogador informado sobre sua progressão.

## Pontuação
- **Cálculo:**  
  - O jogador ganha pontos com base no número de tentativas restantes:  
    `pontuação = tentativas_restantes * 10`.
- **Armazenamento:**  
  - As pontuações de cada partida são **salvas em uma lista chamada `pontuacoes`**, criando um histórico para referência.

## Placar
- Após cada partida, o **histórico de pontuações é exibido**, permitindo ao jogador acompanhar seu desempenho em diferentes rodadas.

## Opção de Jogar Novamente
- Após o término de uma partida, o jogador é questionado se deseja **continuar jogando ou encerrar**.