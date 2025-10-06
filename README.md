# 🌟 Introduction

  Potato diseases like early blight and late blight are serious threats to farmers and food security worldwide. A single outbreak can wipe out entire fields, leaving farmers with heavy losses and communities with reduced food supplies. Detecting these diseases early makes all the difference — it allows timely action to protect yields, improve crop quality, and reduce waste. By identifying problems before they spread, we can support farmers, safeguard harvests, and ensure a more sustainable food system.

## Features: 
1. CNN
2. Fast API
3. TF-Serving
4. Docker

<p align="center">
  <img src="https://thumbs.dreamstime.com/b/potato-leaf-attacked-alternaria-solani-specific-symptom-early-blight-alternaria-solanion-cultivated-potato-leaf-solanum-148379279.jpg" alt="Early Blight" width="25%"/>
  <img src="https://millerresearch.com/wp-content/uploads/2019/01/Halo-2-3-1080x675.jpg" alt="Late Blight" width="25%"/>
</p>

<p align="center">
  <b>Early Blight</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Late Blight</b>
</p>

## 🌱 Potato Diseases: Early Blight vs Late Blight

| Aspect                     | Early Blight (*Alternaria solani*)                                   | Late Blight (*Phytophthora infestans*)                       |
|-----------------------------|----------------------------------------------------------------------|-------------------------------------------------------------|
| **Favorable Conditions**   | - Warm, humid weather <br> - Usually affects older leaves first       | - Cool, wet weather <br> - Rapid spread under prolonged leaf wetness |
| **Symptoms**               | - Small, dark brown concentric spots (target-like) <br> - Yellowing around spots <br> - Lesions merge into large dead areas | - Water-soaked, dark green to black lesions <br> - White fungal growth on leaf undersides <br> - Stem lesions, wilting <br> - Tuber rot (brown, firm decay) |
| **Effects on Potato Growth** | - Reduced photosynthesis <br> - Premature leaf drop (defoliation) <br> - Smaller tubers, reduced yield | - Rapid foliage and stem destruction <br> - Infected tubers, poor storage quality <br> - Severe yield loss (can destroy entire fields) |


## 📊 Dataset
The dataset used in this project is from Kaggle called Plant Village. Here the link : [https://www.kaggle.com/datasets/arjuntejaswi/plant-village](https://www.kaggle.com/datasets/arjuntejaswi/plant-village). This dataset is a collection of images designed to aid in the identification of plant diseases. It includes labeled images of various plant species with corresponding disease categories, making it ideal for training machine learning models in plant disease classification tasks. I have focused specifically on the potato leaf images of this dataset.

## 🤖 Model 
I have used tensorflow in this project. 

### Working
**tf.keras.preprocessing.images_dataset_from_directory** : is used to convert images to *tf.data.Dataset* which can be directly fed to our model. The image size is fixed to 256x256 and the batch size is 32.
**batch processing** is faster than feeding the model one sample at a time. batch().take(n) takes first n batches and batch().skip(n) skips first n batches and selects the rest.
The images are then **resized, rescaled and augmented** to increase the quality of training. They are then passed through convolutional and max pooling layers to extract features and finally flattened and fed to dense layers for *model learning*. *Adam* optimizer is used. This model gives prediction and the confidence level of the prediction.
After training I got accuracy of 96% and loss of 0.076. On testing, I got accuracy of 94% and loss of 0.240 .

<img src="https://github.com/Neeharika-J/Potato-Disease/blob/main/images/Traning_testing_graph.png" alt="Graph" width="50%"/>

Then I have saved the model on my drive as a keras file(.keras)
```bash
import os
model_save_name = 'trained_model.keras'
folder_path = "/content/drive/My Drive/Potato_Disease_Data/"
os.makedirs(folder_path, exist_ok=True)
path = os.path.join(folder_path, model_save_name)

# Save model
model.save(path)
```

## ⚡Fast API
After creating the model, I created an end-point for predicting where the user could enter the image.
```bash
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image
```
This function converts user input (leaf image) into numpy array.
**BytesIO(data)** - Converts the raw bytes (data) into a file-like object in memory.This allows libraries like PIL to read the “file” without saving it to disk.

<br>**Image.open(BytesIO(data))** - Uses PIL (Python Imaging Library) to open the image from the in-memory bytes.Returns a PIL Image object.

<br>**np.array(Image.open(...))** - Converts the PIL Image into a NumPy array, e.g., shape (height, width, channels).Now the image can be used for machine learning, OpenCV, or TensorFlow processing.

Now to import the model in my fast api, I can use my saved model. However everytime, I need to predict I need to load my model which can be time consuming (this is being done in *main.py*). To make the model ever-ready, tf-serving is a server where we can host our model so that we can use it anytime (done in *main-tf.serving*) . To access it, we need to make image in docker. Then start a container with a command: 

```bash
# Docker Command
docker run -t --rm -p 8501:8501 -v E:/pythonProjectPotato_Disease_Detection:/potato-disease  tensorflow/serving --rest_api_port=8501 --model_config_file=/potato-disease/model_config_list
```
**docker run** - Tells Docker to run a container.<br>
**-t** - Allocates a pseudo-TTY (useful for logging output).<br>
**--rm** - Automatically removes the container when it stops.<br>
**-p 8501:8501** - Maps port 8501 on your host machine to 8501 in the container.This is the port used by TensorFlow Serving’s REST API.<br>
**-v E:/pythonProjectPotato_Disease_Detection:/potato-disease** - Mounts a local folder into the container. Host folder: E:/pythonProjectPotato_Disease_Detection. Container folder: /potato-disease. This allows TensorFlow Serving to access your model files.<br>

After successfully tf-serving the model, all I have to do is send a request to my FastAPI and the api will pass the image input to the model hosted on docker, the model then returns its prediction through the docker port to the api and back to me.

##### Thank you for reading this far ❤️ (that is if you really have). Will refine the project further.



