
# création de la distribution de confiance
err_confidence = [confidence[i] for i in err_idx]
corr_confidence = [confidence[i] for i in corr_idx]
distr_err_confidence = np.histogram(err_confidence, [i/100 for i in range(0,101)])
distr_corr_confidence = np.histogram(corr_confidence, [i/100 for i in range(0,101)])
percent_distr_err_confidence = (distr_err_confidence[0] / (distr_corr_confidence[0] + distr_err_confidence[0]))*100
percent_distr_corr_confidence = (distr_corr_confidence[0] / (distr_corr_confidence[0] + distr_err_confidence[0]))*100
percent_distr_err_confidence[np.isnan(percent_distr_err_confidence)] = 0
percent_distr_corr_confidence[np.isnan(percent_distr_corr_confidence)] = 0

# Visualisation
plt.figure(figsize = (20,8))
plt.bar(distr_corr_confidence[1][:-1] + 0.0075, percent_distr_err_confidence, width=0.008, label = "erreur", \
        color = 'red')
plt.bar(distr_corr_confidence[1][:-1] + 0.0075, percent_distr_corr_confidence, width=0.008, label = "correct", \
        bottom=percent_distr_err_confidence, color = 'green')
plt.xlabel("Taux de confiance")
plt.ylabel("%age correct / erreur")
plt.xticks([i / 20 for i in range(0,21)])
plt.xlim(0.5,1)
plt.title("Vue des prédictions correctes / erronées par taux de confiance")
plt.legend(loc='upper right')
plt.show()