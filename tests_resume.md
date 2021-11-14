# Les bibliothèques de test:

## unittest > De base intégrée dans Python.
## Dans le terminal "python - m unittest <nom_du_fichier>" avec ou sans le .py
---
## doctest > également intégrée à Python. (Tests dans des docstrings).
---
## pytest > La plus utilisée. A installer avec pip (pip install pytest & pipinstall pytest-html). Syntaxe épurée par rapport à unitest. Nombreux plugins.
### Plus rapide que les deux cités précédements.
### pytest est compatible avec unittest. (Rétrocompatibilité des test.)
## Dans le terminal pytest "<nom_du_fichier.py>"
---
### Il est important de réaliser un coverage de ces fichiers. en ne visant pas forcément 100% sur la globalité,
### mais en ciblant les fichiers les plus importants. On utilise la librairie coverage.py
### Exemple sur un site / app Web il est important de bien test les models de la BDD, mais moins de test les vues.
### Dans le terminal on effectue coverage run -m unittest <nom_du_fichier>
### Ensuite pour le rapport dans le terminal coverage html
---
### Une méthode de programmation populaire est la TDD, Test Driven Developpement.