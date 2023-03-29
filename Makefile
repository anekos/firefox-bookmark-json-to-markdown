
.PHONY: mypy
mypy:
	(source .venv/bin/activate ; axe *.py mypy.ini -- mypy %1)

.PHONY: run
run:
	(source .venv/bin/activate ; axe *.py -- python %1)
