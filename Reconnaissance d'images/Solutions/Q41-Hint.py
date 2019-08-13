
# On construit la matrice de confusion de l'algorithme
# La matrice de confusion contient en ligne les chiffres réels
# et en colonne les chiffres prédits

confusion = confusion_matrix(lbl_test, prediction) # matrice de confusion

err_confusion = confusion_matrix(lbl_test, prediction) # prédictions erronées seulement (tout sauf diagonale)
np.fill_diagonal(err_confusion, 0)

corr_confusion = np.diag(confusion_matrix(lbl_test, prediction)) # prédictions correctes seulement (diagonale)

confusion