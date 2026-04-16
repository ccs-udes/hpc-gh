Running jobs
============

.. note::

   This page covers the specifics of the GH Cluster. If you are not familiar
   with job submission and management commands (such as ``sbatch``, ``salloc``,
   ``squeue``), read `Running jobs
   <https://docs.alliancecan.ca/wiki/Running_jobs/fr>`_ from the Alliance
   technical documentation first.

Login nodes
-----------

Use the login node (``iv01``) to prepare your jobs. Cluster login nodes do not
have a GPU or the computing power to run jobs. All jobs must be submitted to the
scheduler using the appropriate commands: ``sbatch``, ``salloc``, ``srun``.

Using your group’s nodes
------------------------

Use ``--partition=gh-alice`` in your job script or on the command line to
specify your research group’s scheduler partition, which you can identify from
the :doc:`node table <nodes>`.

Shared access
-------------

Institut quantique researchers
''''''''''''''''''''''''''''''

All contributed nodes are shared via the ``gh-preempt`` partition. If you are
an IQ researcher with access to the GH Cluster, you can use the partition.
However, submitted jobs are automatically cancelled if the owner of a node where
they are running needs it for his own jobs. The owner thus has a “preemption
right”.

Cancelled jobs receive a ``SIGTERM`` signal and have one minute to save their
partial results. A job thus cancelled may request to be requeued with the
``--requeue`` option.

The ``gh-preempt`` partition is useful for batches of short jobs and for jobs
that use software able to write checkpoints to resume an interrupted
calculation.

To use both the shared nodes and one or more contributed nodes, use e.g.
``--partition=gh-alice,gh-preempt``. To exclude a specific node, such as
your own to reserve it for other jobs, add e.g. ``--exclude=gh1399``.

Bioinformatics service staff
'''''''''''''''''''''''''''''

Staff members of the Bioinformatics service also have access to all contributed
nodes, but with a lower priority, via ``gh-preempt-low``. That partition behaves
like ``gh-preempt``, described in the previous section, with one important
difference: jobs are automatically canceled if **any** IQ researcher needs the
allocated resources for their own jobs.

Available resources
-------------------

Use ``susage`` to show allocated or available resources in one or more
partitions. Used with no option or argument, it shows the allocated resources in
the partitions you have access to.

Job management
--------------

Use ``squeue`` to list all jobs currently in the scheduler, or ``sq`` to list
only your own. Use ``sacct`` or ``seff`` to get information about completed
jobs. Use ``srun --jobid=1234 --overlap --pty $SHELL`` to connect to a running
job to monitor it.
