
datagen = ImageDataGenerator(rotation_range = 25, width_shift_range = 0.2, height_shift_range=0.2, zoom_range=0.2)
iterator = datagen.flow(x = np.expand_dims(img, 0), batch_size = 1)

f, axis = plt.subplots(10,10, figsize=(18,20))
for i,ax in zip(range(0,100), axis.flatten()):
    print_img(image = iterator.next().reshape(28,28), \
              title = "Label : " + str(lbl_test[idx]), \
              ax = ax)
    ax.set_axis_off()
plt.show()