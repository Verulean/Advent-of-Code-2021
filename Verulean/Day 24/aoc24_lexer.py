from pygments.lexer import RegexLexer
from pygments.token import *


class AdventOfCode24Lexer(RegexLexer):
    name = "aoc24"
    aliases = ["aoc", "alu"]

    tokens = {
        "root": [
            (r"inp|add|mul|div|mod|eql", Keyword),
            (r"[-0-9]+", Number.Integer),
            (r"\w", Name),
            (r".", Text),
        ]
    }
