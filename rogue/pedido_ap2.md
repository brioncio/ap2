# Pedido da AP2

## Descrição do projeto

Para finalizar o jogo, atenda aos seguintes requisitos adicionais de projeto:

- Modifique a cor do caractere que representa o tesouro para o vermelho;
- Centralize a mensagem do inferior da tela (atributos do aventureiro);
- Inclua na mensagem no inferior da tela a quantidade de experiência atual e a quantidade de experiência por nível, conforme o modelo abaixo:

    Aventureiro nv 3 (2 / 5) - Vida 120/150 - Força 10 - Defesa 20

- Crie um objeto "poção", que será representado no mapa pelo caractere `%`. Esse objeto deve ser inicializado no início do jogo, e deve ficar visível no mapa enquanto o jogador não tiver passado por ele. Ao chegar no item, um de três possíveis efeitos pode acontecer:
  - Dobra a vida do jogador;
  - Aumenta em 15 a força do jogador;
  - Aumenta em 10 a defesa do jogador;
- Crie um sistema de dificuldade do jogo, onde ao pressionar a tecla "N", o jogo fica mais simples (divida por 1.1 todos os atributos dos monstros gerados), e ao pressionar a tecla "M", o jogo fica mais difícil (multiplique por 1.1 todos os atributos dos monstros gerados). Os atributos dos monstros devem ser multiplicados pelo fator da dificuldade e convertidos para um tipo inteiro;
- Coloque, no canto superior direito da tela, um número do tipo `float`, com quatro casas decimais, representando o índice de dificuldade do jogo.

- Inclua uma nova funcionalidade para o jogo! Essa nova funcionalidade pode render até um ponto extra na nota do projeto (até o limite de 10,0). Quanto mais complexa a funcionalidade, maior a pontuação que será concedida.

## Demais informações

- Confira os projetos das outras turmas para inspiração!
- Volte na [página inicial](/pedido_ap2.md) para informações sobre entrega do trabalho, prazos, etc.
