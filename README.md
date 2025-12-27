# Gruvbox Material for Lazygit

This repository provides themes for [Lazygit](https://github.com/jesseduffield/lazygit) based on the [Gruvbox Material](https://github.com/sainnhe/gruvbox-material) color palette.

## Screenshots

*(Coming soon)*

## Installation

1.  Choose a theme from the `themes/` directory.
2.  Copy the content of your chosen theme file.
3.  Open your Lazygit configuration file. The location depends on your operating system:
    *   **Linux:** `~/.config/lazygit/config.yml`
    *   **macOS:** `~/Library/Application Support/lazygit/config.yml`
    *   **Windows:** `%APPDATA%\lazygit\config.yml`
4.  Paste the theme content into the `theme` section of your `config.yml`. If the `theme` section doesn't exist, you can create it.

For example:
```yaml
theme:
  activeBorderColor:
    - "#d4be98"
    - bold
  inactiveBorderColor:
    - "#504945"
  optionsTextColor:
    - "#66c2cd"
  selectedLineBgColor:
    - "#504945"
  selectedRangeBgColor:
    - "#504945"
  cherryPickedCommitBgColor:
    - "#504945"
  cherryPickedCommitFgColor:
    - "#d8a657"
  unstagedChangesColor:
    - "#ea6962"
  defaultFgColor:
    - "#d4be98"
  searchingActiveBorderColor:
    - "#d8a657"
```

## Development

This project uses a Python script to generate the themes from a template.

### Prerequisites

*   Python 3.6+
*   [uv](https://github.com/astral-sh/uv) (for dependency management)

### Setup

1.  Install the dependencies:
    ```sh
    make install
    ```

### Generating Themes

To generate the themes once:

```sh
make run
```

To watch for changes in `palettes.yml` or `theme_template.yml` and automatically regenerate the themes:

```sh
make watch
```

To remove the generated themes:

```sh
make clean
```

## Credits

The color palettes are based on the [Gruvbox Material](https://github.com/sainnhe/gruvbox-material) theme by sainnhe.

