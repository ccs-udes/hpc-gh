Stockage
========

Répertoire personnel
--------------------

Votre répertoire personnel est accessible à ``$HOME``. Par exemple :

.. code-block:: console

    [alice@iv01 ~]$ echo $HOME
    /home/alice

C’est le bon emplacement pour vos fichiers de configuration, votre code et les
logiciels que vous installez. Dû à sa capacité et à sa performance limitées, ce
n’est pas le bon emplacement pour vos données de recherche et vous ne devriez
pas l’utiliser pour lire et écrire de telles données lorsque vous :doc:`exécutez
des tâches <jobs>`.

Données de recherche
--------------------

Le système de fichiers réseau de l’Institut quantique est disponible à
``/net/nfs-iq``.

Le système de fichiers réseau du Service de bio-informatique est disponible à
``/net/nfs-bio``.
