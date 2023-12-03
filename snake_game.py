class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self):
        if self.head is not None:
            deleted_data = self.head.data
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return deleted_data
        else:
            raise IndexError("Queue is empty")

    def search_binary(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def pick_head(self):
        return self.head.data

    def pick_tail(self):
        return self.tail.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        return
    def reverse_iterator(self):
        current = self.tail.prev
        while current:
            yield current.data
            current = current.prev


# configurações iniciais

import pygame

import random

pygame.init()

pygame.display.set_caption("Jogo Snake Python")

largura, altura = 800, 600

tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

# cores RGB

preto = (0, 0, 0)

branco = (255, 255, 255)

vermelho = (255, 0, 0)

verde = (0, 255, 0)

# parametros da cobra

tamanho_quadrado = 20

velocidade_jogo = 15


def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(
        tamanho_quadrado)

    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho])


def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)

    texto = fonte.render(f"Pontos: {pontuacao}", True, branco)

    tela.blit(texto, [1, 1])


def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:

        velocidade_x = 0

        velocidade_y = tamanho_quadrado

    elif tecla == pygame.K_UP:

        velocidade_x = 0

        velocidade_y = -tamanho_quadrado

    elif tecla == pygame.K_RIGHT:

        velocidade_x = tamanho_quadrado

        velocidade_y = 0

    elif tecla == pygame.K_LEFT:

        velocidade_x = -tamanho_quadrado

        velocidade_y = 0

    return velocidade_x, velocidade_y


def rodar_jogo():
    fim_jogo = False

    x = largura / 2

    y = altura / 2

    velocidade_x = 0

    velocidade_y = 0

    tamanho_cobra = 1

    pixels = DoublyLinkedList()

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:

        tela.fill(preto)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                fim_jogo = True

            elif evento.type == pygame.KEYDOWN:

                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # desenhar_comida

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posicao da cobra

        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += velocidade_x

        y += velocidade_y

        # desenhar_cobra

        pixels.insert([x, y])

        if len(pixels) > tamanho_cobra:
            pixels.delete()

        # se a cobra bateu no proprio corpo

        for pixel in pixels.reverse_iterator():
                if pixel == [x, y]:
                    fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)

        # desenhar_pontos

        desenhar_pontuacao(tamanho_cobra - 1)

        # atualizacao da tela

        pygame.display.update()

        # criar uma nova comida

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1

            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

rodar_jogo()
