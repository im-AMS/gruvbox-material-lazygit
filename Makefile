# Makefile for gruvbox-material-lazygit theme generator

.PHONY: all install run watch clean

# Default target
all: run

# Install Python dependencies using uv
install:
	uv sync

# Generate the themes once
run:
	uv run generate.py

# Watch for changes and automatically regenerate themes
watch:
	uv run generate.py --watch

# Remove the generated themes directory
clean:
	rm -rf themes

# Help target to display available commands
help:
	@echo "Available commands:"
	@echo "  make install   - Install dependencies"
	@echo "  make run       - Generate themes once"
	@echo "  make watch     - Watch for file changes and regenerate themes"
	@echo "  make clean     - Remove generated themes"
