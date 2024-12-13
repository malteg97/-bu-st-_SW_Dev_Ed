import pytest
from main_code import x  # Importiere die Variable x aus der Datei main_code

def test_variable_x():
    """Testet, ob die Variable x den Wert 'Hallo' enthält."""
    assert x == 'Hallo', f"Erwartet 'Hallo', aber erhalten: {x}"

    
