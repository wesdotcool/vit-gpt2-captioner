FROM huggingface/transformers-pytorch-gpu
WORKDIR /captioner
COPY download_model.py .
RUN python3 download_model.py
COPY . .
RUN mkdir images/
ENV FLASK_APP=captions
CMD flask run "--host=0.0.0.0"
