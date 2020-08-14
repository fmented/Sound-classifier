# Drums sound classifier


**disclaimer**

*this codes require keras, sklearn, pandas, librosa and make sure FFMPEG is in your PATH if you're in Windows,*

*I wanted to make requirements.txt but seems I had some problems with my virtual environment, so I can not do pip freeze*

**preparation**

make sure you have directory structure like this for your audio files

```bash
📦drum
 ┣ 📂crash
 ┃ ┣ 📜Crash Cymbal #1.wav
 ┃ ┣ 📜Crash Cymbal #2.wav
 ┃ ┣ 📜Crash Cymbal #3.wav
 ┣ 📂hihat
 ┃ ┣ 📜Closed Hat Paiste 1.wav
 ┃ ┣ 📜Closed Hat Paiste 2.wav
 ┃ ┣ 📜Closed Hat Paiste 3.wav
 ┃ ┣ 📜Closed Hat Paiste 4.wav
 ┃ ┣ 📜Closed Hi-Hat rock.wav
 ┣ 📂kick
 ┃ ┣ 📜Andy Sneap Kick 00.wav
 ┃ ┣ 📜Andy Sneap Kick 01.wav
 ┃ ┣ 📜Andy Sneap Kick 02.wav
 ┃ ┣ 📜Andy Sneap Kick 03.wav
 ┃ ┣ 📜Andy Sneap Kick 04.wav
 ┃ ┣ 📜Andy Sneap Kick 05.wav
 ┃ ┣ 📜Andy Sneap Kick 06.wav
 ┃ ┣ 📜Andy Sneap Kick 07.wav
 ┣ 📂ride
 ┃ ┣ 📜Ride Bell Zidjian 1.wav
 ┃ ┣ 📜Ride Bell Zidjian 2.wav
 ┃ ┣ 📜Ride Cymbal (Bell) rock.wav
 ┃ ┣ 📜Ride Cymbal (Bell).wav
 ┃ ┣ 📜Ride Cymbal (Hard).wav
 ┃ ┣ 📜Ride Cymbal rock.wav
 ┃ ┣ 📜Ride Cymbal.wav
 ┃ ┣ 📜Ride Zidjian 1.wav
 ┃ ┣ 📜Ride Zidjian 2.wav
 ┣ 📂snare
 ┃ ┣ 📜A Snare 01.wav
 ┃ ┣ 📜A Snare 02.wav
 ┃ ┣ 📜A Snare 03.wav
 ┃ ┣ 📜A Snare 05.wav
 ┃ ┣ 📜A Snare 06.wav
 ┃ ┣ 📜A Snare 07.wav
 ┃ ┣ 📜A Snare 08.wav
 ┃ ┣ 📜A Snare 09.wav
 ┃ ┣ 📜A Snare 10.wav
 ┗ 📂tom
 ┃ ┣ 📜R Tom 1 Hard 1.wav
 ┃ ┣ 📜R Tom 1 Hard 2.wav
 ┃ ┣ 📜R Tom 1 Hard 3.wav
 ┃ ┣ 📜R Tom 1 Hard 4.wav
 ```

and then in **setting.py** change *main_dir* variable to your root audio files directory (absolute path is recommended) like the example above
and also change *model_name* variable to whatever it should be 

after everything is set run **main.py**


