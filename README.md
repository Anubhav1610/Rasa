# Rasa_Covid19

This is a chatbot developed to provide information about the covid-19 cases.

Training the NLU model
Since the release of Rasa 1.0, the training of the NLU models became a lot easier with the new CLI. Train the model by running:

rasa train nlu
Once the model is trained, test the model:

	rasa shell nlu

Training the dialogue model
The biggest change in how Rasa Core model works is that custom action 'actions' now needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file. This is how to train and run the dialogue management model:


Start the custom action server by running:
	
	rasa run actions


Open a new terminal and train the Rasa Core model by running:
	
	rasa train

Talk to the chatbot once it's loaded after running:
	
	rasa shell

Starting the interactive training session:
To run your assistant in a interactive learning session, run:
Make sure the custom actions server is running:
	
	rasa run actions

Start the interactive training session by running:
	
	rasa interactive
