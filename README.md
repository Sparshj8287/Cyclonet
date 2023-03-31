# CycloNet

## Cyclone Intensity Estimation using Deep Learning

A App User Interface where the user can upload INSAT-3D IR Satellite Image of Cyclone which is then passed to our Deep Convolutional Neural Network built in Tensorflow which is trained on Cyclone imagery of various intensities on dataset curated from Raw INSAT-3D satellite captured images on MOSDAC server. 

The CNN eliminates the need for usage of traditional methods for accurate center determination to estimate the Cyclone intensity using Satellite imagery. 

The Model will return the estimated Intensity of satellite cyclone image in KNOTS instantly.

The Streamlit app is hosted on hugging face.
``App Link:``[Link](https://huggingface.co/spaces/Sj8287/Cyclonet) 

## Dataset

[Curated Dataset link](https://www.kaggle.com/datasets/sshubam/insat3d-infrared-raw-cyclone-images-20132021)

## Tech Stack Used

Tools : Tensorflow-keras,python,Streamlit,Hugging face


## Screenshots and reference Images

``Introduction to App:`` landing section of the App

![Hero]([https://user-images.githubusercontent.com/101162842/163724950-78dbfb1e-c414-4d2d-8a12-b7d4b2d4bdc6.jpg](https://github.com/Sparshj8287/Cyclonet/blob/master/Screenshots/Screenshot%202023-04-01%20at%2012.52.17%20AM.png))


``Form section:`` used to pass the image to the model which computes intensity and forwards input data to the archive via database

![Form](https://user-images.githubusercontent.com/101162842/163724953-f8479e57-267e-4560-8a1c-9761afe49f35.jpg)


``Live Weather Map:`` made using Windy API, showing live wind patterns and redirects the map to the coordinates recieved as input, incase of a cyclone, highlights the area with strong wind pattern

![Windy map](https://user-images.githubusercontent.com/101162842/163724954-7d91ff9a-be77-436a-967c-a067c485af4f.jpg)


``Archive Table:`` displaying all previously uploaded data stored in database

![Archive Table](https://user-images.githubusercontent.com/101162842/163724961-db84f65f-4d13-49dc-8d97-d30726918a14.jpg)


``Submitted Image:`` Would be displayed as

![Image image](https://user-images.githubusercontent.com/101162842/163724965-9bdb6f09-1d3f-4d4b-be08-dfd7bfdcde03.jpg)
