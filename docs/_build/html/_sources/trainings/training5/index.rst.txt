.. _training_5:

Training 5: Running Spatial Prioritisations
===========================================

This module is an online workshop followed by interactive exercises. It will provide training on how to import the spatial data from the Prioritizing Nature Project to the prioritizr, and run the prioritizr analysis in R software to generate the spatial prioritization map. 

.. important:: 
    
    Participants are expected to have basic knowledge of GIS, R software and language, such as running scripts in R


Rshiny
^^^^^^

The  ELSA national tools you may have seen or used on-line are built using *RShiny*, and those we will be setting up to run locally on your computer during this workshop also use *Rshiny*. *RShiny* is an *R* package that allows users to create interactive web applications directly from *R* code without the need for specialist web programming skills - meaning that in a nutshell, users can build/run functional web applications by simply opening the application in their web browser (Chrome, Firefox, Safari, etc). Some of the key features of *RShiny* are:

-   It provides a web application framework for *R*, allowing for interactive app development.
-   Includes reactive programming, allowing for automatically updating of outputs when inputs change.
-   It integrates with other *R* libraries, working seamlessly with with the `tidyverse <https://www.tidyverse.org/>`_ (e.g., *ggplot2*, *dplyr*, *readr*, etc.) *leaflet*, *shinyWidgets*, *terra*, and other *R* libraries.
-   Apps can be deployed on Web and hosted on `ShinyApps.io <https://www.shinyapps.io/>`_, `RStudio Connect <https://posit.co/products/enterprise/connect/>`_, or on private servers (for example, one of the tools for Peru seen below).

.. image:: images/bezos_tool_per_reduced.png
    :align: center

-----

.. important:: 
    
    We run the various national ELSA web tools on private and secure UNICC infrastructure.


ELSA Code Repositories (Git)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TO DO:

-   Git hub repo download - which branch

-   Data and files set up
-   Need to run pre-run.R

    -   Need to set up to run locally and not via CLI 

Download as zip file


GIS Data Downloads 
^^^^^^^^^^^^^^^^^^
Data stacks for this workshop have been pre-created so that we can focus less on data processing and more on working with and understanding the ELSA outputs.

Download the data stack for your country of interest below:

-   `Peru <TBD>`_
-   `Ecuador <TBD>`_

-   Setting up an *R* project and file structure

Setting it all up
^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1
   
   installing_required_packages
   setting_up_gurobi   
