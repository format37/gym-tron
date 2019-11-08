**installation**

*- go where gym package installed*

cd ~/.local/lib/python3.6/site-packages/gym/envs

*- clone this repository*

git clone https://github.com/format37/gym-lex.git

*- install this environment*

pip3 install -e gym-tron

*- install xvfb for notebook animations*

sudo apt install xvfb

**run the notebook**

xvfb-run -s "-screen 0 1400x900x24" jupyter notebook

*- open gym-tron/tron.ipynb and run*
