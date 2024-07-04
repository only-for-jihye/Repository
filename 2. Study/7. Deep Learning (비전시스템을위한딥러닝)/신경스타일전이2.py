# 다른 예제 찾아서 해봄
# 실행 안됌 에러 못잡겠음 ㅠ
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.applications import vgg19
from keras import backend as K
from IPython.display import Image, display
from keras.applications import inception_v3
from scipy.optimize import fmin_l_bfgs_b

# tf.gradients is not supported when eager execution is enabled. Use tf.GradientTape instead. 에러 발생으로 처리 (구글)
# https://ingu627.github.io/error/tfgradients/
tf.compat.v1.disable_eager_execution()

K.set_learning_phase(0)
model = inception_v3.InceptionV3(weights='imagenet', include_top=False)
layer_contributions = {
    'mixed2' : 0.4,
    'mixed3' : 2.,
    'mixed4' : 1.5,
    'mixed5' : 2.3,
}

layer_dict = dict([(layer.name, layer) for layer in model.layers])
loss = K.variable(0.)

for layer_name in layer_contributions :
    coeff = layer_contributions[layer_name]
    activation = layer_dict[layer_name].output
    scaling = K.prod(K.cast(K.shape(activation), 'float32'))
    
    loss = loss + coeff * K.sum(K.square(activation[:, 2: -2, 2: -2, :])) / scaling

dream = model.input
grads = K.gradients(loss, dream)[0]
grads = grads / K.maximum(K.mean(K.abs(grads)), 1e-7)
outputs = [loss, grads]
fetch_loss_and_grads = K.function([dream], outputs)

def eval_loss_and_grads(x) :
    outs = fetch_loss_and_grads([x])
    loss_value = outs[0]
    grad_values = outs[1]
    return loss_value, grad_values

def gradient_ascent(x, iterations, step, max_loss=None) :
    for i in range(iterations) :
        loss_value, grad_values = eval_loss_and_grads(x)
        if max_loss is not None and loss_value > max_loss :
            break
        print(i, ' 번째 반복의 손실 값 : ', loss_value)
        x += step * grad_values
    return x

# hyperparameters
step = 0.01
num_octave = 3
octave_scale = 1.4
iterations = 20
max_loss = 10.

### 여기까지 딥드림 구현


### 여기부터 퍼온 것
def preprocess_image(image_path):
    # Util function to open, resize and format pictures into appropriate tensors
    img = keras.preprocessing.image.load_img(
        image_path, target_size=(img_nrows, img_ncols)
    )
    img = keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = vgg19.preprocess_input(img)
    # return tf.convert_to_tensor(img) # 에러 발생으로 수정
    return img


def deprocess_image(x):
    # Util function to convert a tensor into a valid image
    x = x.reshape((img_nrows, img_ncols, 3))
    # Remove zero-center by mean pixel
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    # 'BGR'->'RGB'
    x = x[:, :, ::-1]
    x = np.clip(x, 0, 255).astype("uint8")
    return x


result_prefix = "js_generated"

# Weights of the different loss components
total_variation_weight = 1e-6
style_weight = 1e-6
content_weight = 2.5e-8

### 여기부터 keras 구현 코드
content_image_path = "C:/Users/funjo/Documents/ivystudy/funjongsoo/비전시스템을위한딥러닝/content.jpg"
style_image_path =   "C:/Users/funjo/Documents/ivystudy/funjongsoo/비전시스템을위한딥러닝/style.JPG"

# Dimensions of the generated picture.
width, height = keras.preprocessing.image.load_img(content_image_path).size
img_nrows = 400
img_ncols = int(width * img_nrows / height)


content_image = K.variable(preprocess_image(content_image_path))
style_image = K.variable(preprocess_image(style_image_path))
combined_image = K.placeholder((1, img_nrows, img_ncols, 3))

input_tensor = K.concatenate([content_image, style_image, combined_image], axis=0)

model = vgg19.VGG19(input_tensor = input_tensor, weights='imagenet', include_top=False)

output_dict = dict([(layer.name, layer.output) for layer in model.layers])
layer_features = output_dict['block5_conv2']

content_image_features = layer_features[0, :, :, :]
combined_features = layer_features[2, :, :, :]

def content_loss(content_image, combined_image) :
    return K.sum(K.square(combined_image - content_image))

content_loss = content_weight * content_loss(content_image_features, combined_features)

def gram_matrix(x) :
    features = K.batch_flatten(K.permute_dimensions(x, (2, 0, 1)))
    gram = K.dot(features, K.transpose(features))
    return gram

def style_loss(style, combined) :
    S = gram_matrix(style)
    C = gram_matrix(combined)
    channels = 3
    size = img_nrows * img_ncols
    return K.sum(K.square(S - C)) / (4.0 * (channels ** 2) * (size ** 2))

feature_layers = [
    'block1_conv1',
    'block2_conv1',
    'block3_conv1',
    'block4_conv1',
    'block5_conv1'
]

for layer_name in feature_layers :
    layer_features = output_dict[layer_name]
    style_reference_features = layer_features[1, :, :, :]
    combination_features = layer_features[2, :, :, :]
    
    sl = style_loss(style_reference_features, combination_features)
    # style_loss += (style_weight / len(feature_layers)) * sl
    #예외가 발생했습니다. TypeError
    #Expected float32, but got <function style_loss at 0x00000220DC2C48B0> of type 'function'.
    #During handling of the above exception, another exception occurred:
    # 코드 잘못되어 있어 수정함
    loss += (style_weight / len(feature_layers)) * sl

def total_variation_loss(x) :
    a = K.square(
        x[:, :img_nrows - 1, :img_ncols - 1, :] - x[:, 1:, :img_ncols - 1, :]
    )
    b = K.square(
        x[:, :img_nrows - 1, :img_ncols - 1, :] - x[:, :img_nrows - 1, 1:, :]
    )
    return K.sum(K.pow(a + b, 1.25))

# 구문 빠져있어 추가
loss += total_variation_weight * total_variation_loss(combined_image)

class Evaluator(object) :
    def __init__(self) :
        self.loss_value = None
        self.grads_values = None
    def loss(self, x) :
        assert self.loss_value is None
        loss_value, grad_value = eval_loss_and_grads(x)
        self.loss_value = loss_value
        self.grads_values = grad_value
        return self.loss_value
    def grads(self, x) :
        assert self.loss_value is None
        grad_values = np.copy(self.grads_values)
        self.loss_value = None
        self.grads_values = None
        return grad_values

evaluator = Evaluator()


Iterations = 20
x = preprocess_image(content_image_path)
x = x.flatten()
for i in range(Iterations) :
    # x, min_val, info = fmin_l_bfgs_b(evaluator.loss, x.flatten(), fprime=evaluator.grads, maxfun=20) # x.flatten() Error 발생으로 수정
    x, min_val, info = fmin_l_bfgs_b(evaluator.loss, x, fprime=evaluator.grads, maxfun=20) # x.flatten() Error 발생으로 수정
    # img = deprocess_image(x.copy())
    img = deprocess_image(img)
    fname = result_prefix + '_at_iteration_%d.png' % i
    keras.preprocessing.image.save_img(fname, img)