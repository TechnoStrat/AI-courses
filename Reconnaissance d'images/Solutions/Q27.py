
# On élimine aléatoirement des neurones / données
dropout_size_first_layer = 0.2 # %age d'élimination des informations de la première couche
dropout_size_last_layer = 0.1 # %age d'élimination des informations de la dernière couche

# Création du nouveau réseau de neurones artifiels
ann_dropout = Sequential() # initialisation
ann_dropout.add(Dropout(dropout_size_first_layer, input_shape=input_shape)) # élimination
ann_dropout.add(Flatten())
ann_dropout.add(Dense(hidden_layer_size))
ann_dropout.add(Activation(activation_function))
ann_dropout.add(Dropout(dropout_size_last_layer)) # élimination
ann_dropout.add(Dense(last_layer_size))
ann_dropout.add(Activation('softmax')) 
ann_dropout.compile(optimizer=optimizer(lr=learning_rate),
                    loss=loss_function,
                    metrics=['accuracy'])  

history = ann_dropout.fit(norm_img_train, vec_lbl_train, epochs=nb_epochs, batch_size=batch_size,
                          validation_data=(norm_img_test, vec_lbl_test), verbose=2)

# On trace l'historique des précisions après chaque epoch
plot_accuracy(history)