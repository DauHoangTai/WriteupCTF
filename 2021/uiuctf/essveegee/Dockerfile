FROM mcr.microsoft.com/playwright:focal

RUN mkdir /app && mkdir /app/sessions && chmod 333 /app/sessions
WORKDIR /app
COPY package*.json .
RUN npm i

# Bundle app source
COPY *.js .

# For handout:
ENV FLAG=uiuctf{REDACTED}
ENV HCAPTCHA_SECRET=REDACTED
ENV SECRET=REDACTED
ENV NODE_ENV=production
# uncomment this to bypass hcaptcha when testing
# ENV DEBUG=1

CMD mount -t tmpfs none /tmp && mount -t tmpfs none /app/sessions && node /app/server.js
