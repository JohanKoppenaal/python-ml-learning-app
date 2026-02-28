"""
Les 1: Variabelen in Python

Deze les behandelt:
- Wat zijn variabelen?
- Variabelen aanmaken en toewijzen
- Naming conventions
- Basis datatypes (int, float, str, bool)
"""

LESSON_INFO = {
    "id": "variables",
    "title": "Variabelen",
    "description": "Leer hoe je data opslaat en gebruikt in Python",
    "order": 1,
}

SECTIONS = [
    {
        "title": "Wat is een variabele?",
        "content": """
Een variabele is een naam die verwijst naar een waarde in het geheugen.
Denk aan het als een gelabeld doosje waar je iets in stopt.

In Python maak je een variabele door simpelweg een naam te kiezen
en er een waarde aan toe te wijzen met het = teken:

    naam = "Johan"
    leeftijd = 30
    is_student = True

Python bepaalt automatisch het type (string, integer, boolean).
Dit heet 'dynamic typing' - je hoeft het type niet te declareren.
""",
    },
    {
        "title": "Naming conventions",
        "content": """
In Python volgen we deze conventies voor variabelenamen:

  ✓ snake_case      → gebruikers_naam, max_waarde
  ✓ lowercase       → naam, leeftijd
  ✓ beschrijvend    → totaal_prijs (niet: tp)

  ✗ camelCase       → gebruikersNaam (dat is Java/JS)
  ✗ UPPERCASE       → NAAM (dat is voor constanten)
  ✗ cijfer vooraan  → 1_naam (syntax error!)
  ✗ spaties         → mijn naam (syntax error!)

Gereserveerde woorden kun je ook niet gebruiken:
  if, else, for, while, class, def, return, True, False, None, ...
""",
    },
    {
        "title": "Basis datatypes",
        "content": """
Python heeft ingebouwde datatypes. De meest gebruikte:

  int       Gehele getallen         42, -7, 0
  float     Decimale getallen       3.14, -0.5
  str       Tekst (strings)         "Hallo", 'Python'
  bool      Boolean (waar/onwaar)   True, False
  None      Geen waarde             None

Je kunt het type checken met type():

    >>> type(42)
    <class 'int'>

    >>> type("hallo")
    <class 'str'>
""",
    },
    {
        "title": "Type conversie",
        "content": """
Je kunt waarden omzetten naar een ander type:

    int("42")       →  42          (string naar int)
    float("3.14")   →  3.14        (string naar float)
    str(42)         →  "42"        (int naar string)
    bool(1)         →  True        (int naar bool)
    bool(0)         →  False

Let op: niet alles kan geconverteerd worden!

    int("hallo")    →  ValueError!
    int("3.14")     →  ValueError! (gebruik float() eerst)
""",
    },
]

EXERCISES = [
    {
        "id": "var_1",
        "question": "Wat is de output van: type(3.14)?",
        "hint": "Decimale getallen zijn floats in Python.",
        "answer": "<class 'float'>",
        "alt_answers": ["float", "class 'float'"],
    },
    {
        "id": "var_2",
        "question": "Maak een variabele 'naam' met jouw naam als waarde. Wat typ je?",
        "hint": "Strings staan tussen quotes.",
        "answer": None,  # Vrije invoer, check patroon
        "pattern": r'^naam\s*=\s*["\'].+["\']$',
    },
    {
        "id": "var_3",
        "question": "Welke variabelenaam is NIET geldig in Python?\n  a) user_name\n  b) 2nd_place\n  c) _private\n  d) userName",
        "hint": "Een variabele mag niet beginnen met een cijfer.",
        "answer": "b",
        "alt_answers": ["b)", "2nd_place"],
    },
    {
        "id": "var_4",
        "question": "Wat is int('42') + 8?",
        "hint": "int() converteert een string naar een integer.",
        "answer": "50",
        "alt_answers": [],
    },
]


def get_lesson_info() -> dict:
    """Return metadata over deze les."""
    return LESSON_INFO


def get_sections() -> list:
    """Return alle secties van de les."""
    return SECTIONS


def get_exercises() -> list:
    """Return alle oefeningen."""
    return EXERCISES


def check_answer(exercise_id: str, user_answer: str) -> tuple[bool, str]:
    """
    Check of het antwoord correct is.

    Returns:
        (is_correct, feedback_message)
    """
    import re

    exercise = next((e for e in EXERCISES if e["id"] == exercise_id), None)
    if not exercise:
        return False, "Oefening niet gevonden."

    user_answer = user_answer.strip()

    # Pattern-based check (voor vrije invoer)
    if "pattern" in exercise:
        if re.match(exercise["pattern"], user_answer):
            return True, "Correct! Goed gedaan."
        return False, f"Niet helemaal. Hint: {exercise['hint']}"

    # Exact match check
    correct = exercise["answer"]
    alt_answers = exercise.get("alt_answers", [])

    if user_answer.lower() == correct.lower() or user_answer.lower() in [a.lower() for a in alt_answers]:
        return True, "Correct! Goed gedaan."

    return False, f"Niet helemaal. Hint: {exercise['hint']}"
