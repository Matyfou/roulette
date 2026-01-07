import time
from random import randint

from rich.live import Live

console = None

rouletteTime = 100

rouletteNbs = [
	0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27,
	13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1,
	20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
]


def get_color(colorNumber: int) -> int:
    index = rouletteNbs.index(colorNumber)
    if (index == 0):
        return 2
    if (index % 2 == 0):
        return 1
    elif (index % 2 == 1):
        return 0

def get_color_id(colorNumber: int) -> str:
    index = rouletteNbs.index(colorNumber)
    if (index == 0):
        return "green"
    if (index % 2 == 0):
        return "grey37"
    elif (index % 2 == 1):
        return "red"





def roll() -> int:
    console.print((" " * 24) + "\\/")
    randSeed = randint(0, 36)
    count = 0
    with Live() as live:
        while count < rouletteTime:
            count += 1
            text = ""
            for x in range(20):
                colorString = get_color_id(rouletteNbs[(count + x + randSeed) % len(rouletteNbs)])
                nb = str(rouletteNbs[(count + x + randSeed) % len(rouletteNbs)])
                nb = nb + " " if len(nb) == 1 else nb
                text += f"[bold {colorString}]{nb}[/bold {colorString}] "
            live.update(text)
            live.refresh()
            time.sleep((count / rouletteTime) ** 1.8 * 0.4)

    return rouletteNbs[((count + x + randSeed) - 11) % len(rouletteNbs)]



