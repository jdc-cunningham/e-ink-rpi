sudo apt update
sudo apt upgrade
sudo apt install python3-pil

python -m venv .e-paper
source .e-paper/bin/activate
python -m pip install -r requirements.txt
