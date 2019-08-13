
# Affichage du %age automatisé vs taux d'erreur
seuil = 0.99

percent_automated = len(np.where(np.array(confidence) >= seuil)[0])/n_test
nb_error_seuil = distr_err_confidence[0][int((seuil)*100):].sum()
nb_correct_seuil = distr_corr_confidence[0][int((seuil)*100):].sum()
error_rate = nb_error / (nb_error + nb_correct)

print("En demandant à un humain de traiter manuellement les cas où l'IA est confiante à moins de {:.1%}, \
      \non automatisera {:.1%} des cas avec un taux d'erreur de l'IA de {:.3%}." \
.format(seuil, percent_automated, error_rate))