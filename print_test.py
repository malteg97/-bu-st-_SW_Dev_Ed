import pytest
from unittest.mock import patch
import cyberpi

# Testfunktion
def test_on_start():
    # Mock die Methode println
    with patch('cyberpi.console.println') as mock_println:
        # Importiere das Modul, damit die Eventfunktion getriggert werden kann
        import main_code # Ersetze "your_module_name" durch den Namen deines Moduls
        
        # Überprüfen, ob cyberpi.console.println mit "Hallo!" aufgerufen wurde
        mock_println.assert_called_once_with("Hallo!")