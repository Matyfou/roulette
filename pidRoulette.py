import time
from rich.live import Live
from rich.text import Text
from rich.console import Console
import os
import random
import sys

if os.geteuid() != 0:
    print("Ce programme nécessite les droits root.")
    print("Relancement avec sudo...")
    os.execvp("sudo", ["sudo", "python3"] + sys.argv)

console = Console()

rouletteTime = 50
count = 0

win_count = 0

pids = [pid for pid in os.listdir("/proc") if pid.isdigit()]

for pid in pids:
    try:
        with open(f"/proc/{pid}/comm") as f:
            name = f.read().strip()
        #print(pid, name)
    except IOError:
        pass


def get_pid_name(pid : int):
    try:
        with open(f"/proc/{pid}/comm") as f:
            return f.read().strip()
    except IOError:
        return ""

def end_game(pid : int):
    global win_count
    win_count += 1
    name = get_pid_name(pid)

    print(f"killing {pid}, {name}...")

    time.sleep(1)

    if(name == ""):
        print(f"You have luck pid don't exist anymore")
    else:
        os.system(f"kill -9 {pid}")
        print(f"Killed !")

    time.sleep(0.5)

    print(f"Score : {win_count}")

def roll():
    global count

    seed = random.randint(1, len(pids))

    with Live(Text(""), refresh_per_second=30) as live:
        while count < rouletteTime:
            count += 1

            text = ""
            for i in range(20):
                pid = pids[(count + i + seed) % len(pids)]
                if(i == 10):
                    prefix = "> "
                else:
                    prefix = "  "

                try:
                    with open(f"/proc/{pid}/comm") as f:
                        name = f.read().strip()
                        text += f"{prefix}{pid} - {name}\n"
                except IOError:
                    text += f"{pid}\n"
            live.update(text)

            time.sleep((count / rouletteTime) ** 1.8 * 0.4)
    end_game(pids[(count + 10 + seed) % len(pids)])

print("---- PID ROULETTE ----")
input("Press Enter to continue...")
while 1:
    pids = [pid for pid in os.listdir("/proc") if pid.isdigit()]
    random.shuffle(pids)
    rouletteTime = 50
    count = 0
    roll()
    input("Press Enter to continue...")
