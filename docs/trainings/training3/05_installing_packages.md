# Installing *R* packages

One of the most useful things about the *R* language is the very large number of software libraries that *R* users have created for often very specific use cases. Indeed, many of *R*'s most useful functions are found in these packages. An *R* package bundles together useful functions, help files, and data sets, and they can be used within your own *R* scripts once you have installed and then loaded the library in your *R* session. 

## Using base *R*

#### Installing packages

To install a package we can use base *R* functions:

```r
install.packages()
```For example, within an RStudio session, type (or copy/paste) the following into the console, press `Enter`:

```r
install.packages("terra")
install.packages("sf")
```Multiple packages can be installed at the same time by passing (i.e., concatenating) the names of each package within the `c()` function. 

For example, within an RStudio session, type (or copy/paste) the following into the `Console` panel, and press `Enter`:

```r
install.packages(c("prioritizr", "terra", "sf"))
```#### Loading packages

To load a package that we already have correctly installed, we can use the base *R* function:

```r
library()
```This function can be used in the console as well; however, typically we will want to load installed packages within a script we are developing, that will be saved (as a `.R` file) for later use. By convention, best practice is to install and load all necessary packages to run each script at the top of the *R* script, one package per line (although, see the :ref:`pacman` section below). First, within your open *RStudio* session, we need to create a new R Script, either by:

-   Clicking on **File →  New File → R Script** or
-   Typing `Ctrl+Shift+N` on your keyboard (**NOTE: your keyboard shortcuts may differ!**)

This will open a new (empty) text file in your `Source` panel; type (or copy/paste) the following into the new file.

```r
library("terra")
library("sf")
```Before running these lines of code we must save our new script, either by:

-   Clicking on **File → Save As...**
-   Typing `Ctrl+S`
-   These will open a dialogue window - save your file to location you will remember. It will automatically have the `.R` file type appended to it.

!!! note
    Clicking on **File → Save** will also work if you are saving a new file the first time 

You can now run the new script by either:

-   Clicking on the `Source` button (on the top right of the `Source` panel in RStudio)
-   Typing `Ctrl+Shift+S` or `Ctrl+Shift+Enter`.

Some information about the versions of you packages, and other information, may print to your `Console` window (or report errors if they occur... eeek!)

[pacman]: ## pacman

#### Installing and loading packages

One particularly useful *R* package that helps streamline the installation of R packages that are in the CRAN repositories is **pacman**. Following the conventional best practice of installing and loading all packages required to run each script at the top of the R script, **pacman** can simplify the process by both installing (if not previously installed) and loading required packages, in a more concise format. 

First, create a new R Script as done previously, and save it to disk. We will need to install the **pacman** first; afterwards we can use the `pacman::p_load()` function both install (again, if not already installed) and load the desired packages. Type (or copy/paste) the following into the new file:

```r
install.packages("pacman")
pacman::p_load(tidyverse, terra, prioritizr)
```You can now run your script using the methods shown above (e.g., typing `Ctrl+Shift+S`, `Ctrl+Shift+Enter`, or clicking on the `Source` button).
