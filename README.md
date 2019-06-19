# AutoSelfie_bot. Telegram:  @AutoSelphi_bot

### Description:

Telegram Bot for Automate Selphi segmentation
It is small demo of the work of the neural network from my project: 
https://github.com/DmitriiDenisov/faces_picsart
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

![alt-text-1](https://i.ibb.co/MPBN9Fh/Screen-Shot-2019-06-09-at-19-13-38.png "title-1") ![alt-text-2](https://i.ibb.co/PwZ2tqQ/Screen-Shot-2019-06-09-at-19-01-45.png "title-2")

![alt-text-1](https://i.ibb.co/h8hfFCb/Screen-Shot-2019-06-09-at-19-02-02.png "title-1") ![alt-text-2](https://i.ibb.co/NrLZgNK/Screen-Shot-2019-06-09-at-19-02-12.png  "title-2")
![alt-text-1](https://i.ibb.co/Vq19TNp/Screen-Shot-2019-06-09-at-19-03-51.png "title-1") ![alt-text-2](https://i.ibb.co/Fn3GBjy/Screen-Shot-2019-06-09-at-19-04-38.png "title-2")
![alt-text-1](https://psv4.userapi.com/c848320/u6729856/docs/d6/eb84b77a7a15/Screen_Shot_2019-06-09_at_19_13_38.png?extra=tDiTaKhYBV64EA2RUy844LWqrkM0kKekXv3DaFdPZ4p0NSO2CQHz9nEP8mh3Lp_WSpYBPfe8OrDq61Hm0FJtx3bMizzcDc0S60EJtPP9G6ObXresksO54ro0B5sQ26M2cMUor3apzLse9RiO) ![alt-text-2](https://i.ibb.co/WnxW9xh/Screen-Shot-2019-06-09-at-19-13-23.png "title-2")


