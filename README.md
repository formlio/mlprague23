Reproducible, Portable, and Distributable ML Solutions in Python
================================================================

When achieved, the combination of reproducibility, portability, and distributability in ML
solutions constitutes a powerful faculty unlocking a number of operational opportunities.
While reproducibility is a well-established pathway for conducting scientific research, it is not
always receiving the same recognition within the data product industry. Similarly, portability
and distributability are typically regarded as irrelevant for bespoke solutions and only
pursued in case of explicit demands. This might be reasonable given the extra cost incurred
by conventional development; but with modern tooling, these properties can be easily
achieved without much extra effort. In return, this brings significant benefits in the form of
highly collaborative R&D, inherent lifecycle management, effective model troubleshooting,
carefree and flexible deployment (latency/throughput-optimal runtime modes), and even
potential commoditization (market of turnkey solutions).
In this workshop, we will dive deeper into these concepts examining carefully the available
technologies and reviewing some of the existing tools. A significant amount of the time will
be spent working with the [ForML](http://forml.io/) framework implementing a practical end-to-end ML solution demonstrating all of these declared principles.

[MLPrague](https://www.mlprague.com/) 2023 Workshop


Setup
-----

Clone this repository:

    $ git clone git@github.com:formlio/mlprague23.git
    $ cd mlprague23


Docker
^^^^^^

The recommended way to save time during this workshop is to perform all the
steps in the pre-built Docker container.

1. [Install Docker Engine](https://docs.docker.com/engine/install/) along with
   the [Docker Compose plugin](https://docs.docker.com/compose/install/).
2. Edit the [`.env`](.env) file and supply your local `UID` and `GID` numbers.

  * Use the `id` (or `id -u` and `id -g` respectively) on Mac/Linux to find out
    your UID/GID.

3. Spin up the workspace container from within the `mlprague23` project root
   directory:

    $ docker compose up

4. Load the [workspace notebook interface](http://127.0.0.1:8888/lab) using
   your browser.


From Scratch
^^^^^^^^^^^^

The following procedure can be followed to setup the environment without Docker.
It is, however, not recommended due to the limitted time during the workshop.

1. [Install ForML](https://docs.forml.io/en/latest/install.html) (with at least
   the `dask`, `graphviz`, `rest`, `spark` and `sql` extras).
2. [Confgiure your platform](https://docs.forml.io/en/latest/platform.html)
   based on the [config.toml](config.toml) to replicate the setup used
   throughout this tutorial.
3. [Install OpenLake](https://openlake.readthedocs.io/en/latest/install.html)
   feed (with at least the `kaggle` extras).
4. Unless pre-existing, [register a Kaggle account](https://www.kaggle.com/)
   and [setup your API token](https://www.kaggle.com/docs/api) (`kaggle.json`).
5. [Accept the Avazu dataset terms](https://www.kaggle.com/competitions/avazu-ctr-prediction/data).
6. [Install and launch](https://jupyter.org/install) JupyterLab to access the
   notebooks.
