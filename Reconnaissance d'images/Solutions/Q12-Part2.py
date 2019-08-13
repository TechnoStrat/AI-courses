
# Idée 2 : afficher l'image moyenne des échantillons d'entraînement et de test
# chaque pixel de cette image représente la moyenne des mêmes pixels de chaque image de l'échantillon
avg_img_train = img_train.sum(axis=0)/n_train
avg_img_test = img_test.sum(axis=0)/n_test

# on affiche chacune des images moyennes ainsi calculées
f, axis = plt.subplots(1,2, figsize=(10,5))
print_img(image = avg_img_train,
          title = "Image moyenne\n(échantillon d'entraînement)",
          ax = axis[0])
print_img(image = avg_img_test,
          title = "Image moyenne\n(échantillon de test)",
          ax = axis[1])
plt.show()