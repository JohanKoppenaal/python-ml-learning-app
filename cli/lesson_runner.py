"""
Lesson Runner - Interactieve les-weergave voor CLI.
"""


def clear_screen():
    """Maak het scherm leeg (optioneel)."""
    # We doen dit niet standaard - kan verwarrend zijn
    pass


def show_section(section: dict, section_num: int, total: int):
    """Toon een sectie van de les."""
    print(f"\n{'═' * 60}")
    print(f"  📖 {section['title']}  ({section_num}/{total})")
    print(f"{'═' * 60}")
    print(section["content"])
    print()


def wait_for_continue():
    """Wacht tot de gebruiker verder wil."""
    input("Druk op Enter om verder te gaan...")


def run_lesson(lesson_module) -> dict:
    """
    Voer een les interactief uit.

    Args:
        lesson_module: Een geïmporteerde les-module (bijv. variables)

    Returns:
        dict met resultaten (score, etc.)
    """
    info = lesson_module.get_lesson_info()
    sections = lesson_module.get_sections()
    exercises = lesson_module.get_exercises()

    # Intro
    print(f"\n{'═' * 60}")
    print(f"  📚 Les: {info['title']}")
    print(f"  {info['description']}")
    print(f"{'═' * 60}")
    print()
    input("Druk op Enter om te beginnen...")

    # Secties doorlopen
    for i, section in enumerate(sections, 1):
        show_section(section, i, len(sections))
        wait_for_continue()

    # Oefeningen
    print(f"\n{'═' * 60}")
    print("  🎯 Oefeningen")
    print(f"{'═' * 60}")
    print("\nLaten we testen wat je hebt geleerd!\n")

    correct_count = 0
    total_count = len(exercises)

    for i, exercise in enumerate(exercises, 1):
        print(f"Vraag {i}/{total_count}:")
        print(f"  {exercise['question']}")
        print()

        attempts = 0
        max_attempts = 2

        while attempts < max_attempts:
            answer = input("Jouw antwoord: ").strip()

            if not answer:
                print("Typ een antwoord.\n")
                continue

            is_correct, feedback = lesson_module.check_answer(exercise["id"], answer)

            if is_correct:
                print(f"✅ {feedback}\n")
                correct_count += 1
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print(f"❌ {feedback}")
                    print("Probeer nog een keer.\n")
                else:
                    print(f"❌ {feedback}")
                    if exercise.get("answer"):
                        print(f"Het juiste antwoord was: {exercise['answer']}\n")
                    else:
                        print()

    # Resultaat
    percentage = int((correct_count / total_count) * 100) if total_count > 0 else 0

    print(f"\n{'═' * 60}")
    print(f"  🏁 Les afgerond!")
    print(f"{'═' * 60}")
    print(f"\n  Score: {correct_count}/{total_count} ({percentage}%)")

    if percentage == 100:
        print("  🌟 Perfect! Je hebt alles goed!")
    elif percentage >= 75:
        print("  👍 Goed gedaan!")
    elif percentage >= 50:
        print("  📚 Niet slecht, maar herhaling kan helpen.")
    else:
        print("  💪 Blijf oefenen, het komt goed!")

    print()

    return {
        "lesson_id": info["id"],
        "score": correct_count,
        "total": total_count,
        "percentage": percentage,
        "completed": True,
    }
