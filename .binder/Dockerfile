FROM ghcr.io/rocker-org/binder:4.4.2

ARG NB_UID=1000
ARG NB_GID=1000

COPY --from=ghcr.io/astral-sh/uv:0.11.18 /uv /uvx /bin/

WORKDIR /home/jovyan/

USER ${NB_UID}

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --all-groups --locked --no-install-project

RUN --mount=type=bind,source=.binder/bashrc-venv.sh,target=/mnt/bashrc-venv.sh,readonly \
    cat /mnt/bashrc-venv.sh >> .bashrc

COPY --chown=${NB_UID}:${NB_GID} . .

RUN uv sync --all-groups --locked

RUN uv run poe install-kernels

ENV VIRTUAL_ENV=/home/jovyan/.venv
ENV PATH="/home/jovyan/.venv/bin:${PATH}"

EXPOSE 8888
