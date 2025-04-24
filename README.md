
# Minecraft Server x Ngrok Status

Page displaying status and address of Minecraft server running on ngrok (addresses change on each restart and I can't bother sending it each time to my friends). The UI is simple (if your mind still lives in 2005), I'll let you discover it yourself.

## Run Locally

Clone the project

```bash
  git clone https://github.com/ereszka/minecraft_status
```

Go to the project directory

```bash
  cd minecraft_status
```


Create .env file 

```bash
  cd app && cp .env.template .env
```

Fill API_KEY with ngrok API key value.

Install dependencies

```bash
  pip install flask
  pip install python-dotenv
```

Start the server

```bash
  python home.py 
```

or 

```bash
  flask --app home run
```

