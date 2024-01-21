# MARKER_START_PRE_PROCESS
# ... Pre-processing code ...
def open_file(file_load):
  zip = zipfile.ZipFile(file=file_load, mode='r')
  zip.extractall('./')
  zip.close
train = open_file('/content/drive/MyDrive/train.pickle.zip')
test = open_file('/content/drive/MyDrive/test.pickle.zip')
valid = open_file('/content/drive/MyDrive/valid.pickle.zip')
with open('/content/train.pickle', mode='rb') as training:
  train = pickle.load(training)
with open('/content/test.pickle', mode='rb') as test:
  test = pickle.load(test)
with open('/content/valid.pickle', mode='rb') as valid:
  valid = pickle.load(valid)
train
x_train, y_train = train['features'], train['labels']
x_test, y_test = test['features'], test['labels']
x_valid, y_valid = valid['features'], valid['labels']
x_train.shape
y_train.shape
x_test.shape
x_valid.shape
import random
i = random.randint(1000, 34799)
plt.imshow(x_train[i])
y_train[i]
from sklearn.utils import shuffle
x_train, y_train = shuffle(x_train, y_train)
x_train_gray = np.sum(x_train / 3, axis=3, keepdims=True)
x_test_gray = np.sum(x_test / 3, axis=3, keepdims=True)
x_valid_gray = np.sum(x_valid / 3, axis=3, keepdims=True)
x_train_gray.shape
x_train_gray_norm = (x_train_gray - 255) / 255
x_test_gray_norm = (x_test_gray - 255) / 255
x_valid_gray_norm = (x_valid_gray - 255) / 255
np.max(x_train_gray_norm)
i = random.randint(0, 34799)
plt.imshow(x_train_gray[i].squeeze(), cmap='gray')
plt.figure()
plt.imshow(x_train[i])
plt.figure()
plt.imshow(x_train_gray_norm[i].squeeze(), cmap='gray')
i = random.randint(0, 12630)
plt.imshow(x_test_gray[i].squeeze(), cmap='gray')
plt.figure()
plt.imshow(x_test[i])
plt.figure()
plt.imshow(x_test_gray_norm[i].squeeze(), cmap='gray')
i = random.randint(0, 4410)
plt.imshow(x_valid_gray[i].squeeze(), cmap='gray')
plt.figure()
plt.imshow(x_valid[i])
plt.figure()
plt.imshow(x_valid_gray_norm[i].squeeze(), cmap='gray')
# MARKER_END_PRE_PROCESS