Training 3: *R* and *RStudio* Setup
===================================

Most software tools for conservation planning (e.g. `Marxan <https://marxansolutions.org/>`_ or `Zonation <https://zonationteam.github.io/Zonation5/>`_) do not require any specific coding skills, and only require basic GIS capabilities to correctly extract and prepare input data. However, `prioritizr <https://prioritizr.net/>`_, the tool that runs behind the scenes in ELSA (that we will be using today) is written in *R* and having a basic understanding of the *R* programming language will help with both small-scale troubleshooting and provide a better understanding of the inner workings of the ELSA tools. On top of that, understanding how *R* (or any computer language you work with) operates allows for creating fast and reproducible workflows by exploiting the advantages of the programming language. It also allows for pre- and post-processing of your data, all in *R*.

The first step to all this (of course) is to install *R*. We will also install several other useful and required software programs (or libraries), such as *RStudio*, that either are requirements for using *prioritizr* or will simply make our lives a little bit easier.

.. important:: 

   Even if you already have *R*, *RStudio*, and some of the required packages installed, we recommend making sure that all of these are updated regularly and on the latest version. Some of the material provided here might throw errors if old software versions are used.


.. toctree::
   :maxdepth: 2

   installing_r
   installing_rstudio
   using_rstudio
   creating_r_projects
   installing_packages
   installing_solvers
