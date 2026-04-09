Storage
=======

Home directory
--------------

Your home directory is accessible at ``$HOME``. For instance:

.. code-block:: console

    [alice@iv01 ~]$ echo $HOME
    /home/alice

This is the right location for configuration files, your code, and software that
you install. Due to limited capacity and performance, it is not the right
location for research data and you should not use it to read and write such data
when :doc:`running jobs <jobs>`.

Research data
-------------

The Institut quantique network filesystem is available at ``/net/nfs-iq``.

The Bioinformatics service network filesystem is available at ``/net/nfs-bio``.
