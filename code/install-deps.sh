sudo apt update
sudo apt upgrade

python -m venv .e-paper
source .e-paper/bin/activate
python -m pip install -r requirements.txt

# clone the specific subfolder
git clone --no-checkout https://github.com/waveshare/e-Paper.git
cd e-Paper
git sparse-checkout init --cone
git sparse-checkout set RaspberryPi_JetsonNano/python
git checkout master
