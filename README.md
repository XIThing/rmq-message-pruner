# RMQ Message Pruner

Filter messages from a RabbitMQ queue based on matching text. Messages can be
removed or republished depending on the chosen mode.

## Install (from source)
```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
```

## Usage
```sh
rmq-message-pruner \
  --queue events \
  --match "foo" --match "bar" \
  --match-mode all
```

## Options
- `--host`, `--port`, `--vhost`, `--user`, `--password`: connection settings.
- `--queue`: queue name to read from.
- `--match`: substring match rules (repeatable).
- `--match-mode`: `any` or `all`.
- `--ignore-case`: match case-insensitively.
- `--republish`: put non-matching messages back on the queue.
- `--workers`: number of worker threads.
- `--batch-size`: number of messages to acknowledge at once.
- `--max-messages`: stop after processing N messages.

## Development
```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
pytest
```

## License
See `LICENSE`.
