import pygame
import random

# Inicialização do pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ping Pong")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Raquetes
raquete_largura, raquete_altura = 10, 100
raquete_jogador = pygame.Rect(50, altura // 2 - raquete_altura // 2, raquete_largura, raquete_altura)
raquete_bot = pygame.Rect(largura - 50 - raquete_largura, altura // 2 - raquete_altura // 2, raquete_largura, raquete_altura)

# Bola
bola_tamanho = 20
bola = pygame.Rect(largura // 2 - bola_tamanho // 2, altura // 2 - bola_tamanho // 2, bola_tamanho, bola_tamanho)
bola_velocidade_x = 7
bola_velocidade_y = 7

# Pontuação
pontuacao_jogador = 0
pontuacao_bot = 0
fonte = pygame.font.Font(None, 36)

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Movimentação das raquetes
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete_jogador.top > 0:
        raquete_jogador.y -= 10
    if teclas[pygame.K_s] and raquete_jogador.bottom < altura:
        raquete_jogador.y += 10

    # Movimentação do bot
    if bola.centery < raquete_bot.centery:
        raquete_bot.y -= 7
    elif bola.centery > raquete_bot.centery:
        raquete_bot.y += 7

    # Movimentação da bola
    bola.x += bola_velocidade_x
    bola.y += bola_velocidade_y

    # Colisões com as bordas
    if bola.top <= 0 or bola.bottom >= altura:
        bola_velocidade_y *= -1

    # Colisões com as raquetes
    if bola.colliderect(raquete_jogador) or bola.colliderect(raquete_bot):
        bola_velocidade_x *= -1

    # Pontuação
    if bola.left <= 0:
        pontuacao_bot += 1
        bola.x = largura // 2 - bola_tamanho // 2
        bola.y = altura // 2 - bola_tamanho // 2
        bola_velocidade_x *= random.choice([1, -1])
        bola_velocidade_y *= random.choice([1, -1])
    elif bola.right >= largura:
        pontuacao_jogador += 1
        bola.x = largura // 2 - bola_tamanho // 2
        bola.y = altura // 2 - bola_tamanho // 2
        bola_velocidade_x *= random.choice([1, -1])
        bola_velocidade_y *= random.choice([1, -1])

    # Desenhar elementos
    janela.fill(branco)
    pygame.draw.rect(janela, preto, raquete_jogador)
    pygame.draw.rect(janela, preto, raquete_bot)
    pygame.draw.ellipse(janela, preto, bola)
    texto = fonte.render(f"{pontuacao_jogador} - {pontuacao_bot}", True, preto)
    janela.blit(texto, (largura // 2 - texto.get_width() // 2, 20))
    pygame.display.update()

