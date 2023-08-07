
# Hotel Bot

This project is to book a Hotel (Barasti) room using Conversational AI.

# Tech Stack

- [Python 3.9.0](https://www.python.org/downloads/release/python-390/)
- [Conda 23.1.x](https://docs.conda.io/projects/conda/en/23.1.x/user-guide/install/index.html)
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=mac)
- [Visual Studio Code](https://learn.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2022)
- [Git](https://git-scm.com/downloads)
- [Sublime Merge](https://www.sublimemerge.com/download)

# Installation Steps

Assuming the Tech stack mentioned above is installed completely, if so move ahead with the below instructions. (The below instructions are provided for Mac M1 Silicon, the below commands more or less stay the same for `Windows` and `Linux`)

```bash
git checkout https://github.com/astrokathi/hotel-bot-rasa.git

# Assuming this is executed from Documents folder
# Once the checkout is completed, then you could see the below folder structure
#   Documents | 
#       -- hotel-bot-rasa |
#           -- Chatbot-Widget-Main |
#           -- hotel-bot-chat |
#           -- hotel-bot |
#           ... (other files)

cd ~/Documents/hotel-bot-rasa
# From here on this is referred to as the Root directory.
```

- Once the code is checkedout, open the folder `hotel-bot-rasa` in PyCharm.
- Open terminal from the PyCharm IDE and execute the below commands.

```bash
# Creating the new virtual environment

conda create -n rasa python=3.9.0

# rasa is the environment name

conda activate rasa

# This will make the rasa environment active, now we can use conda/pip to manage the packages.

# From the root directory, execute the below command to install all the dependencies needed for RASA 3

pip install -r requirements.txt

# Once all the dependencies are installed, then the below Rasa commands to be executed.
```

# Rasa commands

To check whether the training data, stories, rules and domain configurations provided is valid or not, we can use the below command, this is the first step to validate the training data and if any errors found, we can make the necessary modifications.

### Rasa verification
```python
rasa --version
# If the response is received for the above command, then move ahead, if not the Rasa is
# not installed properly and need to follow the guidelines to install.
# For Mac M1 Silicion processors, use this link as the guide for the Rasa installation.
# https://forum.rasa.com/t/an-unofficial-guide-to-installing-rasa-on-an-m1-macbook/51342
# All the necessary files are available in the root directory.
```

### Rasa Data validation
```python
rasa data validate
# This provides errors if the training data is not properly defined.
```

### Rasa Train
```python
rasa train --debug
# This trains the NLU data and generates the NLU model
# The --debug switch provides insights on the logs on what process is running
```

### Rasa Action Server
```python
rasa run actions --debug
# We have custom actions written.
# So prior to running the Rasa Server, the action server has to be Run.
# The --debug switch provides insights on the logs on what process is running
```

### Rasa Server
```python
rasa run -m models --enable-api --cors "*" --debug
# -m switch says to which directory it needs to look to load the model.
# --enable-api switch is to enable Rest APIs, so the communication can be tested
# from the Postman or any Rest Client.
# --cors switch is to handle filtering unknown origins, for now we keep it "*'
# This allows all origins or any origin.
# The --debug switch provides insights on the logs on what process is running
```

### Visual Studio

Open the folder `hotel-bot-chat` from the root directory in VSCode. Install the extension [Live Preview](https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server) in VSCode.
Once the extension is installed, then open `index.html` in VSCode and from command pallette, start the live preview, this will host the Rasa webchat in `localhost` on port `3000` (this is the default port, all these settings can be changed from the extension settings, including the IP Address).
The caht bot will be opened in the browser as shown below, the chat widget on the bottom right can be used to ask questions or FAQs related to the Hotel room booking.


[Reference Image](attach)


## Badges

[![Python](https://img.shields.io/badge/Python-Rasa-yellow.svg)](https://rasa.com/docs/rasa/)
[![HTML5](https://img.shields.io/badge/Html5-Rasa%20Webchat-blue.svg)](https://chat-widget-docs.rasa.com/?path=/docs/rasa-chat-widget--widget)