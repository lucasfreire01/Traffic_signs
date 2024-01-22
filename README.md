# Traffic_signs
Hello guys, I'm here to show my new project Traffic_signs where we have a convolutional neural network (CNN). Each image in the dataset has more than 1200 pixels but by providing 400 pixel
the model forecasts the traffic signs, and the pixels provided are processing their model.
## Pre_process
We have 3 datasets(train, test, valid) in pickle all database is constituted with values like:
{'coords': array([[  6,   5,  21,  20],<br>
        [  6,   6,  22,  22],<br>
        [  5,   6,  22,  23],<br>
        ...,<br>
        [ 17,  15, 178, 155],<br>
        [ 17,  15, 183, 160],<br>
        [ 20,  18, 211, 184]], dtype=uint8),<br>
 'labels': array([41, 41, 41, ..., 25, 25, 25], dtype=uint8),<br>
 'features': array([[[[ 28,  25,  24],<br>
          [ 27,  24,  23],<br>
          [ 27,  24,  22],<br>
          ...,<br>
          [ 32,  28,  24],<br>
          [ 31,  27,  25],<br>
          [ 31,  27,  26]],<br>
 <br>
         [[ 29,  26,  25],<br>
          [ 27,  25,  23],<br>
          [ 27,  25,  23],<br>
          ...,<br>
          [ 32,  28,  24],<br>
          [ 31,  27,  24],<br>
          [ 30,  27,  25]],<br>
 <br>
         [[ 28,  26,  26],<br>
          [ 27,  25,  23],<br>
          [ 26,  25,  23],<br>
          ...,<br>
          [ 32,  28,  24],<br>
          [ 31,  27,  24],<br>
          [ 30,  27,  25]],<br>
take attention in the features this mind the pixels in images all databases have these column features. Next split these database in x_train, x_test, x_valid, y_train, y_test, y_valid 
where the X variable is the features, and the Y Variables are the labels. Bellow there is a example of a colorful picture.<br>
![colorful_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download.png)<br>
Changing these pictures to colorful for gray help us with some things, these images are transformed into gray pictures because the colorful images are 3 buses (R, G, B) for example (187, 222, 87) when we get a gray image in RGB will be for example(187, 187, 187) we have gray in the RGB base when all values are the same the color is gray this enables us to use 1 buses because the number is the same that is the 3 buses(R G B), bellow is an example in the gray. After we norm these values based on the white number in RGB (255). The images below are the first picture in gray next the image in colorful and next the gray norm.<br>
![gray_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download1%20(2).png)<br>
![colorful_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download2%20(2).png)<br>
![gray_norm_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download3%20(2).png)<br>
## Model
This model is used based on the LeNet architecture. Here is a soon description of the LeNet.<br>

LeNet is a classic convolutional neural network (CNN) architecture developed in 1998 by Yann LeCun and others. It was designed for handwritten character recognition tasks, with a focus on simplicity and effectiveness. The architecture includes convolutional layers, average pooling, and fully connected layers, showcasing the principles that have influenced many subsequent CNN designs. LeNet played a key role in establishing the viability of deep learning for image recognition.<br>
![gray_norm_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/Capturar.PNG)<br>
This is the architecture. Bellow there is the summary of the model with the sequential layers in the conv2d because these pictures are 2d using a pooling(avarege_pooling) that 
we reduce the dimension taking a square and result in a new square with the mean for the output after the processing of images is use the Dense(layer) 
| Layer (type)             | Output Shape       | Param # |
| ------------------------ | ------------------ | ------- |
| conv2d                   | (None, 28, 28, 6)  | 156     |
| average_pooling2d        | (None, 14, 14, 6)  | 0       |
| conv2d_1                 | (None, 10, 10, 16) | 2416    |
| average_pooling2d_1      | (None, 5, 5, 16)   | 0       |
| flatten                  | (None, 400)        | 0       |
| dense                    | (None, 120)        | 48120   |
| dense_1                  | (None, 84)         | 10164   |
| dense_2                  | (None, 43)         | 3655    |

===========================================================<br>
Total params: 64511 (252.00 KB)<br>
Trainable params: 64511 (252.00 KB)<br>
Non-trainable params: 0 (0.00 Byte)<br>
The model running 50 epochs with a batch = 500 and the accuracy in the test dataset get us 84,75%
![gray_norm_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download1%20(3).png)<br>
![gray_norm_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download2%20(3).png)<br>
Now we have the confusion matrics and a frame of result if the model is across with the real values.
![gray_norm_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download1%20(4).png)<br>
![gray_norm_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download2%20(4).png)<br>
This project did in the Practical Deep Learning with TensorFlow and Python at AI Expert academy. Link bellow:<br>
https://iaexpert.academy/?doing_wp_cron=1705932255.1060640811920166015625
