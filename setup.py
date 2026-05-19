import pygame
from characters import *

black_pieces_files = [
    "graphics/black_pieces/king-b.svg",
    "graphics/black_pieces/amazon-b.svg",
    "graphics/black_pieces/rook-b.svg",
    "graphics/black_pieces/augnw-b.svg",
    "graphics/black_pieces/bishop-b.svg",
    "graphics/black_pieces/pawn-b.svg"
]

white_pieces_files = [
    "graphics/white_pieces/king-w.svg",
    "graphics/white_pieces/amazon-w.svg",
    "graphics/white_pieces/rook-w.svg",
    "graphics/white_pieces/augnw-w.svg",
    "graphics/white_pieces/bishop-w.svg",
    "graphics/white_pieces/pawn-w.svg"
]

def add_pieces(pieces):
    for i in range(3):
        if i == 0:
            character = Rook
        elif i == 1:
            character = Knight
        elif i == 2:
            character = Bishop
        for x in [i, 7-i]:
            for y in [0, 7]:
                pieces[
                    character(
                        0 if y == 7 else 1,
                        white_pieces_files[i+2] if y == 7 else black_pieces_files[i+2]
                    )
                ] = (x, y)
    add_pawn(pieces)

def add_pawn(pieces):
    for color in range(2):
        for columns in range(8):
            pieces[
                Pawn(color,
                     black_pieces_files[5] if color == 1 else white_pieces_files[5]
                     )
            ] = [columns, 1] if color == 1 else [columns, 6]

def create_pieces(pieces):
    sprites = []
    for piece, coordinate in pieces.items():
        piece.rect.topleft = (
            coordinate[0] * piece.horizontal_multiplier,
            coordinate[1] * piece.vertical_multiplier
        )
        sprites.append(piece)
    return sprites
