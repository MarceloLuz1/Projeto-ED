# Jogo Snake com Fila (Queue) em Python

## Descrição

Este é um projeto simples de um jogo Snake implementado em Python, fazendo uso de uma estrutura de dados de fila (queue) para armazenar as posições da cobra. O Pygame é utilizado para criar a interface gráfica do jogo.

## Estrutura de Dados

O jogo utiliza uma implementação de lista duplamente encadeada com comportamento de fila para armazenar as posições da cobra. A classe DoublyLinkedList é responsável por manipular a fila.

```bash
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```
A posição de cada pixel da cobra é armazenada em um vetor de coordenadas (x, y). Ao se mover o vetor de coordenadas mais antigo (primeiro da fila) é deletado e um novo vetor é adicionado (último da fila), desse modo, fica evidente o porquê a estrutura de dados fila (queue) foi escolhida neste projeto.

## Requisitos

Certifique-se de ter o Python 3 ou superior e o Pygame instalados em seu sistema (utilize o código abaixo no terminal)

```bash
pip install pygame
```

## Como Jogar

Execute o código Python.
Use as teclas de seta (cima, baixo, esquerda, direita) para controlar a direção da cobra (pixels verdes na tela). \n
A cobra crescerá ao comer a comida (pixels vermelhos na tela). O contador no canto superior esquerdo indico o número de pontos.\n
O jogo termina se a cobra colidir com as bordas da tela ou com seu próprio corpo.


## Créditos

Autor(es) e contribuidores.

## Licença

Este projeto é distribuído sob a licença MIT.

## Agradecimentos

Agradecimentos a contribuidores e projetos inspiradores.
