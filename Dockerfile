FROM debian:12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    cowsay \
    fortune-mod \
    fortunes \
    netcat-openbsd \
    curl && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/games:${PATH}"

WORKDIR /app
COPY wisecow.sh .
RUN chmod +x wisecow.sh

EXPOSE 4499

CMD ["/app/wisecow.sh"]
