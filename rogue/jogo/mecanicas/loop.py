import time

from . import som
from . import mecanicas
from .inputbox import ler_texto
from .buttonbox import escolher_classe

from ..gui.tela import Tela

from ..personagens.aventureiro.aventureiro import Aventureiro
from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.tank import Tank
from ..personagens.tesouro import Tesouro
from ..personagens.npc import NPC
from ..personagens.inimigos.boss import Boss
from ..mecanicas import mecanicas

import pygame

def determinar_direcao(teclas):
    if teclas[pygame.K_a]:
        return "A"
    if teclas[pygame.K_w]:
        return "W"
    if teclas[pygame.K_s]:
        return "S"
    if teclas[pygame.K_d]:
        return "D"

    return ""

def determinar_dificuldade(teclas):
    if teclas[pygame.K_n]:
        return "N"
    if teclas[pygame.K_m]:
        return "M"

def executar():
    som.iniciar_musica()

    nome = ler_texto()
    classe = escolher_classe()
    match classe:
        case "Guerreiro":
            aventureiro = Guerreiro(nome)
        case "Tank":
            aventureiro = Tank(nome)
        case _:
            aventureiro = Aventureiro(nome)

    tesouro = Tesouro()
    npc = NPC(tesouro)
    tela = Tela()

    jogo_rodando = True
    while jogo_rodando:
        # Análise dos eventos
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                # Processamento do jogo
                if teclas[pygame.K_q]:
                    aventureiro.status = "Já correndo?"
                    jogo_rodando = False

                if teclas[pygame.K_c]:
                    aventureiro.trocar_char()
                elif teclas[pygame.K_v]:
                    aventureiro.trocar_cor()
                elif teclas[pygame.K_b]:
                    aventureiro.trocar_cor(aleatorio=True)
                    
                if teclas[pygame.K_n]:
                     mecanicas.trocar_dificuldade(teclas)
                elif teclas[pygame.K_m]:
                    mecanicas.trocar_dificuldade(teclas)

                if teclas[pygame.K_SPACE]:
                    mecanicas.conversar(aventureiro, npc)
                else:
                    direcao = determinar_direcao(teclas)
                    if direcao != "" and not mecanicas.movimentar(aventureiro, direcao, npc):
                        jogo_rodando = False

                    if aventureiro.posicao == tesouro.posicao:
                        boss = Boss()
                        if mecanicas.iniciar_combate(aventureiro, boss):
                            aventureiro.status = f"Parabéns! Você derrotou {boss.nome} e encontrou o tesouro!"
                        else:
                            aventureiro.status = f"Você foi derrotado por {boss.nome}! Game over..."
                        jogo_rodando = False

        # Renderização na tela
        tela.renderizar(aventureiro, tesouro, npc)
        pygame.time.Clock().tick(60)

    time.sleep(2)
