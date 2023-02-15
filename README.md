<div align="center">
  <img src="/assets/logo.png" alt="logo" width="200" height="auto" />
  <h1>API_ControlTV</h1>
  
  <p>
    A lightweight API to control TV's via CEC-Client with a Raspberry Pi
  </p>
  
<h4>
    <a href="https://github.com/Ki-re/dgt_exam_alert/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/Ki-re/dgt_exam_alert/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- About the Project -->
## About the Project

A simple script that tracks the exam results on the DGT and sends a telegram message with the conclussion once published

This script was designed on 2022 and is no longer being mantained, feel free to adapt the code to your needs

<!-- Requirements -->
### Requirements

In order to run this script you will need: 

```bash
 pip install selenium
```

```bash
 Download the chromedriver version that matches your chrome version: https://chromedriver.chromium.org/downloads
```

### Get Started

Clone the project

```bash
  git clone https://github.com/Ki-re/dgt_exam_alert.git
```

Clone the project

```bash
  git clone https://github.com/Ki-re/dgt_exam_alert.git
```

Create your telegram bot with BotFather

```bash
  /newbot
```

Get your bot's telegram token and the chat id where you want the result message to be sent

```bash
  telegram_bot_token = ""
  chat_id = ""
```

Set-up the config.py file with your data

```bash
  nif = "00000000A"
  fecha_examen = "00/00/0000"
  fecha_nacimiento = "00/00/0000"
  carnet = ""
  update_time = 300 
  telegram_bot_token = ""
  chat_id = ""
```

## Contributing

Contributions are always welcome!

<!-- License -->
## License

Distributed under the no License. See LICENSE.txt for more information.
