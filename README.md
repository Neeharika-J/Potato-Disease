# 🌟 Introduction

  Potato diseases like early blight and late blight are serious threats to farmers and food security worldwide. A single outbreak can wipe out entire fields, leaving farmers with heavy losses and communities with reduced food supplies. Detecting these diseases early makes all the difference — it allows timely action to protect yields, improve crop quality, and reduce waste. By identifying problems before they spread, we can support farmers, safeguard harvests, and ensure a more sustainable food system.

<p align="center">
  <img src="https://thumbs.dreamstime.com/b/potato-leaf-attacked-alternaria-solani-specific-symptom-early-blight-alternaria-solanion-cultivated-potato-leaf-solanum-148379279.jpg" alt="Early Blight" width="25%"/>
  <img src="https://millerresearch.com/wp-content/uploads/2019/01/Halo-2-3-1080x675.jpg" alt="Late Blight" width="25%"/>
</p>

<p align="center">
  <b>Early Blight</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Late Blight</b>
</p>

# 🌱 Potato Diseases: Early Blight vs Late Blight

| Aspect                     | Early Blight (*Alternaria solani*)                                   | Late Blight (*Phytophthora infestans*)                       |
|-----------------------------|----------------------------------------------------------------------|-------------------------------------------------------------|
| **Favorable Conditions**   | - Warm, humid weather <br> - Usually affects older leaves first       | - Cool, wet weather <br> - Rapid spread under prolonged leaf wetness |
| **Symptoms**               | - Small, dark brown concentric spots (target-like) <br> - Yellowing around spots <br> - Lesions merge into large dead areas | - Water-soaked, dark green to black lesions <br> - White fungal growth on leaf undersides <br> - Stem lesions, wilting <br> - Tuber rot (brown, firm decay) |
| **Effects on Potato Growth** | - Reduced photosynthesis <br> - Premature leaf drop (defoliation) <br> - Smaller tubers, reduced yield | - Rapid foliage and stem destruction <br> - Infected tubers, poor storage quality <br> - Severe yield loss (can destroy entire fields) |


## 📊 Dataset
The dataset used in this project is from Kaggle called Plant Village. Here the link : [Link Text](https://www.kaggle.com/datasets/arjuntejaswi/plant-village). This dataset is a collection of images designed to aid in the identification of plant diseases. It includes labeled images of various plant species with corresponding disease categories, making it ideal for training machine learning models in plant disease classification tasks. I have focused specifically on the potato leaf images of this dataset.





The picture shared by the user is converted to shape (256,256,3) and then passed through convolutional layes (Conv2D + Max Pooling Layers) which extract features and then it is flattened and fed to the dense layers.
The model is trained on huge dataset consisting of early blight, late blight and healthy potato leaf plant images along with data augmentation. Then the model is hosted on Tensorflow Server (tf-serving) and can be used anytime
using docker container. Then this container is connected to my FastApi which takes in an image and gives prediction and the confidence level of the prediction.

## Features: 
1. CNN
2. Fast API
3. TF-Serving
4. Docker

```bash
# Docker Command
docker run -t --rm -p 8501:8501 -v E:/pythonProjectPotato_Disease_Detection:/potato-disease  tensorflow/serving --rest_api_port=8501 --model_config_file=/potato-disease/model_config_list

