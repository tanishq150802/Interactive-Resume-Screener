# Interactive-Resume-Screener
### A real-time LLM App powered by Pathway's llm-app to help recruiters interact with JDs &amp; CVs, and help them take informed decisions

By: [Tanishq Selot](https://github.com/tanishq150802) , A modification of [Pathway's Dropbox AI Chat App](https://github.com/pathway-labs/dropbox-ai-chat) - Instructions to run are similar. Clone this repository to a local folder & install Dropbox and Docker (for containerizing in case Windows OS). 

Open Command Prompt. ```cd``` into the cloned repository and use the commands ```docker-compose build``` and ```docker-compose up``` to find the app running on http://localhost:8501/.

### About the App
![image](https://github.com/tanishq150802/Interactive-Resume-Screener/assets/81608921/1c670e25-bb30-44f3-aeb3-ed0db4bec646)
* This tool enables the recruiters to interact with CVs and Job Descriptions, making resume screening interactive and more dynamic. In the example above, the ML Engineer JD is uploaded to the dropbox folder where other candidate CVs are already stored. 
* [Pathway/llm-app's](https://github.com/pathwaycom/llm-app) seemless vector indexing for Retrieval augmented generation enables the recruiters to take informed decisons by prompting the LLM to rank the CVs based on specific fields/skills from the JD.
* LLM can also be prompted to suggest feedback specific to the JD and CVs which can improve the current feedback scenario where the candidates just receive a selection/rejection message in the form of feedback.
* Mostly, recruiters lack technical skills and rely on Team leads or Managers who design the JDs, while shortlisting. This App makes the first stage of recruitement more independent and simpler for them.
* This is highly instrumental in today's time when high volumes of Job applications are processed daily.
* This has a high business value as a B2B product which revolutionize the recruitement process.
* Pathway made it very easy to chain this whole project while making use of OpenAI's GPT-3.5 Turbo as the LLM.

## Requirements
* pathway
* llm_app
* unstructured[all-docs]==0.10.15
* tiktoken
* requests
* datetime
* streamlit
* python-dotenv

### References
* [Pathway's llm-app](https://github.com/pathwaycom/llm-app)
* [Streamlit](https://streamlit.io/)
