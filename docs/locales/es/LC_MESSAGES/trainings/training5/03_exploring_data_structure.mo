��          �               �  �   �  )   F  #   p  �   �     w     �  �   �    E  9   V  �   �  �   #  Z   �  s       �  S   �  {  �  �   \
  `   )  ^   �  �   �  Z   k  b   �  �  )  �   �  1   ~  2   �  �   �     �     �  �   �  4  �  8   �  �   (  �   �  �   o  �   �    r  _   �  �  �  "  �  v   �  y   S  �   �  n   p  ~   �   Before going further we need to exact the .zip archive we downloaded. Use an extract tool available on your system to extract the downloaded zip archive to a location on your computer. Exploring the Repository's Data Structure Important files for the RShiny app: Make Sure you extract the data to a location that is easy to find and that you have both read and write permissions to, such as your home directory or Desktop (not to a shared network drive that may restrict your permissions). Other important files: Sub-folders The ``gurobi.env`` file will provide access to the *Gurobi* cloud solver only during  the workshop and trainings, and will be deactivated shortly after the workshop ends. The extracted contents of the zip archive (shown for the Ecuador branch) can been seen below in a tree format. While this may be more info that you want, we will describe several of the important files and what they do further down. Don't spent too long looking at this... Three (3) subfolders exist: ``data``, ``R``, and ``www``: To discuss with us how we can support continued use of *Gurobi* after the trainings and workshops please contact us support@unbiodiversitylab.org. ``R`` contains helper and utility functions that are used within the *Rshiny* app to carry out specific calculations and produce map outputs. ``data`` and ``elsa_inputs`` contain all the geospatial input files to make the tools run. ``global.R`` an *R* script that loads input data and other parameters globally at the starting of the *Rshiny* app. ``gurobi.env`` You will not see this file in the downloaded repository; it is a file we will pass to you during the workshop that will allow you too access the Gurobi cloud solver. It will need to be saved into the root directory of the *Prioritizing Nature Webtool*. ``packages.R`` a script that loads all the *R* packages and libraries in one place. ``pre_run.R`` an *R* script that carries out some pre-processing of data layers, reads in file names, file information, feature weights, feature impact scores, and budget values for the tool. It reads in data from the ``prioritizing-nature-database-master.xlsx`` and points towards (and creates internal data links to geospatial data found in the ``data/elsa_inputs`` directory). ``prioritizing-nature-database-master.xlsx`` an Excel spreadsheet that provides a simplified location for users to provide default feature weights, feature impacts scores, and layer info and descriptions. ``server.R`` a required *R* script that includes all the logic of the *Rshiny* app when it runs. ``start.R`` a required *R* script that does what it name implies - it starts the *RShiny* app. ``translation-matrix.xlsx`` an excel sheet of translation strings used to convert text in the app to language other than English. ``ui.R`` a required script that manages the user interface and design of the *Rshiny* app. ``www``. Some custom css and background images for the app. There is nothing for you to note here. Project-Id-Version: ELSA Online Documentation 
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2025-02-28 18:59+1000
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: es
Language-Team: es <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1);
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.17.0
 Antes de continuar, necesitamos extraer el archivo .zip que descargamos. Usa una herramienta de extracción disponible en tu sistema para descomprimir el archivo en una ubicación de tu computadora. Explorando la Estructura de Datos del Repositorio Archivos importantes para la aplicación *RShiny*: Asegúrate de extraer los datos en una ubicación fácil de encontrar y en la que tengas permisos de lectura y escritura, como tu directorio personal o el Escritorio (no en una unidad de red compartida que pueda restringir tus permisos). Otros archivos importantes: Subcarpetas El archivo ``gurobi.env`` proporcionará acceso al solucionador en la nube de *Gurobi* solo durante el taller y las capacitaciones, y será desactivado poco después de que finalice el taller. El contenido extraído del archivo .zip (mostrado para la rama de Ecuador) se puede ver a continuación en formato de árbol. Aunque esto puede ser más información de la que necesitas, describiremos varios de los archivos importantes y su función más adelante. No te preocupes demasiado por esto ahora... Existen tres (3) subcarpetas: ``data``, ``R`` y ``www``: Para discutir cómo podemos apoyar el uso continuo de *Gurobi* después de las capacitaciones y talleres, por favor contáctanos en support@unbiodiversitylab.org. ``R`` contiene funciones auxiliares y utilitarias que se utilizan dentro de la aplicación *RShiny* para realizar cálculos específicos y generar mapas de salida. ``data`` y ``elsa_inputs`` contienen todos los archivos de entrada geoespaciales necesarios para que las herramientas funcionen. ``global.R`` es un script de *R* que carga datos de entrada y otros parámetros globalmente al inicio de la aplicación *RShiny*. ``gurobi.env`` No verás este archivo en el repositorio descargado; es un archivo que te proporcionaremos durante el taller y que te permitirá acceder al solucionador en la nube de Gurobi. Deberás guardarlo en el directorio raíz de la herramienta *Prioritizing Nature Webtool*. ``packages.R`` es un script que carga todos los paquetes y bibliotecas de *R* en un solo lugar. ``pre_run.R`` es un script de *R* que realiza un preprocesamiento de las capas de datos, lee los nombres de archivos, la información de los archivos, los pesos de las características, las puntuaciones de impacto de las características y los valores de presupuesto para la herramienta. Lee los datos desde ``prioritizing-nature-database-master.xlsx`` y apunta (y crea enlaces internos) a los datos geoespaciales ubicados en el directorio ``data/elsa_inputs``. ``prioritizing-nature-database-master.xlsx`` es una hoja de Excel que proporciona una ubicación simplificada para que los usuarios definan los pesos predeterminados de las características, las puntuaciones de impacto de las características y la información y descripciones de las capas. ``server.R`` es un script obligatorio de *R* que incluye toda la lógica de la aplicación *RShiny* cuando se ejecuta. ``start.R`` es un script obligatorio de *R* que hace exactamente lo que su nombre indica: inicia la aplicación *RShiny*. ``translation-matrix.xlsx`` es una hoja de Excel con cadenas de traducción utilizadas para convertir el texto de la aplicación a un idioma distinto del inglés. ``ui.R`` es un script obligatorio que gestiona la interfaz de usuario y el diseño de la aplicación *RShiny*. ``www``. Contiene archivos CSS personalizados e imágenes de fondo para la aplicación. No hay nada que debas modificar aquí. 