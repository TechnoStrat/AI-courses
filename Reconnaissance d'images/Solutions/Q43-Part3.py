
# Comme on le voit avec LIME, l'algorithme semble accorder beaucoup d'importance à certaines régions vides
# On crée donc une image avec un rectangle blanc sur les 5 premières lignes
hack_img = np.array(img)
hack_img[:,4:7,:] = 255
hack_img[:,-7:-4:,:] = 255

hack_img = np.expand_dims(hack_img, 0)
hack_pred, hack_confidence = predict(hack_img, cnn, norm)

# On affiche le résultat
f, axis = plt.subplots(1,2, figsize=(6,5))

print_img(image = img,
          title = "Image de base\nPrédiction : {}\nConfiance : {:.2%}".format(prediction[idx], confidence[idx]),
          ax = axis[0])

print_img(image = hack_img.reshape(28,28),
          title = "Image hackée\nPrédiction : {}\nConfiance : {:.2%}".format(hack_pred[0], hack_confidence[0]),
          ax = axis[1])

axis[0].set_axis_off()
axis[1].set_axis_off()
plt.show()