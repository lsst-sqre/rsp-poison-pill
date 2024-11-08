# Poison pill for lsst-rsp

This demonstrates a user-installed package that will keep the RSP from
starting in a single-python RSP Lab container.  However, the same user
installed package will *not* prevent a two-python container (as
described in [sqr-088](https://sqr-088.lsst.io)).

## Installation

First, please don't, except in the very limited case where you mean to
demonstrate the behavior described above.

If you are doing that, `pip install
git+https://github.com/lsst-sqre/rsp-poison-pill` ; then you will have
to shut down your running Lab instance.

If you then start a one-python container, it will fail to start up.

If you start a two-python container, it will run.

## Maintenance and development and stuff

Just don't, please?  This is not a module intended for long-term
maintenance.
