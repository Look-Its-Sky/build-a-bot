# Partial Credit to 
# https://lazypro.medium.com/build-a-small-ta-lib-container-image-dcc22c77fa62
FROM python:3.7-slim AS compile-image

WORKDIR /build
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc wget
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install numpy
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/opt/venv && \
  make && \
  make install
RUN pip install --global-option=build_ext --global-option="-L/opt/venv/lib" TA-Lib==0.4.16
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PATH="/opt/venv/bin:$PATH"
ENV LD_LIBRARY_PATH="/opt/venv/lib"

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
