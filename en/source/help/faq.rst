Frequently asked questions
==========================

Why are the GH managed separately?
----------------------------------

Grace Hopper servers have ARM CPUs (``aarch64`` architecture) that do not fit
with servers that have the more common Intel or AMD CPUs (``x86_64``
architecture). If we added the GH nodes to an Intel/AMD cluster, you would
encounter software incompatibilities. To work around these, you would need to
carefully separate software for the two architectures.

Having a separate cluster with a dedicated login node and home directories
avoids this issue.
