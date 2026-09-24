Lancer des tâches
=================

.. note::

   Cette page couvre les spécificités de la Grappe GH. Si vous n’êtes pas
   familier avec les commandes pour lancer et gérer des tâches (telles que
   ``sbatch``, ``salloc``, ``squeue``), lisez d’abord `Exécuter des tâches
   <https://docs.alliancecan.ca/wiki/Running_jobs/fr>`_ dans la documentation de
   l’Alliance.

Login nodes
-----------

Utilisez le nœud de connexion (``iv01``) pour préparer vos tâches de calcul. Les
nœuds de connexion des grappes n’ont pas de GPU ou la puissance de calcul pour
exécuter des tâches. Toutes les tâches doivent être soumises à l’ordonnanceur
avec les commandes appropriées : ``sbatch``, ``salloc``, ``srun``.

Utiliser les nœuds de votre groupe
----------------------------------

Utilisez ``--partition=gh-alice`` dans votre script de tâche ou avec la ligne de
commande pour spécifier la partition de l’ordonnanceur pour votre groupe de
recherche. Identifiez cette partition à l’aide de la :doc:`table des
nœuds <nodes>`.

Accès partagé
-------------

Chercheurs de l’Institut quantique
''''''''''''''''''''''''''''''''''

Tous les nœuds contribués sont partagés via la partition ``gh-preempt``. Si vous
êtes un chercheur de l’IQ et que vous avez accès à la Grappe GH, vous pouvez
utiliser cette partition. Toutefois, les tâches en cours sont automatiquement
annulées si le propriétaire d’un nœud où elles s’exécutent en a besoin pour ses
propres tâches. Le propriétaire dispose ainsi d’un « droit de préemption ».

Les tâches annulées reçoivent un signal ``SIGTERM`` et disposent d’une minute de
grâce pour sauvegarder leurs résultats partiels. Une tâche ainsi annulée peut
demander à être remise dans la file d’attente avec l’option ``--requeue``.

La partition ``gh-preempt`` est utile pour les lots de courtes tâches et pour
les tâches qui utilisent des logiciels capables d’écrire des points de contrôle
afin de reprendre un calcul interrompu.

Pour utiliser à la fois les nœuds partagés et un ou plusieurs nœuds contribués,
utilisez e.g. ``--partition=gh-alice,gh-preempt``. Pour exclure un nœud
particulier, tel que le vôtre pour le réserver à d’autres tâches, ajoutez e.g.
``--exclude=gh1399``.

Personnel du Service de bio-informatique
''''''''''''''''''''''''''''''''''''''''

Les membres du personnel du Service de bio-informatique ont aussi accès à tous
les nœuds contribués, mais avec une priorité réduite, via ``gh-preempt-low``.
Cette partition se comporte comme ``gh-preempt``, décrite à la section
précédente, avec une différence importante : les tâches sont automatiquement
annulées si **n’importe quel** chercheur de l’IQ a besoin des ressources
allouées pour ses propres tâches.

Ressources disponibles
----------------------

Utilisez ``susage`` pour afficher les ressources allouées ou disponibles dans
une ou plusieurs partitions. Utilisée sans option ni argument, la commande
affiche les ressources allouées dans les partitions auxquelles vous avez accès.

Gestion des tâches
------------------

Utilisez ``squeue`` pour afficher toutes les tâches présentement dans
l’ordonnanceur ou ``sq`` pour n’afficher que les vôtres. Utilisez ``sacct`` ou
``seff`` pour obtenir de l’information sur les tâches complétées. Utilisez
``srun --jobid=1234 --overlap --pty $SHELL`` pour vous connecter à une tâche en
cours pour l’examiner.
