Linux users
===========

1. *R* comes preinstalled on many Linux distros, but you will need to have the most updated version of *R* installed.
2.  To update your version of *R*, or in case you need to install it in the first place, click on `Download R for Linux <https://cran.r-project.org/bin/linux/>`_; the CRAN website provides files to build R from source on Debian, Fedora, Redhat, and SUSE, and Ubuntu-based systems. Simply select your required linux flavour and then follow the directory trail to the version of Linux you wish to install on. 

.. image:: images/linux_os/image1.gif
   :alt: image1
   :align: center

----

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
