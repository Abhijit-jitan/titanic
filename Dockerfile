FROM python:3.6-slim-buster
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit","run"]
CMD ["Streamlit_prototype.py"]
