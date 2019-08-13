
# Idée 1 : afficher la distribution des chiffres réprésentés sur les images
plt.figure(figsize = (10,5))
plt.hist(x = [lbl_train, lbl_test],
         bins = np.arange(0,11) - 0.5, ec='black',
         weights=[np.ones(n_train) / n_train, np.ones(n_test) / n_test],
         label = ["Entraînement", "Test"])

plt.xlabel("Chiffres manuscrits")
plt.ylabel("Fréquence d'occurrence")
plt.xticks(range(0,10))
plt.title("Distribution des échantillons")
plt.legend(loc='upper right')
plt.show()