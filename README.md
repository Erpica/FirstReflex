            # REFLEX

Vamos a crear nuestro primer proyecto Reflex con VSCode, PowerShell y Python 3.14.4 (En el momento de iniciar)

Creamos, en la carpeta del proyecto el ENTORNO VIRTUAL con:
1. Vemos si estamos en algún entorno virtual:
   $env:VIRTUAL_ENV
2. Salimos del entorno virtual actual:
   deactivate
3. Creamos el nuevo entorno virtual:
   python -m venv 1.FirstReflex
4. Dentro de la carpeta 1.FirstReflex: (Si da error de permisos -> p:\[...]>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser)
   .\Scripts\Activate.ps1

Creamos el proyecto GIT:
1. Dentro de la carpeta 1.FirstReflex:
   git init
2. Creamos, en la raíz del proyecto el .gitignore con el siguiente contenido:
   ```
   # Entornos virtuales
   .venv/
   venv/
   # Variables de entorno y llaves secretas
   .env
   # Cache y archivos temporales de Python
   __pycache__/
   *.py[cod]
   ```

Sincronizamos con GITHUB:
1. git add .
2. git commit -m "Commit inicial: Creado entorno virtual y proyecto git"
3. Creamos el repositorio sin README.md ni gitignore (ya los tengo en local)
4. git branch -M main (por si estuviera en la master, como antiguamente)
5. git remote add origin https://github.com/Erpica/FirstReflex.git
6. git push -u origin main