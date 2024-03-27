# Alindor_Project

Overview:
The project is a web application that provides text and audio conversation summarization using Deepgram API and OpenAI API. Users can upload either text files or audio files, and the application will generate a concise summary of the conversation.


Features:
Text Conversation Summarization: Users can upload text files containing conversations, and the application will summarize the dialogue using OpenAI API.
Audio Conversation Summarization: Users can upload audio files containing conversations, and the application will transcribe the audio using Deepgram API and summarize the dialogue using OpenAI API.
User-Friendly Interface: The web interface is intuitive and easy to use, allowing users to upload files with ease.
Real-Time Summarization: The application provides real-time summarization, allowing users to receive quick insights into the content of their conversations.
Installation

To run the application locally, follow these steps:

Install the required dependencies:

pip install -r requirements.txt

Run the Flask application:

export OPENAI_API_KEY="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"
python3 app.py

Usage:
Access the web application by navigating to http://localhost:5000 in your web browser.
Choose whether to upload a text file or an audio file.
Upload the file containing the conversation.
Wait for the summarization process to complete.
View the summarized conversation on the web interface.

Technologies Used:
Flask
HTML/CSS
JavaScript
Deepgram API
OpenAI API

Contributor:
Jessica Grover
