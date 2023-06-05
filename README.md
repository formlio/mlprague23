Reproducible, Portable, and Distributable ML Solutions in Python
================================================================

When achieved, the combination of reproducibility, portability, and distributability in machine
learning (ML) solutions becomes a powerful capability that unlocks numerous operational
opportunities.

While reproducibility is a well-established practice in scientific research, it often doesn't
receive the same recognition in the data product industry. Similarly, portability and
distributability are typically considered irrelevant for custom solutions and are only pursued when
explicitly required. However, with modern tooling, these properties can be easily achieved without
significant additional effort. As a result, they offer substantial benefits such as highly
collaborative research and development, inherent lifecycle management, effective model
troubleshooting, seamless and flexible deployment (latency/throughput-optimal runtime modes), and
even potential commoditization in the form of turnkey solutions.

In this workshop, we will delve deeper into these concepts, carefully examining the available
technologies and reviewing existing tools. A significant portion of our time will be dedicated
to working with the [ForML](http://forml.io) framework, where we will implement a practical
end-to-end ML solution that demonstrates all of these principles we've discussed.


Slides
------
* The introduction slides are available on [google slides](https://tinyurl.com/5t34erst)
* The workshop slides are available at [formlio.github.io/mlprague23](https://formlio.github.io/mlprague23/).

Article
--------------
An accompanying article in more depth on the lifecycle patterns can be found on [medium](https://towardsdatascience.com/understanding-ml-product-lifecycle-patterns-a39c18302452)


Setup
-----

1. Clone the [workshop repository](https://github.com/formlio/mlprague23):
```shell
$ git clone git@github.com:formlio/mlprague23.git
$ cd mlprague23
```
2. [Install Docker Engine](https://docs.docker.com/engine/install/) along with the
[Docker Compose plugin](https://docs.docker.com/compose/install/) (should be already part of any
recent docker engine version).
3. Spin up the workspace container from within the `mlprague23` project root directory (this will
need to bind ports `8888`, `8000` and `4040` on your machine):
```shell
$ docker compose up -d
```
4. Load the workspace notebook interface at [http://127.0.0.1:8888/lab](http://127.0.0.1:8888/lab)
using your browser.
