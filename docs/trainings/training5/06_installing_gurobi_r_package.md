# Installing the *Gurobi R* package

To use *Gurobi's R* interface, you will need to install the *Gurobi* package in your *R* installation. The generalised *R* command for doing this is:

```r
install.packages('<R-package-file>', repos=NULL)
```The *Gurobi R* package file can be found within the directory where you installed *Gurobi* on your system (see :ref:`installing_gurobi` if you have not already successfully installed *Gurobi* on your computer). The default installation directory is:

-   For **64-bit Windows**: `C:\gurobi1201win64` , and
-   For **MacOS**: `/Library/gurobi1201/macos_universal2`,
-   For **Linux** systems: `/opt/gurobi1201/linux64`

!!! note
    Update the version number in the path if you have installed a different Gurobi version.

You will find the exact name of the file for your operating system inside the `<installdir>/R`.

-   For **64-bit Windows** this is: `gurobi_12.0-1.zip` , and
-   For **MacOS** this is: `gurobi_11.0-0_R_.tgz`,
-   For **Linux** systems this is: `gurobi_12.0-1_R_.tar.gz`

Operating specific instructions can be found below:

??? note "Windows"
     ```r

     ```        > install.packages("c:\gurobi1201win64/linux64/R/gurobi_12.0-1_R_4.4.0.tar.gz", repos = NULL)
        Installing package into ‘/home/scottca/R/x86_64-pc-linux-gnu-library/4.4’
        (as ‘lib’ is unspecified)
        * installing *binary* package ‘gurobi’ ...
        * DONE (gurobi)

    
??? note "macOS"
     ```r

     ```        > install.packages("/Library/gurobi1201/macos_universal2/linux64/R/gurobi_12.0-1_R_4.4.0.tar.gz", repos = NULL)
        Installing package into ‘/home/scottca/R/x86_64-pc-linux-gnu-library/4.4’
        (as ‘lib’ is unspecified)
        * installing *binary* package ‘gurobi’ ...
        * DONE (gurobi)

??? note "Linux (x64/armlinux64)"
     ```r

     ```        > install.packages("/opt/gurobi1201/linux64/R/gurobi_12.0-1_R_4.4.0.tar.gz", repos = NULL)
        Installing package into ‘/home/scottca/R/x86_64-pc-linux-gnu-library/4.4’
        (as ‘lib’ is unspecified)
        * installing *binary* package ‘gurobi’ ...
        * DONE (gurobi)

    There is likely nothing else you need to do. Pat yourself on the back for using Linux and being awesome.

Depending on your local *R* environment you might need to install the R package slam. To do this, you should issue the following command in the *RStudio* console:

```r
install.packages('slam')
```Test that gurobi installed correctly by running:
    
```r
> library(gurobi)
Loading required package: slam
```!!! important
    You will need to be careful to make sure that the *R* binary and the *Gurobi* package you install both use the same instruction set. For example, if you are using the 64-bit version of *R*, you’ll need to install the 64-bit version of *Gurobi*, and the 64-bit *Gurobi R* package. This is particularly important on Windows systems, where the error messages that result from instruction set mismatches can be quite cryptic.
