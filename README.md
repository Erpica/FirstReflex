<h1 align="center">🚀 FirstReflex</h1>

Vamos a crear nuestro primer proyecto Reflex con VSCode, PowerShell, uv y Python 3.14.4 (En el momento de iniciar)

Creamos, en la carpeta del proyecto el **ENTORNO VIRTUAL** con:
1. Vemos si estamos en algún entorno virtual:
   $env:VIRTUAL_ENV
2. Salimos del entorno virtual actual:
   deactivate
3. Creamos el nuevo entorno virtual:
   python -m venv 1.FirstReflex
4. Dentro de la carpeta 1.FirstReflex: (Si da error de permisos -> p:\[...]>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser)
   .\Scripts\Activate.ps1

Creamos el proyecto **GIT**:
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

Sincronizamos con **GITHUB**:
1. git add .
2. git commit -m "Commit inicial: Creado entorno virtual y proyecto git"
3. Creamos el repositorio sin README.md ni gitignore (ya los tengo en local)
4. git branch -M main (por si estuviera en la master, como antiguamente)
5. git remote add origin https://github.com/Erpica/FirstReflex.git
6. git push -u origin main

Instalamos lo necesario y empezamos a usar **REFLEX**:
1. uv pip install reflex
2. reflex init




Notas adicionales:
- Actualizar todo: `uv pip install -U -r requirements.txt`
- Para proyectos profesionales debemos tener pyproject.toml:
   * uv init
   * uv add requests
- Ver que paquetes reconoce uv: `uv tree`




======================================

Componentes de reflex:
* Estructura y Diseño (Layout)

   Box: Contenedor genérico basado en una etiqueta div para aplicar estilos.
   
   Flex / Grid: Permiten organizar elementos en filas, columnas o rejillas responsivas.
   
   Spacer: Añade espacio flexible entre componentes.

* Formularios y Entrada de DatosButton: 

   Botón interactivo para activar eventos.
   
   Input / Text Area: Campos de texto para que el usuario escriba información.
   
   Checkbox / Radio Group / Switch: Opciones de selección múltiple o interruptores.
   
   Upload: Componente para subir archivos.

* Visualización de Datos y Contenido

   Text / Heading: Textos planos y títulos de diferentes niveles.
   
   Avatar / Badge: Imágenes de perfil e insignias o etiquetas.
   
   Code Block: Bloques de código con resaltado de sintaxis.
   
   Spinner / Skeleton: Indicadores de carga visual.
   
* Renderizado Dinámico y Control
   Cond: Renderiza componentes de forma condicional según una variable.
   
   Foreach: Permite iterar sobre listas de datos para mostrar elementos repetitivos.
   
   Match: Funciona como una estructura de selección múltiple (switch/case) visual.