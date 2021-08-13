FROM mcr.microsoft.com/playwright:focal

RUN mkdir /app && mkdir /app/sessions && chmod 333 /app/sessions
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm i

# Bundle app source
COPY *.js ./
COPY *.html ./

# For prod:
ENV FLAG=uiuctf{i_R4al1y_h0p3_u_d0nt_c0Nv3rt_sVgs_l1k3_th1S}
ENV HCAPTCHA_SECRET=0x41b6C2010685D10D1803A214AC342f928d73bC56
ENV SECRET=ac70b2afb26c77b9a15f
ENV NODE_ENV=production
# ENV DEBUG=1


# For dist:
# ENV FLAG=uiuctf{REDACTED}
# ENV HCAPTCHA_SECRET=REDACTED
# ENV SECRET=REDACTED
# ENV NODE_ENV=production



# mount /sessions for local FS
# will NOT work for scaling multiple containers because /sessions is local
# need gcsfuse mount on /sessions
CMD mount -t tmpfs none /tmp && mount -t tmpfs none /app/sessions && node /app/server.js
