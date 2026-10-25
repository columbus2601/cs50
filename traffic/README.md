# Traffic Sign Recognition (CS50 AI Project 5)

## Overview
This project builds and evaluates a Convolutional Neural Network (CNN) using TensorFlow and Keras to classify road signs from the German Traffic Sign Recognition Benchmark (GTSRB) dataset across 43 different categories.

## Experimentation and Design Process

### 1. Initial Architecture & The Role of Input Normalization
Our initial baseline architecture consisted of:
- **Conv2D (32 filters, 3x3 kernel, ReLU activation)**
- **MaxPooling2D (pool size 2x2)**
- **Conv2D (64 filters, 3x3 kernel, ReLU activation)**
- **MaxPooling2D (pool size 2x2)**
- **Flatten**
- **Dense (128 units, ReLU activation)**
- **Dropout (0.5)**
- **Dense (43 units, Softmax activation)**

**Observation & Discovery:**
When trained directly on raw pixel values in the range `[0, 255]` returned by OpenCV, the initial loss exploded to $\approx 89.7$, and gradient updates caused severe saturation. After 10 epochs, the network stagnated around 5.4% accuracy. 

To address this, we integrated an input normalization layer (`tf.keras.layers.Rescaling(1.0 / 255)`). Normalizing pixel values into the range `[0.0, 1.0]` dramatically stabilized gradient propagation: initial cross-entropy loss dropped to 3.76 in the very first epoch, and the network converged smoothly.

### 2. Number and Sizing of Convolutional & Pooling Stages
We experimented with different convolutional depth configurations:
- **Single Conv Block (32 filters, 3x3, pool 2x2):**
  This achieved approximately 88% test accuracy. While computationally lightweight, it underperformed on fine-grained distinctions between similar circular warning or speed-limit signs.
- **Two Conv Blocks (32 filters followed by 64 filters, both 3x3 with 2x2 pooling):**
  Adding a second convolutional hierarchy allowed the network to learn compositional features—moving from low-level edges and color gradients to distinctive shapes and traffic symbols. Training accuracy rose rapidly above 94%.
- **Three Conv Blocks (32 -> 64 -> 128 filters):**
  Given the compact input resolution ($30 \times 30$), three pooling stages reduced spatial dimensions to $2 \times 2$, leading to spatial information loss without measurable accuracy improvement over the two-block design.

### 3. Dense Layer Capacity and Dropout Regularization
To map high-dimensional convolutional features into 43 categorical distributions:
- We tested dense hidden layers of size 64 vs. 128 units. The 128-neuron layer provided sufficient capacity to capture complex combinations of sign features across all 43 classes.
- Without regularization, the network showed signs of overfitting around epoch 6, where training loss continued to decline while test loss plateaued.
- We tested dropout rates of 0.2, 0.4, and 0.5. A dropout rate of **0.5** provided the best generalization, forcing distributed feature representation and preventing neuron co-adaptation.

### 4. Final Architecture & Quantitative Results
The finalized network architecture is structured as follows:
1. **Rescaling Layer:** `1.0 / 255` (input shape $30 \times 30 \times 3$)
2. **Conv2D:** 32 filters, $3 \times 3$ kernel, ReLU activation
3. **MaxPooling2D:** Pool size $2 \times 2$
4. **Conv2D:** 64 filters, $3 \times 3$ kernel, ReLU activation
5. **MaxPooling2D:** Pool size $2 \times 2$
6. **Flatten Layer**
7. **Dense Layer:** 128 neurons, ReLU activation
8. **Dropout Layer:** Rate 0.5
9. **Dense Output Layer:** 43 neurons, Softmax activation

**Compilation & Training:**
- Optimizer: **Adam**
- Loss: **Categorical Crossentropy**
- Metric: **Accuracy**
- Epochs: 10

**Evaluation Performance on Test Split (40% hold-out, 10,656 test images):**
- **Test Loss:** `0.0598`
- **Test Accuracy:** `98.57%`
