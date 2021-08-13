tar --owner="arx" --group="arx" \
    --exclude challenge/Dockerfile \
    --transform 's|Dockerfile.handout|Dockerfile|' \
    --transform 's|challenge|pwnyIDE|' \
    -czvf handout.tar.gz challenge
