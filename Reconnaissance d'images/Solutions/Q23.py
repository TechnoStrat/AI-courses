
# Encodage des labels pour être conforme aux données de sortie du réseau de neurones
vec_lbl_train = to_categorical(lbl_train)
vec_lbl_test = to_categorical(lbl_test)

# on vérifie le résultat
print("Le label d'entraînement {} a été encodé en {}".format(lbl_train[0], vec_lbl_train[0]))
print("Le label de test {} a été encodé en {}".format(lbl_test[0], vec_lbl_test[0]))