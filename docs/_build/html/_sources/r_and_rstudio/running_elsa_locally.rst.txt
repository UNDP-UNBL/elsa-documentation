Running ELSA Locally
====================

Rshiny
^^^^^^

The  ELSA national tools we will be setting up to run locally and working with during this workshop uses *Rshiny*. *RShiny* is an *R* package that allows users to create interactive web applications directly from *R* code without the need for specialist web programming skills - meaning that in a nutshell, users can build functional web applcations and open the application in their web browser (Chrome, Firefox, Safari, etc). Some of the key features of *RShiny* are:

-   It provides a web application framework for *R*, allowing for interactive app development.
-   Includes reactive programming, allowing for automatically updating of outputs when inputs change.
-   It integrates with other *R* libraries, working seamlessly with *ggplot2*, *leaflet*, *dplyr*, *shinyWidgets*, etc.
-   Apps can be deployed on Web and hosted on `ShinyApps.io <https://www.shinyapps.io/>`_, `RStudio Connect <https://posit.co/products/enterprise/connect/>`_, or private servers (see the example below).

.. image:: ../running_elsa/images/bezos_tool_per_reduced.png
    :align: center

-----

.. note::
    
    We run the various national ELSA web tools on private and secure UNICC infrastructure.


ELSA Code Repositories (Git)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TO DO:

-   Git hub repo download - which branch

-   Data and files set up
-   Need to run pre-run.R

    -   Need to set up to run locally and not via CLI 


Getting the Input GIS Data 
^^^^^^^^^^^^^^^^^^^^^^^^^^

-   Download link to data
-   Setting up an R project and file structure

Setting it all up
^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1
   
   ../running_elsa/installing_required_packages
   ../running_elsa/using_gurobi   
