#!/usr/bin/env python3

from random import randint
import time
from rich.live import Live
from rich.console import Console
from rich.panel import Panel
import roulette as roulette

console = Console()
roulette.console = console

console.print(Panel("[bold white on red] ROUGE [/bold white on red][red] 32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 20, 14, 9, 18[/red]"))
console.print(Panel("[bold white on grey37] NOIR [/bold white on grey37][grey37] 15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 22, 29, 7, 28, 12, 35, 3, 26[/grey37]"))
console.print(Panel("[bold grey37 on green] VERT [/bold grey37 on green][green] 0[/green]"))

input = console.input("[bold magenta]Entre ton guess [R/N/V/chiffre] : [/bold magenta]").lower()
selection = 0 # 0 : red | 1 : black | 2 : green | negative : number

if(input.isdigit()):
    selection = -(int(input))
elif(type(input) == str):
    if(input == "r"):
        selection = 0
    elif (input == "n" or input == "b"):
        selection = 1
    elif (input == "v" or input == "g"):
        selection = 2
    else:
        raise Exception("Couleur inconnu")
else:
    raise Exception("Format inconnu")

roll = roulette.roll()
roll_color = roulette.get_color_id(roll)
if(selection >= 0 and roulette.get_color(roll) == selection):
    console.print(f"\n[bold {roll_color}]  Couleur Trouvée ![/bold {roll_color}]")
elif(selection < 0 and roll == selection):
    console.print(f"\n[bold {roll_color}]  Chiffre Trouvée ! : {roll}[/bold {roll_color}]")
else:
    #console.print(str(roulette.get_color(roll)), " | ", selection)
    console.print(f"\n[bold {roll_color}]  Perdu... : {roll}[/bold {roll_color}]")

print("\nCTRL+C to quit")
time.sleep(60)
