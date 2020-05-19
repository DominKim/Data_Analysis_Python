'''
step05_dot_example.py

시경망에서 행렬곱 적용 예

 - 은닉층(h) = [입력(X) * 가중치(w)] + 편향(b)
'''

import numpy as np

# 1.ANN model
# input : image(28 x 28). hidden node : 32개 -> weight[28, 32]

# 2. input data : image data
28 * 28 # 784
x_image = np.random.randint(0, 256, size = 784) # 0 ~ 255
x_image.shape # (784,)
x_image.max() # 0 ~ 255

# 이미지 정규화 : 0 ~ 1
x_image = x_image / 255
x_image.max() # 1.0
x_img2d = x_image.reshape(28, 28)
x_img2d.shape  # (28, 28)

# 3. weight data
weight = np.random.randn(28, 32)
weight
weight.shape # (28, 32)

# 4. hidden layer
hidden = np.dot(x_img2d, weight)
hidden.shape # h(28, 32) = x(28, 28) * w(28, 32)
