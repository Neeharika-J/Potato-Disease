import tensorflow as tf
loaded_model = tf.keras.models.load_model("E:/pythonProjectPotato_Disease_Detection/saved_models/1/trained_model.keras")
loaded_model.export("E:/pythonProjectPotato_Disease_Detection/saved_models/2")
