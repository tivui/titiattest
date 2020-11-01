#depuis le dossier app, importer l'objet app contenu dans le dossier init, l'objet app est de type application Flask
from app import app

if "__main__" == __name__:
    app.run(debug=True)
