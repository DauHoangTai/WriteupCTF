tar --owner="kuilin" --group="kuilin" \
    --exclude challenge/flag.txt \
    --exclude challenge/Dockerfile \
    --transform 's|Dockerfile.handout|Dockerfile|' \
    --transform 's|challenge|wasmcloud|' \
    -czvf handout.tar.gz challenge