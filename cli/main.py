"""
Python & ML Learning App - CLI Interface

Een interactieve command-line applicatie die je stap voor stap
door Python en Machine Learning heen leidt.
"""

import sys
from pathlib import Path

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.lessons import variables
from cli.lesson_runner import run_lesson

# Beschikbare lessen (wordt later dynamisch)
AVAILABLE_LESSONS = [
    {"module": variables, "info": variables.get_lesson_info()},
]


def show_banner():
    """Toon de welkomstbanner."""
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║        Python & Machine Learning Learning App            ║
    ║                                                          ║
    ║        Leer Python door te bouwen.                       ║
    ║        Leer ML door het toe te passen.                   ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(banner)


def show_menu():
    """Toon het hoofdmenu en return de keuze."""
    print("\n--- Hoofdmenu ---\n")
    print("  1. Lessen")
    print("  2. Quiz")
    print("  3. Voortgang bekijken")
    print("  4. Over deze app")
    print("  0. Afsluiten")
    print()

    choice = input("Kies een optie: ").strip()
    return choice


def handle_lessons():
    """Toon beschikbare lessen en laat gebruiker kiezen."""
    print("\n📚 Beschikbare Lessen\n")

    for i, lesson in enumerate(AVAILABLE_LESSONS, 1):
        info = lesson["info"]
        print(f"  {i}. {info['title']} - {info['description']}")

    print(f"  0. Terug naar hoofdmenu")
    print()

    choice = input("Kies een les: ").strip()

    if choice == "0":
        return

    try:
        lesson_index = int(choice) - 1
        if 0 <= lesson_index < len(AVAILABLE_LESSONS):
            selected = AVAILABLE_LESSONS[lesson_index]
            result = run_lesson(selected["module"])
            # TODO: Save result to progress tracker
        else:
            print("\n⚠️  Ongeldige keuze.")
    except ValueError:
        print("\n⚠️  Voer een nummer in.")


def handle_quiz():
    """Start een quiz."""
    print("\n📝 Quiz\n")
    print("  Quiz-engine wordt nog gebouwd.\n")


def handle_progress():
    """Toon voortgang."""
    print("\n📊 Voortgang\n")
    print("  Voortgangstracker wordt nog gebouwd.\n")


def handle_about():
    """Toon informatie over de app."""
    print("\n ℹ️  Over deze app\n")
    print("  Dit is een interactieve learning app voor Python en ML.")
    print("  Je leert door de app zelf te bouwen en uit te breiden.")
    print()
    print("  Fase 1: Python Fundamentals")
    print("  Fase 2: Python Verdieping (OOP)")
    print("  Fase 3: Data Science Basis")
    print("  Fase 4: Machine Learning Intro")
    print("  Fase 5: ML Verdieping")
    print("  Fase 6: Deep Learning & NLP")
    print("  Fase 7: Web Interface\n")


def main():
    """Hoofdloop van de applicatie."""
    show_banner()

    while True:
        choice = show_menu()

        if choice == "1":
            handle_lessons()
        elif choice == "2":
            handle_quiz()
        elif choice == "3":
            handle_progress()
        elif choice == "4":
            handle_about()
        elif choice == "0":
            print("\nTot ziens! Blijf leren. 👋\n")
            break
        else:
            print("\n⚠️  Ongeldige keuze. Probeer opnieuw.")


if __name__ == "__main__":
    main()
