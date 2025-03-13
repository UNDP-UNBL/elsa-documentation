Running the *Prioritizing Nature Webtool* - Data Setup
======================================================

Before the *Prioritizing Nature Webtool* app can run we needs to run a script called ``pre_run.R``. The ``pre_run.R`` script has several primary functions:

1) It reads in information from the ``prioritizing-nature-database-master.xlsx`` Excel sheet on:

    -   Feature names (including local translations),
    -   File names;
    -   Feature weights;
    -   Feature impact scores; and
    -   Budget values,
    -   and other feature layers metadata (policy relevance, source info, etc)

2) It does any geospatial work needed to prepare input feature, zone, locked in area, and *prioritizr* zone data and layers, and creates file pointers to the rasters found in ``data/elsa_inputs`` so they can be used by the `terra` package.  

An compressed *R* data format file called ``prioritizing_nature.Rdata`` is created at the end of the the ``pre_run.R`` - this is read back back in quickly and efficiently when the RShiny app is run, and called in the ``global.R`` function.

Running `pre_run.R`
^^^^^^^^^^^^^^^^^^^

1) Open the ``pre_run.R`` file by typing either **Ctrl+O** or clicking on **File → Open File...** and selecting the ```pre_run.R`` file.

2) Inspect lines 11-18 of the script:

.. code-block:: r

    iso3 <- "ECU" # not used - local testing only
    country <- "Ecuador"
    language <- "es" # not used - local testing only
    input_spreadsheet <- "prioritizing-nature-database-master.xlsx"
    sheetname <- "ECU_data_stack"
    blm <- 0
    reducedres <- FALSE
    weight_cal <- FALSE

3) Ensure that they point to the correct ``iso3`` code (i.e., ``ECU`` if you are working with Ecuador's data and ``PER`` if Peru)

4) Ensure the language is set to the language you prefer: currently options are English, Spanish, and French.

4) Ensure the ``input_spreadsheet`` and ``sheetname`` variables are correct.

The ``blm``, ``reducedres``, and ``weight_cal`` fields should be left as is - they should only be changed if you need to rerun pre-calibration weights or do local testing on reduced resolution data (so it runs faster).

5) Run the ``pre_run.R`` script by either 
    
    1) Typing **Ctrl+Alt+Enter** (which is the same as running:

    .. code-block:: r

        source('pre_run.R')

    2) Or clicking on the |pre_run1| button in the upper right side of the editor panel.

.. |pre_run1| image:: images/pre_run1.png

6) You will see the script running in the console window - it may take several minutes depending on how powerful your computer is.

.. code-block:: r

    > #!/usr/bin/env Rscript
    > source("packages.R")
    > [...]
    > save.image(here::here("prioritizing_nature.RData"), compress = "gzip")
    > gc()
                used  (Mb) gc trigger  (Mb) max used  (Mb)
    Ncells 4778855 255.3    8503747 454.2  8503747 454.2
    Vcells 7689927  58.7   14786712 112.9 14786554 112.9
    > # terra::tmpFiles(remove = TRUE)

If you see any errors here, let us know.