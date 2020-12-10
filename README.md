# Lightshow

Lightshow is a collection of LED strip animations controlled by a single unified web interface. 
Instructions and setup documentation to come. This project is still in early development.

*Just a warning: Most of this code is subject to change. There are a lot of things I would like to rework
eventually. I am developing this in parallel with my school course load so these things will happen
when they happen.*

![](assets/webpanel.png?raw=true)

## Downloading and Running

```bash
git clone https://github.com/djcopley/lightshow.git
cd lightshow
python3 setup.py install
export FLASK_APP=lightshow.main
sudo -E flask run -h 0.0.0.0 -p 80
```

## Supported Hardware
- Raspberry Pi
- WS2811 series RGB addressable LED strips
