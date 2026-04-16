Foire aux questions (FAQ)
=========================

Pourquoi les GH sont-ils gérés séparément ?
-------------------------------------------

Les serveurs Grace Hopper ont des CPU ARM (architecture ``aarch64``) qui
diffèrent des CPU Intel ou AMD plus communs (architecture ``x86_64``). Si nous
ajoutions les GH à une grappe Intel/AMD, vous feriez face à des incompatibilités
logicielles. Pour les éviter, vous devriez séparer soigneusement les logiciels
pour les deux architectures.

Avoir une grappe séparée avec un nœud de connexion et des répertoires personnels
dédiés évite ce problème.
