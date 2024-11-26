# -bu-st-_SW_Dev_Ed
## Branching Strategy
### Hauptbranch
- **main**: Der Hauptbranch für stabile Versionen.

### Feature Branches
- **feature/&lt;name&gt;**: Branch für die Entwicklung neuer Features.
- **bugfix/&lt;name&gt;**: Branch für das Beheben von Fehlern.

---

## Workflow
1. Erstelle einen neuen Branch basierend auf `main`.
    ```bash
    git checkout -b feature/<name>
    ```
2. Entwickle und committe Änderungen:
    ```bash
    git commit -m "Beschreibung der Änderung"
    ```
3. Pushe den Branch ins Remote-Repository:
    ```bash
    git push origin feature/<name>
    ```
4. Erstelle einen Pull Request, um den Branch in `main` zu mergen.

---

## Ziel
Diese Repository-Struktur ermöglicht eine klare Trennung von Features und Bugfixes sowie eine sichere Integration in den Hauptbranch.