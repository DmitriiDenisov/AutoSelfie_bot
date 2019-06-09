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

![alt-text-1](https://psv4.userapi.com/c848136/u6729856/docs/d5/2f8c48949113/Screen_Shot_2019-06-09_at_19_02_02.png?extra=WU2FwQIeplhUgXGFT4s34qIsSbRzaTA4mxBFinqQ9RUMcBDPKmSkKpNaLMFVab8bEoKXYDS2Nno-EBihtAKQpBSaS-uknIHVm1hq-W0w_rwBgJqxWT_sSDakB2DP3Q0i-Z90mnKc9HwaTMR4 "title-1") ![alt-text-2](https://psv4.userapi.com/c848320/u6729856/docs/d12/d7e442d4a8ca/Screen_Shot_2019-06-09_at_19_02_12.png?extra=tcpAwHPUjjHNPbPOP2UerIIH778uRHEbZN6I5PAD_Yk2BmMNV2YHXiJK6hhwDvXUmeVBMhfSV58CFiuKcuHZ-z3LjqOydlQVv6rnNgMLeLXZMAhlJSKiqhqLdB-cKXB1vX6A4jpmBUN_bqh7 "title-2")

![alt-text-1](https://psv4.userapi.com/c848220/u6729856/docs/d3/9cab01e89043/Screen_Shot_2019-06-09_at_19_01_45.png?extra=vBB3xusBTBXH6Kfv8imCIjQkY74RL8ksSptO6fnRxrFW9QbhyaZ-Fdv5fQwi7IKaUVGreZa49Rjt2QRsOcfTq21Y2xyfr5gq8JROUKg_0BjiFIcRpRnyUvD7pldWs3HoZW2Q3l2cgvU4woAl "title-1") ![alt-text-2](https://psv4.userapi.com/c848036/u6729856/docs/d11/d9ac3d2538dd/Screen_Shot_2019-06-09_at_20_58_17.png?extra=v27Yjjkc3Ei9Vp3JUA7PrDpSsXgqCkrI5ZYQ9xrZpZZwO_34FFq83BbyUbkCzxX7va37rNHozjlrh75SMmquP9nFUBpfenS9O9DUEVwhmUyO9UDXdYwjP0qLHlDw8m8sSXFEh-26pqMciXzP  "title-2")
![alt-text-1](https://psv4.userapi.com/c848024/u6729856/docs/d3/cd17e4a9ab31/Screen_Shot_2019-06-09_at_19_03_51.png?extra=XQ0J_bngRXLOWUk8bjFEtih1Ek_37L5jrI6TvrvCULDINhNwF_axFuiJMRMpO5PSEGr4E03aPQBXGTODRy0iQ5QU5n3Y0qUwcJk8eRmYCDvuuQfijvDzhpB5NvoUaYUcbCWeSVklNErzo5f- "title-1") ![alt-text-2](https://psv4.userapi.com/c848036/u6729856/docs/d2/5ca9502877f3/Screen_Shot_2019-06-09_at_19_04_38.png?extra=DrDJIDWhEa6ut1VsD8LLELpdEB3DkmHRBSgIBAE8H9duwLuYkIujmoTA7fovOaIy9_YM3Tbr6OCxlo2t3wbpqAO3pgKjuFJyD8uqmbFL31qPVE3L2fejBTtErOopzpnfktjSD1rl-fdbT2ID "title-2")
![alt-text-1](https://psv4.userapi.com/c848320/u6729856/docs/d6/eb84b77a7a15/Screen_Shot_2019-06-09_at_19_13_38.png?extra=tDiTaKhYBV64EA2RUy844LWqrkM0kKekXv3DaFdPZ4p0NSO2CQHz9nEP8mh3Lp_WSpYBPfe8OrDq61Hm0FJtx3bMizzcDc0S60EJtPP9G6ObXresksO54ro0B5sQ26M2cMUor3apzLse9RiO) ![alt-text-2](https://psv4.userapi.com/c848216/u6729856/docs/d11/eb99983263d7/Screen_Shot_2019-06-09_at_19_13_23.png?extra=CmvhnOVoVkDFzQtOUnuF4WdgM0zTKJY2_O9TJiSvV43WN8AQRgHbMOf7dL5tYH2gUueuZVY0FSY5ZxhB_QF6J3U8Mb_9XHNe12g4J5haXY2qwJZt62wnr8yn4KzlZFkp-1Go2t1N7yqr8cqw "title-2")


