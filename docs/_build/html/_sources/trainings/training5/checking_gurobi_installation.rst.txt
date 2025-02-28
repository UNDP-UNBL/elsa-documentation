Checking if your *Gurobi R* Installation was Successful
=======================================================

To double check that you have correctly installed *Gurobi* and that it correctly uses a license allowing it connect to our cloud solver subscription (or to a local license if you have a local license), you run one of the *R* examples provided with the *Gurobi* distribution. For example, in the RStudio console window you can type:

.. code-block:: r
    
    source('mip.R')

.. important:: 

    This needs to include the full path to the ``mip.R`` file in the examples directory in your *Gurobi* installation; for example, on Linux including the full path would look like:

    .. code-block:: r 
        
        source('/opt/gurobi1201/linux64/examples/R/mip.R')


If the *Gurobi R* package was successfully installed, you should see the following output:

.. code-block:: r

    [1] 'Solution:'
    [1] 3
    [1] 1 0 1