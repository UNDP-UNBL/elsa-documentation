.. _installing_r:

Installing *R*
==============

Installing *R* on your machine is straightforward. Follow these steps:

1. Go to the `CRAN <http://cran.r-project.org>`_ (Comprehensive *R* Archive Network) *R* website. If you type "r" into Google it is the first entry

2. Follow the instructions below for your operating system:

.. dropdown:: Windows
   
   1.  Click on `Download R for Windows <https://cran.r-project.org/bin/windows/>`_.

   .. image:: images/windows_os/image1.gif
      :alt: image1
      :align: center

   |
         
   2.  Select the `base <https://cran.r-project.org/bin/windows/base/>`_ version. This will link to where you can can download the file.

   .. image:: images/windows_os/image2.gif
      :alt: image2
      :align: center

   |

   3.  Click on `Download R-4.4.2 for Windows <https://cran.r-project.org/bin/windows/base/R-4.4.2-win.exe>`_ (the current version at the time of writing). The link will download an installer program, which installs the most up-to-date version of R for Windows. 

   .. image:: images/windows_os/image3.gif
      :alt: image1
      :align: center

   |
   
   4.  Run the downloaded program and step through the installation wizard that appears. The wizard will install R into your program files folders and place a shortcut in your Start menu.

   **Additional Installations**
   
   For Windows users, if you plan to use the *Gurobi* solver that will be used in :ref:`training_5`, you will also need to install the `RTools <https://cran.r-project.org/bin/windows/Rtools/rtools44/rtools.html>`_  package to enable installing *Gurobi* in *R* from source (If you do not plan to use *Gurobi*, then you can disregard this step). *RTools* is toolchain bundle used for building *R* packages from source, which may require a software compiler that may not be available on most Windows systems.

   .. note:: 
      These compilers (Xcode, GCC, C++, Fortan, etc.) are often/typically installed on MacOS and Linux systems, so this extra installation does not apply to you if your systems runs either of these OS.

   To download RTools, click the `Rtools44 installer <https://cran.r-project.org/bin/windows/Rtools/rtools44/files/rtools44-6459-6401.exe>`_ link, download the file, run it, and follow the installation instructions.


.. dropdown:: macOS

   1.  Click on `Download R for macOS <https://cran.r-project.org/bin/macosx/>`_.

   2. Choose the version relevant to your operating system. 

   .. image:: images/mac_os/image1.gif
      :alt: image1
      :align: center

   |
   
   .. note:: 

      - If you have the new M1, M2, .. powered Mac, you will need to download the Arm version `R-4.4.2-arm64.pkg <https://cran.r-project.org/bin/macosx/big-sur-arm64/base/R-4.4.2-arm64.pkg>`_; 
      - if you have older Intel Macs you will need to download the `R-4.4.2-x86_64.pkg <https://cran.r-project.org/bin/macosx/big-sur-x86_64/base/R-4.4.2-x86_64.pkg>`_ version.


   3.  An installer will download and guide you through the installation process. The installer allow you to customise your installation, but the defaults will be suitable for most users. If your computer requires a password before installing new programs, you will need it here.

.. dropdown:: Linux (x64/armlinux64)
   
   1. *R* comes preinstalled on many Linux distros, but you will need to have the most updated version of *R* installed.
   2.  To update your version of *R*, or in case you need to install it in the first place, click on `Download R for Linux <https://cran.r-project.org/bin/linux/>`_; the CRAN website provides files to build *R* from source or from the official repos on Debian, Fedora, Redhat, and SUSE, and Ubuntu-based systems. Simply select your required linux flavour and then follow the directory trail to the version of Linux you wish to install on. 

   .. image:: images/linux_os/image1.gif
      :alt: image1
      :align: center

   |
   
   For example, Ubuntu based distros (e.g., Ubuntu, Linux Mint, etc.) can be installed via apt by adding the CRAN repository, as follows:

   .. code-block:: r

      # update indices
      sudo apt update -qq
      # install two helper packages we need
      sudo apt install --no-install-recommends software-properties-common dirmngr
      # add the signing key (by Michael Rutter) for these repos
      # To verify key, run gpg --show-keys /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc 
      # Fingerprint: E298A3A825C0D65DFD57CBB651716619E084DAB9
      wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
      # add the repo from CRAN -- lsb_release adjusts to 'noble' or 'jammy' or ... as needed
      sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
      # install R itself
      sudo apt install --no-install-recommends r-base 


   4.  The exact installation procedure will vary depending on the Linux distro you use. CRAN guides the process by grouping each set of source files with documentation or README files that explain how to install on your system. 

   5.  If you are a Linux user, you probably know all this by now! Apologies.

.. important::
    
    If you already have *R* installed, please ensure it has been updated recently.