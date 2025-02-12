Installing Solvers (General)
============================

.. note:: 

   This section is not required reading for the Protecting Nature workshops, since we will making use of our paid Gurobi solver license. It is worth familiarising yourself with the text below, but feel free to skip foward to :ref:`using_gurobi`.
   
   
Solving conservation problems with *prioritizr* also requires having a solver installed on your machine. Solvers use specific algorithms that use mathematical optimization to find an optimal solution to a problem. There are many different solvers available that differ in terms of their efficiency and cost. The best solvers are proprietary and usually expensive to use, but there are some good free ones available. For more information on solver comparisons and benchmarks, the developers of *prioritizr* have written a helpful `article <https://prioritizr.net/articles/solver_benchmarks.html>`_ .

.. note:: 

   If you are affiliated with an academic institution, you might have access to a free academic license of Gurobi, one of the state-of-the-art solvers out there. While we will not go through a step-by-step guide on how to install Gurobi here, there are many resources on how to install Gurobi, for example `the installation guide <https://prioritizr.net/articles/gurobi_installation_guide.html>`_ on the *prioritizr* website. We recommend using this solver if you have access to it.

In general, we recommend using one of the freely available solvers that are supported by *prioritizr* and are easily installed, such as the SYMPHONY solver, which can be installed using.

If you are a Windows user, *lpsympony* might work better. Check their website for more details: https://www.bioconductor.org/packages/release/bioc/html/lpsymphony.html.

.. code-block:: r
   
   if (!require(remotes)) install.packages("remotes")
   remotes::install_bioc("lpsymphony")

If you are a Mac/Linux user, rcbc might work better. Check their README for more details https://github.com/dirkschumacher/rcbc.

.. code-block:: r
   
   if (!require(remotes)) install.packages("remotes")
    remotes::install_github("dirkschumacher/rcbc")

Alternatively, if the installation fails for some reason, on your machine, try installing the HiGHS solver.

.. code-block:: r
   
   install.packages("highs")


