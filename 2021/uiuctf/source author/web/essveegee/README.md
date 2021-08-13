# essveegee

## Dev notes
- run ./make_handout.sh to reassemble the handout file for ctfd
- this challenge isn't really designed to scale w/ kctf but it might be possible with a gcsfuse mount on /app/sessions
- healthcheck does an e2e test :)
- TODO improvements if time:
  - auto-reaping sessions or confirm that it restarts container if storage limits reached?