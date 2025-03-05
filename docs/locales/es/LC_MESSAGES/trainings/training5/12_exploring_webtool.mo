��    (      \              �  �   �  8   C  �   |    `  e   y  +  �  �     �   �     :     J  +   d  �  �     /
     A
     _
  U   }
  �   �
  v  �  8   "  
   [  S   f  I   �       p     .   �  S   �  $   	  �   .     �     �  �  �  @   �  �  �  ]   �  4   8  G   m  J  �  <      �  =  �  �  �   c  R     �   c  -  _  t   �  {    �   ~  �   0     �     �  =      �  @      "  '   "  '   D"  a   l"  �   �"  �  �#  E   �%     �%  _   �%  W   @&     �&  �   �&  4   /'  _   d'  $   �'  �   �'     �(     �(  �  �(  K   �*  b  +  h   r-  =   �-  M   .  e  g.  G   �/  �  0   A dropdown menu allowing you to select how you would like to deal with potential OECM and degraded areas within existing Protected Areas. There are four (4) options: A heatmap of the summed (weighted) input feature layers. A map will generate and open in this tab showing the weighted input feature data layers, as well as the ``Protect``, ``Restore``, and ``Manage`` zones. It may take a little time to generate the map (depending on your computer). A tickbox option to specify whether you want to run either a single prioritisation or multiple prioritisations (one for each data theme that exists). This defaults to running a single prioritisation (the box is unticked). In the Spanish language version of the tool this shows as: After you have completed an optimisation, the results map will generate and open in this tab showing: Any increase in BPF from 0 will cause increases in memory consumption on your computer and the solver and will increase solve times. Large BPFs can produce **VERY LONG SOLVE TIMES**. If you modify this value, be sensible (typically values of 100 to 500 will induce suitable clumping in the outputs). As noted in the tool, these values cannot be smaller than the minimum area (again, as a %) that is already locked in to an action based on your lock-in selection above. Boundary Length Penalty Factor. The BLP (or sometimes called the BLM - Boundary Length Modifier) controls how compact a solutions is. Editing Weights Existing protected areas. Exploring the *Prioritizing Nature Webtool* For example, the image below (in Ecuador), if you select to lock-in OECMs (either OECMs by themselves or OECMs and degraded areas within existing protected areas), the minimum budget value for protect increases greatly. In simple terms, if OCEMs are locked-in to a  solution (in Ecuador), a minimum of 63.07% of the country is allocated to the Protect action (you can increase the budget higher, but not lower it). Global Parameters Heatmaps for each data theme. Heatmaps for each date theme. If you selected to run multiple theme prioritisations, the map in this tab will show: In the column on the left you will find global parameters that you can set for analyses you run. These do have default values that are set when you start the webtool. Starting with the top-most parameter, these are: In the first of these tabs (the left most) loads a table of the input feature data that is used in the prioritisation. Four (4) columns are shown that provide the name of the ``Data``, the data's ``Theme``, the ``Weight`` given to the feature, and a column indicating the policy the feature speaks to (either GBF or NBSAP, depending on which county tool you are looking at). In the the webtools it will appear like the image below: Input Data It may take some time to generate the map, depending on the speed of your computer. Lock-in degraded areas within existing protected areas (for restoration); Lock-in nothing; Lock-in potential OECM area (for protection) and degraded areas within existing protected area (for restoration) Lock-in potential OECM areas (for protection); Opening this tab *before* you have run an optimisation will generate a map showing: Potential OECM areas in the country. Protect, Restore, and Manage budgets. Budgets are in percentages (%) and are the maximum area of a country that  could be spatially allocated to particular action. Results & Downloads Results Map The *Prioritizing Nature Webtool* you have running locally on your computer is the same application that you can access running online for either `Ecuador <https://elsa.unbiodiversitylab.org/Bezos_ECU/>`_ or `Peru <https://elsa.unbiodiversitylab.org/Bezos_PER/>`_. You may be familiar with the tool's layout from previous trainings, meetings and workshops, but below we provide an overview of the layout of webtool running on front of you. The *Protecting Nature* prioritisation results map (and actions) The Results & Downloads is, as the name implies, where you will find the results of the prioritzaion. Once an optimisation has completed this tab will present a table the feature representation in the solution and a bar plot showing this graphically. You are also able to Download the GIS data layers (as Geotiffs) of the solution here, as well as an Excel (.xlsx) version of the output representation table and a CSV of the model parameters you passed to priortizr and the optimisation solver. The column on the right is itself made of of four (4) tabs that each have different purposes: The prioritisation map for each specific data theme. The values in the ``Weights`` column can be edited (the others cannot). The webtool is broadly broken apart into a Header across the top of the page, and two columns, the first of which (on the left) covers ~1/3 of the width of the screen, while the second column (on the right) covers ~2/3 of the width of the screen. The column on the right has four (4) tabs on it (similar to tabs in a web browser). This tab will be empty before any optimisation has been run. When this is set to 0 (the default value, shown above), each planning unit will be considered for allocation to an action based on its own attributes and contribution to the solution. When this value is greater than 0, the optimisation model will producer more grouped allocations of planning units to actions; the greater the BPF value you choose, the more the model will group planning units into actions. Project-Id-Version: ELSA Online Documentation 
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
 Un menú desplegable que te permite seleccionar cómo manejar las posibles OECM y las áreas degradadas dentro de las Áreas Protegidas existentes. Hay cuatro (4) opciones: Un mapa de calor de las capas de características de entrada sumadas (ponderadas). En esta pestaña se generará y abrirá un mapa que mostrará las capas de datos de entrada ponderadas, así como las zonas de ``Protección``, ``Restauración`` y ``Gestión``. Puede tardar un poco en generarse el mapa, dependiendo de tu computadora. Una casilla de verificación para especificar si deseas ejecutar una única priorización o múltiples priorizaciones (una por cada tema de datos disponible). Por defecto, se ejecuta una única priorización (la casilla está desmarcada). En la versión en español de la herramienta, se muestra como: Después de completar una optimización, el mapa de resultados se generará y se abrirá en esta pestaña mostrando: Cualquier aumento del BLP desde 0 provocará un mayor consumo de memoria en tu computadora y en el solucionador, además de incrementar el tiempo de resolución. Valores altos de BLP pueden producir **TIEMPOS DE RESOLUCIÓN MUY LARGOS**. Si modificas este valor, hazlo con precaución (típicamente, valores entre 100 y 500 generarán una agrupación adecuada en los resultados). Como se indica en la herramienta, estos valores no pueden ser menores que el área mínima (en %) que ya está bloqueada en una acción según la selección de bloqueo anterior. Factor de Penalización por Longitud de Frontera. El BLP (a veces denominado BLM - Modificador de Longitud de Frontera) controla cuán compacta es una solución. Edición de Pesos Áreas protegidas existentes. Explorando la *Herramienta de Priorización de la Naturaleza* Por ejemplo, en la imagen a continuación (en Ecuador), si seleccionas bloquear los OECM (ya sea solos o junto con áreas degradadas dentro de áreas protegidas existentes), el valor mínimo del presupuesto para proteger aumenta significativamente. En términos simples, si los OECM están bloqueados en una solución (en Ecuador), al menos el 63.07% del país se asignará a la acción de Protección (puedes aumentar el presupuesto, pero no reducirlo). Parámetros Globales Mapas de calor para cada tema de datos. Mapas de calor para cada tema de datos. Si seleccionaste ejecutar múltiples priorizaciones por tema, el mapa en esta pestaña mostrará: En la columna de la izquierda encontrarás parámetros globales que puedes configurar para los análisis que ejecutes. Estos tienen valores predeterminados cuando inicias la herramienta. Comenzando desde el parámetro superior, estos son: En la primera de estas pestañas (la más a la izquierda) se carga una tabla con los datos de las características de entrada utilizadas en la priorización. Se muestran cuatro (4) columnas que indican el nombre de los ``Datos``, el ``Tema`` de los datos, el ``Peso`` asignado a la característica y una columna que indica la política a la que se refiere la característica (ya sea GBF o NBSAP, dependiendo de la herramienta del país que estés utilizando). En las herramientas web aparecerá como en la imagen a continuación: Datos de Entrada Puede tardar algún tiempo en generarse el mapa, dependiendo de la velocidad de tu computadora. Bloquear áreas degradadas dentro de Áreas Protegidas existentes (para restauración); No bloquear nada; Bloquear áreas OECM potenciales (para protección) y áreas degradadas dentro de Áreas Protegidas existentes (para restauración). Bloquear áreas OECM potenciales (para protección); Abrir esta pestaña *antes* de haber ejecutado una optimización generará un mapa que muestra: Áreas OECM potenciales en el país. Presupuestos de Protección, Restauración y Gestión. Los presupuestos están en porcentajes (%) y representan el área máxima de un país que podría asignarse espacialmente a una acción determinada. Resultados y Descargas Mapa de Resultados La *Herramienta de Priorización de la Naturaleza* que tienes ejecutándose localmente en tu computadora es la misma aplicación a la que puedes acceder en línea para `Ecuador <https://elsa.unbiodiversitylab.org/Bezos_ECU/>`_ o `Perú <https://elsa.unbiodiversitylab.org/Bezos_PER/>`_. Puede que ya estés familiarizado con la estructura de la herramienta por entrenamientos, reuniones o talleres previos, pero a continuación proporcionamos una descripción general de su interfaz. El mapa de resultados de priorización de *Protecting Nature* (y acciones). La pestaña de Resultados y Descargas es, como su nombre lo indica, donde encontrarás los resultados de la priorización. Una vez que la optimización se haya completado, esta pestaña mostrará una tabla con la representación de las características en la solución y un gráfico de barras que lo muestra visualmente. También podrás descargar aquí las capas de datos GIS (en formato Geotiff) de la solución, así como una versión en Excel (.xlsx) de la tabla de representación de resultados y un archivo CSV con los parámetros del modelo que pasaste a *prioritizr* y al solucionador de optimización. La columna de la derecha está compuesta por cuatro (4) pestañas, cada una con un propósito diferente: El mapa de priorización para cada tema de datos específico. Los valores en la columna ``Pesos`` pueden editarse (las demás columnas no). La herramienta está dividida en un encabezado en la parte superior de la página y dos columnas: la primera (a la izquierda) ocupa aproximadamente 1/3 del ancho de la pantalla, mientras que la segunda (a la derecha) ocupa aproximadamente 2/3 del ancho. La columna de la derecha contiene cuatro (4) pestañas (similares a las pestañas de un navegador web). Esta pestaña estará vacía antes de ejecutar cualquier optimización. Cuando este valor se establece en 0 (el valor predeterminado, mostrado arriba), cada unidad de planificación se considerará para asignación a una acción según sus propios atributos y contribución a la solución. Cuando este valor es mayor que 0, el modelo de optimización agrupará más las unidades de planificación en las acciones; cuanto mayor sea el valor del BLP que elijas, más se agruparán las unidades de planificación en acciones. 