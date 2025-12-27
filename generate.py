import yaml
import os
import time
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def generate_themes():
    """
    Loads palettes and a template to generate theme files.
    """
    # Create themes directory if it doesn't exist
    if not os.path.exists("themes"):
        os.makedirs("themes")

    # Load palettes and template
    try:
        with open("palettes.yml", "r") as f:
            palettes_data = yaml.safe_load(f)

        with open("theme_template.yml", "r") as f:
            template = f.read()

        # Generate a theme file for each palette
        for palette_name, colors in palettes_data.get("palettes", {}).items():
            theme_content = template
            for color_name, color_value in colors.items():
                theme_content = theme_content.replace(f"{{{{ {color_name} }}}}", str(color_value))

            with open(f"themes/{palette_name}.yml", "w") as f:
                f.write(theme_content)
        print("Themes generated successfully in 'themes/' directory.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure palettes.yml and theme_template.yml exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


class ThemeChangeHandler(FileSystemEventHandler):
    """
    Handles file system events for the theme files.
    """
    def on_modified(self, event):
        if event.src_path.endswith(("palettes.yml", "theme_template.yml")):
            print(f"Detected change in {event.src_path}. Regenerating themes...")
            generate_themes()

def watch_files():
    """
    Watches for changes in palette and template files and regenerates themes.
    """
    event_handler = ThemeChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    print("Watching for file changes... (Press Ctrl+C to stop)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate or watch for theme changes.")
    parser.add_argument("--watch", action="store_true", help="Watch for file changes and regenerate themes automatically.")
    args = parser.parse_args()

    if args.watch:
        generate_themes() # Generate once at the start
        watch_files()
    else:
        generate_themes()
