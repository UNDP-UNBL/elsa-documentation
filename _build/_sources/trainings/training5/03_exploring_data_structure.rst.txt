Exploring the Repository's Data Structure
=========================================

Before going further we need to exact the .zip archive we downloaded. Use an extract tool available on your system to extract the downloaded zip archive to a location on your computer.

.. important::
    
    Make Sure you extract the data to a location that is easy to find and that you have both read and write permissions to, such as your home directory or Desktop (not to a shared network drive that may restrict your permissions).

The extracted contents of the zip archive (shown for the Ecuador branch) can been seen below in a tree format. While this may be more info that you want, we will describe several of the important files and what they do further down. Don't spent too long looking at this...

.. code-block:: text

    .
    ├── data
    │   └── elsa_inputs
    │       ├── aprovechamiento_sustentable_galapagos_2017_ecu_bezos.tif
    │       ├── areasprioritarias_ecu_bezos.tif
    │       ├── aves_richness_ecu_bezos.tif
    │       ├── bosque_nativo_2022_ecu_bezos.tif
    │       ├── conservation_galapagos_2017_ecu_bezos.tif
    │       ├── contaminacion_hidrocarburo_ecu_bezos.tif
    │       ├── costal_ecu_bezos.tif
    │       ├── desertificacion_ecu_bezos.tif
    │       ├── drought_suscept_ecu_bezos.tif
    │       ├── flood_suscept_ecu_bezos.tif
    │       ├── forestfires_suscept_ecu_bezos.tif
    │       ├── forest_restore_priority_agreement_land_ecu_bezos.tif
    │       ├── indigenous_territories_ecu_bezos.tif
    │       ├── kba_2024_ecu_bezos.tif
    │       ├── mangrove_union_ecu_bezos.tif
    │       ├── mass_movement_suscept_ecu_bezos.tif
    │       ├── ncs_restore_ecu_bezos.tif
    │       ├── paramos_2022_ecu_bezos.tif
    │       ├── pa_restore_ecu_bezos.tif
    │       ├── potential_oecms_ecu_bezos.tif
    │       ├── production_forest2020_ecu_bezos.tif
    │       ├── protection_forest2020_ecu_bezos.tif
    │       ├── protect_zone_ecu_bezos.tif
    │       ├── restoration_actions2023_ecu_bezos.tif
    │       ├── restore_zone_ecu_bezos.tif
    │       ├── snap2023_ecu_bezos.tif
    │       ├── soc2021_ecu_bezos.tif
    │       ├── vaciosconservacionsnap_ecu_bezos.tif
    │       ├── veg_conectivity_ecu_bezos.tif
    │       ├── veg_threat_ecu_bezos.tif
    │       ├── vulnerable_agricultural_frontier_ecu_bezos.tif
    │       └── zona_intangible_galapagos_2017_ecu_bezos.tif
    ├── global.R
    ├── packages.R
    ├── pre_run.R
    ├── prioritizing-nature-database-master.xlsx
    ├── R
    │   ├── calc_feature_representation.R
    │   ├── define_problem.R
    │   ├── get_coverage.R
    │   ├── get_leaflet_basemap.R
    │   ├── get_min_lockin_target.R
    │   ├── get_target.R
    │   ├── get_translation.R
    │   ├── make_elsa_categorical_raster.R
    │   ├── make_elsa_representation_plot.R
    │   ├── make_leaflet_elsa_0.R
    │   ├── make_leaflet_elsa_1.R
    │   ├── make_leaflet_input.R
    │   └── move_elsa_files.R
    ├── README.md
    ├── server.R
    ├── shiny-server.conf
    ├── start.R
    ├── translation-matrix.xlsx
    ├── translations.rds
    ├── ui.R
    └── www
        ├── custom.css
        └── ELSA_reduced.jpeg

Sub-folders
^^^^^^^^^^^

Three (3) subfolders exist: ``data``, ``R``, and ``www``:

-   ``data`` and ``elsa_inputs`` contain all the geospatial input files to make the tools run.
-   ``R`` contains helper and utility functions that are used within the *Rshiny* app to carry out specific calculations and produce map outputs.
-   ``www``. Some custom css and background images for the app. There is nothing for you to note here.

Important files for the RShiny app:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-   ``ui.R`` a required script that manages the user interface and design of the *Rshiny* app.
-   ``start.R`` a required *R* script that does what it name implies - it starts the *RShiny* app.
-   ``global.R`` an *R* script that loads input data and other parameters globally at the starting of the *Rshiny* app.
-   ``packages.R`` a script that loads all the *R* packages and libraries in one place. 
-   ``server.R`` a required *R* script that includes all the logic of the *Rshiny* app when it runs. 

Other important files:
^^^^^^^^^^^^^^^^^^^^^^

-   ``translation-matrix.xlsx`` an excel sheet of translation strings used to convert text in the app to language other than English.
-   ``prioritizing-nature-database-master.xlsx`` an Excel spreadsheet that provides a simplified location for users to provide default feature weights, feature impacts scores, and layer info and descriptions. 
-   ``pre_run.R`` an *R* script that carries out some pre-processing of data layers, reads in file names, file information, feature weights, feature impact scores, and budget values for the tool. It reads in data from the ``prioritizing-nature-database-master.xlsx`` and points towards (and creates internal data links to geospatial data found in the ``data/elsa_inputs`` directory). 
-   ``gurobi.env`` You will not see this file in the downloaded repository; it is a file we will pass to you during the workshop that will allow you too access the Gurobi cloud solver. It will need to be saved into the root directory of the *Prioritizing Nature Webtool*.

.. note:: 

    The ``gurobi.env`` file will provide access to the *Gurobi* cloud solver only during  the workshop and trainings, and will be deactivated shortly after the workshop ends.

    To discuss with us how we can support continued use of *Gurobi* after the trainings and workshops please contact us support@unbiodiversitylab.org.
