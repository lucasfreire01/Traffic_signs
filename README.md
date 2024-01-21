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
where the X variable is the features, and the Y Variables are the labels. Bellow there is a example of a colorful picture.
![colorful_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download.png)<br>
Changing these pictures to colorful for gray help us with some things, these images are transformed into gray pictures because the colorful images are 3 buses (R, G, B) for example (187, 222, 87) when we get a gray image in RGB will be for example(187, 187, 187) we have gray in the RGB base when all values are the same the color is gray this enables us to use 1 buses because the number is the same that is the 3 buses(R G B), bellow is an example in the gray. After we norm these values based on the white number in RGB (255). The images below are the first picture in gray next the image in colorful and next the gray norm.<br>
![gray_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download1%20(2).png)<br>
![colorful_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download2%20(2).png)<br>
![gray_norm_picture](https://github.com/lucasfreire01/Traffic_signs/blob/main/download3%20(2).png)<br>
