# AutoSelfie_bot

### Description:
Telegram Bot for Automate Selphi segmentation
It is small demo for my another repo: https://github.com/DmitriiDenisov/faces_picsart
### Fast Launch instructions:

1. Clone repository 
2. Run init.py: it will download model file for you
3. Create file token.txt in root directory and place there token of your Telegram bot
4. (Optional) Create file server_parameters.txt in root directory and place there internal IP of your server (this is only for duplicating your server)
5. Run from root directory ```sudo docker build -t selphie_image -f Dockerfile.server .```
6. Run from root directory ```docker run -v `pwd`/models:/app/models -d --name selfie_cont --restart always --hostname $(hostname) selphie_image```

### Author
Dmitrii Denisov; 
Telegram: @DmitriiDenisov

### Example of work:
<p align="center">
  <img src="" width="450" alt="accessibility text">
</p>

