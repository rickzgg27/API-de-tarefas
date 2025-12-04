import os
import sys
import time
import random
import shutil

# -------------------------------
# CONFIGURAÇÕES BÁSICAS
# -------------------------------
REFRAIN_LINES = [
    "Let down and hanging around",
    "Crushed like a bug in the ground",
    "Let down and hanging around..."
]

# Tempo entre letras (ajuste para mudar o ritmo)
TYPE_SPEED = 0.05  # menor = mais rápido
LINE_DELAY = 1.5   # pausa entre as linhas
ANIMATION_SPEED = 0.04  # velocidade das ondas

# -------------------------------
# FUNÇÕES AUXILIARES
# -------------------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def generate_wave(width: int) -> str:
    """Gera uma linha de ondas ASCII pseudoaleatórias."""
    levels = "▁▂▃▄▅▆▇█"
    return "".join(random.choice(levels) for _ in range(width))

def type_text(line: str):
    """Anima a digitação letra por letra."""
    for ch in line:
        print(ch, end="", flush=True)
        time.sleep(TYPE_SPEED)
    print()  # quebra de linha no final

def animate_refrain():
    """Mostra as ondas e o texto simultaneamente."""
    cols = shutil.get_terminal_size().columns
    clear_screen()
    print("\033[1;36m")  # cor ciano suave

    # Exibe título
    print("╔══════════════════════════════════════════════════════╗")
    print("║               ♪  Let Down — Refração ♪               ║")
    print("╚══════════════════════════════════════════════════════╝\n")
    time.sleep(1.2)

    # Loop pelas linhas do refrão
    for line in REFRAIN_LINES:
        # Enquanto escreve a linha, anima as ondas em paralelo
        for i, ch in enumerate(line):
            print(ch, end="", flush=True)
            wave = generate_wave(cols)
            print(f"\n{wave}", end="\r")
            time.sleep(TYPE_SPEED)
        print("\n")
        time.sleep(LINE_DELAY)
    print("\033[0m")  # reset de cor

def ending_animation():
    """Efeito final: ondas intensas"""
    cols = shutil.get_terminal_size().columns
    print("\n\033[1;35m")  # magenta
    for _ in range(25):
        wave = generate_wave(cols)
        print(wave, end="\r")
        time.sleep(ANIMATION_SPEED)
    print("\033[0m\n")
    print("✨ Fim do refrão — Let Down (Refração) ✨\n")

# -------------------------------
# EXECUÇÃO PRINCIPAL
# -------------------------------
if __name__ == "__main__":
    try:
        animate_refrain()
        ending_animation()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")
        sys.exit(0)
