# Tryhackme_Room_Scripts
Exploits, scanners, etc

## Original Script: Brute Force Login with Captcha
Description

This script reads a list of usernames from a file, and attempts to log in to a website using these usernames along with a default password. The website also contains a captcha that requires solving a simple math problem. The script extracts the captcha, solves it, and submits the login request along with the captcha answer.

### Requirements

    Python 3.x
    requests library

### Usage

    Install the required libraries:

```
pip install requests
```

    Create a text file named usernames.txt with a list of usernames, one per line.

    Run the script:

```
python BruteG.py
```



## Enhanced Script: Brute Force Login with Captcha and Neural Network
### Description

This script is an enhanced version of the original brute force login script. It adds a neural network to predict the probability of a successful login attempt based on the error message received after each login attempt. The neural network uses TensorFlow and Keras to process the error messages and make predictions.

### Requirements

    Python 3.x
    requests and tensorflow libraries

### Usage

    Install the required libraries:

```
pip install requests tensorflow
```

    Create a text file named usernames.txt with a list of usernames, one per line.

    Train a neural network using TensorFlow and Keras, and save the trained model as your_trained_model.h5. Replace this filename in the script with the actual name of your trained model.

    Update the tokenizer initialization in the script with the same parameters used during the training of the neural network.

    Run the script:
```
python brute_force_login_with_neural_network.py
```

Note: The neural network integration assumes you have already trained a neural network model using TensorFlow and Keras. You will need to customize the model architecture and training parameters based on your specific task and dataset.
