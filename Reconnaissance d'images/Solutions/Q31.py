
# Fonction permettant de faire la convolution entre une image et un filtre (kernel) avec éventuellement maxpooling
def conv(image, kernel, maxpooling = False, strides = 2):
    def my_filter(shape):
        return np.expand_dims(np.expand_dims(kernel,-1),-1)
    
    apply_conv = Sequential() # Initialisation
    
    apply_conv.add(Conv2D(kernel_size=(2,2), # Convolution de l'image par 'kernel'
                     filters=1,
                     kernel_initializer= my_filter,
                     input_shape=(None, None, 1)))
    
    if maxpooling:
        apply_conv.add(MaxPooling2D(pool_size = (2,2), strides = strides)) # Maxpooling 2x2 avec un pas de 1
        
    return apply_conv.predict(np.expand_dims(image,0))[0,:,:,0]

print("Après convolution : ")
print(conv(image, kernel, maxpooling=False, strides=1))
print()
print("Après convolution et MaxPooling : ")
print(conv(image, kernel, maxpooling=True, strides=1))