FROM python:3.8.6-buster
COPY model.joblib /model.joblib
COPY MemoBrainModel /MemoBrainModel
COPY api /api
COPY requirements.txt /requirements.txt
#COPY /path/to/your/credentials.json /credentials.json
COPY /home/cynthias13w/code/cynthias13w/gcp/memobrain-342910-0a8ef6226044.json
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
