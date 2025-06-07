FROM python:3.13-slim as generate
WORKDIR /usr/src/app

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
	pip install -r requirements.txt

COPY src/ ./src/
COPY user_stories/ ./user_stories/

ENTRYPOINT ["python", "./src/main.py"]

FROM node:lts-alpine3.22 as execute
WORKDIR /usr/src/app
ENV NODE_ENV test

COPY package.json .
RUN --mount=type=cache,target=/root/.npm \
	npm i --save

COPY babel.config.js .

CMD ["npm", "test"]
