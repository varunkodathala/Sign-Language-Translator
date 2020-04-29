# Sign-Language-Translator


# Sign Language refers to 


![Image 1](https://github.com/varunkodathala/Sign-Language-Translator/blob/master/demo/1.jpg?raw=true)
![Image 2](https://github.com/varunkodathala/Sign-Language-Translator/blob/master/demo/2.jpg?raw=true)

# Model:

1. Image Access through webcam using opencv
2. Predict the Image using trained CNN model.  [Model](https://github.com/varunkodathala/Sign-Language-Translator/blob/master/demo/gesture_model.h5)
3. Process the prediction and display back using opencv


# Architecture:

![Model Summary](https://github.com/varunkodathala/Sign-Language-Translator/blob/master/demo/model_summary.png?raw=true)

# Dataset:

[Kaggle ASL Dataset](https://www.kaggle.com/grassknoted/asl-alphabet)

# Class Id's:

```ruby
class_labels = ['A','B','C','D','E','F','G','H','I','J','K','L',
               'M','N','O','P','Q','R','S','T','U','V','W','X',
               'Y','Z','del','nothing','space']
```
# Model Analysis:

- Total Epochs: 60

Plots:
- Accuracy Plot

- Loss Plot
