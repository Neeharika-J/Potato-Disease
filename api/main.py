from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

app = FastAPI()

endpoint="http://localhost:8501/v1/models/potatoes_model:predict"
# MODEL= keras.models.load_model("../saved_models/1")
loaded_model = tf.keras.models.load_model("E:\\pythonProjectPotato_Disease_Detection\\saved_models\\1\\trained_model.keras")
CLASS_NAMES=["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data)->np.ndarray:
    image= np.array(Image.open(BytesIO(data)))
    return image


@app.get("/ping")
async def ping():
    return "server running"

@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image,0)
    prediction = loaded_model.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    return {
        'class':predicted_class,
        'confidence':float(confidence)
    }

if __name__=="__main__":
    uvicorn.run(app, host='localhost', port=4000)

