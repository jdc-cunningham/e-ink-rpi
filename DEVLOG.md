### 10/22/2026

8:08 PM

Alright so this is pretty annoying and it might be due to interference but this pi zero w on my desk keeps losing the wifi connection.

Specifically to the desktop mobile hotspot next to it.

There is a Pi 4B about a ft away and then a pi zero non-w maybe 5 feet away... another Pi zero w 10 ft away and another like 20 ft away.

This is the one that is having problems though for some reason.

I was looking into this, it is pretty straightforward to get this to work, I should have just RTFM.

Specifically this one:

https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual#Working_With_Raspberry_Pi

I'll be using Python

<img src="./devlog-images/small-hdmi-display.JPG"/>

It's annoying setting this up, this display is terrible too it's 3.5" but 480x320 resolution really hard to read.

At least a raw HDMI signal

8:17 PM

Today I want to get something displayed on this screen.

I think the main driver or thing I have running in the end is a CRON job that runs a python script that then displays something on the screen.

Specifically it'll countdown how many days I have till I move into my new apartment, that's a nexus point in my life.

If I don't make that I'm f'd I won't die but my life will suck. Like if I don't get into that apartment it means something went wrong and I'm gonna be homeless.

---

### 10/21/2026

6:30 PM

Need to find a basic driver to display stuff on the screen. I had tried a JS one in the past but I'll probably just use a python one.

What's annoying is my wifi router broke so I've been using my desktop's hotspot but the IP addresses keep jumping around.

I had to connect this pi to an HDMI display to run `nmtui`.
