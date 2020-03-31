FROM selenium/standalone-chrome
USER root
WORKDIR /root
RUN apt -y update && apt install -y python3 python3-dev python3-pip
RUN pip3 install selenium gunicorn flask twitter

#RUN curl https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
#RUN apt update -y && apt install -y google-chrome-stable unzip
#RUN wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
#RUN unzip chromedriver_linux64.zip -d ~/bin/
#RUN export PATH=$PATH:$HOME/bin

#COPY main.py main.py
COPY app.py app.py
COPY ./var var
#RUN python3 main.py
RUN mkdir downloads
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]