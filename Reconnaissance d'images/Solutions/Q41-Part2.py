
# On visualise les prédictions erronées vs prédictions attendues
plt.yticks(range(0,10))
plt.xticks(range(0,10))
plt.ylabel("Chiffre réel")
plt.xlabel("Chiffre prédit")
plt.title("Chiffre réel vs chiffre prédit sur les prédictions erronées")
plt.imshow(err_confusion, cmap = 'Reds')
plt.show()