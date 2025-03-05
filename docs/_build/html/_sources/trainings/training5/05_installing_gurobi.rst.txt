.. _installing_gurobi:

Installing Gurobi
=================

The exact methods for installing the *Gurobi* solver depends on the operating system installed on your computer. Thankfully *Gurobi* provides detailed `platform-specific instructions <https://support.gurobi.com/hc/en-us/articles/4534161999889-How-do-I-install-Gurobi-Optimizer>`_ for Windows, MacOS, and Linux systems that should help with this. 

Broadly speaking, on Windows systems, you need only double-click on the *Gurobi* installer, follow the prompts, and the installer will automatically handle everything for you (using default settings). On Linux and MacOS systems, you will need to manually extract the downloaded file’s contents to a folder, move the extracted contents to a suitable location (typically ``/opt/gurobi``), and update your system’s variables so that it knows where to find *Gurobi* (i.e., the PATH variable). See OS specific instructions below for more details.

After installing the *Gurobi* software suite on your computer, you will need to activate your license.

.. important:: 
   
   *Gurobi* is a commercial and proprietary computer program. This means that is will not work without a valid license - downloading the software is also not possible without being registered with *Gurobi*. 
   
   We provide a short term usage of our cloud license for the *Prioritizing Nature* Trainings, only. Academics (including students) can obtain a special free license at no cost but individuals and others that are not affiliated with a recognized educational institution may need to purchase a license.


.. dropdown:: Windows

   Double-click on the Gurobi installer that you downloaded (unless you selected *Run* when downloading. in which case you've already run the installer and don't need to do it again.)

   By default, the installer will place the Gurobi 12.0.* files in the directory ``c:\gurobi1201\win64``. The installer gives you the option to change the installation target, but it's easiest to accept the default settings.

   The installer can also be used to repair or remove a past installation.

   .. note:: 

      To work with compressed files within Gurobi Optimizer, it is recommended that you install `gzip <www.gzip.org>`_ and/or `7zip <www.7-zip.org>`_.


.. dropdown:: macOS

   Double-click on the appropriate Gurobi installer (e.g., gurobi12.0.1_macos_universal2.pkg for Gurobi 12.0.1) and follow the prompts.

   By default, the installer will place the Gurobi 12.0.* files in ``/Library/gurobi1201/macos_universal2`` (note that this is the system ``/Library`` directory, not your personal ``~/Library`` directory).

   .. note::
      
      Your <installdir>  will be ``/Library/gurobi1201/macos_universal2``.


.. dropdown:: **Linux (x64/armlinux64)**
   
   .. note:: 
      
      The following instructions are for **x64** and **armlinux64** Linux systems only.

   Extract the download to your chosen destination directory. Gurobi recommend ``/opt`` for a shared installation (assuming you have sudo privileges to write in that directory), or your home directory for a private installation, but other directories will work as well. You'll need to change your working directory to the destination directory:
   
   For example: 
   
   .. code-block::
   
      cd /opt
      
   Then copy the *Gurobi* distribution to that directory, and then extract the contents:

   .. code-block:: r

      tar xvfz gurobi12.0.1_linux64.tar.gz

   or

   .. code-block:: r

      tar xvfz gurobi12.0.1_armlinux64.tar.gz


   This command will create a sub-directory ``/opt/gurobi1201/linux64`` or ``/opt/gurobi1201/armlinux64`` that contains the complete Gurobi distribution (assuming you chose /opt). Your <installdir> will be this subdirectory.

   Gurobi's Optimizer makes use of several executable files. To allow these files to be found when needed, you will need to modify a few environment variables:

   - ``GUROBI_HOME`` should point to your ``<installdir>``.

   - ``PATH`` should be extended to include ``<installdir>/bin``.
      
   - ``LD_LIBRARY_PATH`` should be extended to include ``<installdir>/lib``.


   If you are using *RStudio* on a Linux system, you might need to add the following text to a *Rstudio* configuration file (located at ``/etc/rstudio/rserver.conf``):

   .. code-block:: r

      rsession-ld-library-path=/opt/gurobi1201/linux64/lib

   We have also found that on some Ubuntu based distros (e.g., Ubuntu, Linux Mint) you may need to run the following:

   .. code-block:: 

      echo "/opt/gurobi1201/linux64/lib" > /etc/ld.so.conf.d/gurobi.conf

