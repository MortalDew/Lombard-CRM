FROM python:slim
COPY . /src
WORKDIR /src
RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev
RUN pip3 install --upgrade pip && pip3 install -U -r requirements.txt && apt-get update && apt-get install libcairo2-dev -y && apt-get install libpango1.0-dev -y
CMD bash -c 'python3 pawnshop_crm/manage.py migrate && python3 pawnshop_crm/manage.py runserver 0.0.0.0:8000'