
Early and late blights are destructive potato and tomato diseases caused by different pathogens: early blight is caused by the fungus Alternaria solani and occurs in warmer, humid conditions, creating target-like spots on older leaves.
Late blight, caused by the oomycete Phytophthora infestans, thrives in cool, wet weather and causes water-soaked lesions, wilting, and potential tuber rot.  

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

