# Face-computervision-azure

Face-computervision-azure trata de una app en Flask, en la cual, podemos introducir la url de una imagen y extraer información de ella con el uso de Face y ComputerVision (Azure).

## Installation

La app (Flask) es levantada en un entorno virtual y las librerías utilizadas las podemos encontrar en requimerents.txt

## Usage

Crear entorno virtual en app e instalar las librerías que podemos encontrar en requirements.txt

```bash
# activar entorno virtual
# Linux:
app$ source venvPr/bin/activate
# Windows:
app$ venvPr\Scripts\activate.bat
(venvPr) app/code$ python -m pip install -r requirements.txt

export FLASK_APP=app
export FLASK_ENV=development

# levantar app
(venvPr) app/code$ flask run
```
