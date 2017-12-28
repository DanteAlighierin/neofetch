# neofetch

I made this because I got a laptop from my school which runs macOS but my IT admin has blocked me from using the brew command. I wanted to install neofetch but since I couldn't use brew I decided to write neofetch my self in Python as a fun project and because I thought it would be a nice project and I wanted neofetch on my laptop.

## Installation
```bash
curl https://raw.githubusercontent.com/sdushantha/neofetch/master/neofetch > neofetch && mkdir -p ~/bin && mv neofetch ~/bin && chmod +x ~/bin/neofetch
```

Add ```export PATH=$PATH":$HOME/bin"``` to ```.bash_profile``` or ```.profile```


Then ```source .bash_profile``` or ```source .profile```

## Preview

![screen shot 2017-12-28 at 15 31 19](https://user-images.githubusercontent.com/27065646/34413513-46ba780e-ebe4-11e7-93ec-f2b9602321b2.png)
