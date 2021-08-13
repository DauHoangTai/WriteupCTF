FROM mcr.microsoft.com/playwright:focal

RUN mkdir /app && mkdir /files
WORKDIR /app
COPY package*.json .
RUN npm i && npm i -g tcpslow

COPY start.sh .

COPY *.js .
COPY static static

ENV FLAG=uiuctf{i_h0P3_th4t_waS_a_fUn_ch4In_75d997b}
ENV HCAPTCHA_SECRET=0x41b6C2010685D10D1803A214AC342f928d73bC56
ENV ADMIN_TOKEN=6d1cbcc5a8c00e4ce2807ffc20963a0d
# Turn this on when testing locally to bypass hCaptcha
# ENV DEBUG=1
CMD mount -t tmpfs none /tmp && mount -t tmpfs none /files && ./start.sh
