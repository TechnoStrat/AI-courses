
# On calcule le nombre d'erreurs par classe (chiffre manuscrit)
plt.bar(range(0,10),err_confusion.sum(axis=1) / confusion.sum(axis=1))
plt.xticks(range(0,10))
plt.title("Fréquence d'erreurs par chiffre")
plt.ylabel("Fréquence d'erreurs")
plt.xlabel("Chiffre manuscrit")
plt.show()