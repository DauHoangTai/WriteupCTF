tar --owner="arx" --group="arx" \
    --exclude challenge/Dockerfile \
    --transform 's|Dockerfile.handout|Dockerfile|' \
    --transform 's|challenge|essveegee|' \
    -czvf handout.tar.gz challenge
