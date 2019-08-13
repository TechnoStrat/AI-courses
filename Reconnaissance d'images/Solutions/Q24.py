
# Interprétation de la sortie du réseau de neurones : on retient la position de la probabilité maximale
nn_output = np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.91, 0.01, 0.01, 0.01, 0.01])
pred = nn_output.argmax()
confidence = nn_output.max()

print("Pour la sortie du réseau de neurones {}, \
       \nle chiffre {} sera retenu avec une confiance de {:.1%}".format(nn_output, pred, confidence))