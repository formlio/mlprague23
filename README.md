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
be spent working with the [ForML](http://forml.io/) framework implementing a practical end-to-end
ML solution demonstrating all of these declared principles.

[MLPrague](https://www.mlprague.com/) 2023 Workshop


Setup
-----

1. Clone the [workshop repository](https://github.com/formlio/mlprague23):
```shell
$ git clone git@github.com:formlio/mlprague23.git
$ cd mlprague23
```
2. [Install Docker Engine](https://docs.docker.com/engine/install/) along with the [Docker Compose plugin](https://docs.docker.com/compose/install/) (should be already part of any recent docker engine version).
3. Spin up the workspace container from within the `mlprague23` project root directory (this will need to bind ports `8888`, `8000` and `4040` on your machine):
```shell
$ docker compose up -d
```
4. Load the workspace notebook interface at [http://127.0.0.1:8888/lab](http://127.0.0.1:8888/lab) using your browser.
