# Lightshow

Lightshow is a collection of LED strip animations controlled by a single unified web interface. 
Instructions and setup documentation to come. This project is still in early development.

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
