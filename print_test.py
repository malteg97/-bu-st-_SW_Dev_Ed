import pytest

def test_code_contains_specific_lines():
    # Öffne die Datei, die getestet werden soll
    with open("main_code.py", "r") as file:
        code = file.read()
    
    # Definiere die Zeilen, nach denen gesucht werden soll
    expected_lines = [
        "import cyberpi",
        "x = 'Hallo'",
        "cyberpi.console.println(x)"
    ]

    # Überprüfen, ob jede erwartete Zeile im Code enthalten ist
    for line in expected_lines:
        assert line in code, f"Die Zeile '{line}' fehlt im Code."