# About

Some code for doing the following:

- using CRON to display something at an interval/schedule
- an API on the Pi Zero W which an Electron desktop app talks to

# Install deps

- `$chmod +x install-deps.sh`
- `$./install-deps.sh`

This project uses the example files from this repo: https://github.com/waveshareteam/e-Paper

# Run

You can manually run the code eg. `$python cron-display.py` or add it to cron like this:

- `$crontab -e`
- `* * * * * /usr/bin/python /home/pi/e-ink-rpi/code/cron-display.py` (every minute)
