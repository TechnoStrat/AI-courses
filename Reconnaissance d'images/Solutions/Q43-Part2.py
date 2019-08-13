
# On crée une image décalée de 'offset' pixels
offset = 4
hack_img = np.expand_dims(np.roll(img, offset),0)
hack_pred, hack_confidence = predict(hack_img, cnn, norm)

# On affiche le résultat
f, axis = plt.subplots(1,2, figsize=(6,5))

print_img(image = img, \
          title = "Image de base\nPrédiction : " + str(prediction[idx]) \
                  + "\nConfiance : " + str(np.round(confidence[idx]*100,1)) + '%', \
          ax = axis[0])

print_img(image = hack_img.reshape(28,28), \
          title = "Image décalée\nPrédiction : " + str(hack_pred[0]) \
                  + "\nConfiance : " + str(np.round(hack_confidence[0]*100,1)) + '%', \
          ax = axis[1])

axis[0].set_axis_off()
axis[1].set_axis_off()
plt.show()