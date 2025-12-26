import yaml
import os
import time

# --- Hardcoded Filenames ---
INPUT_FILENAME = "gruvbox_config.yml"
OUTPUT_FILENAME = "gruvbox_dark.yml"

def process_yaml_file():
  """
  Reads the input YAML, resolves aliases, and writes the 'gui' part
  to the output file. This is the core conversion logic.
  """
  try:
    with open(INPUT_FILENAME, 'r') as file:
      full_config = yaml.safe_load(file)

    gui_config = full_config.get('gui')

    if gui_config:
      with open(OUTPUT_FILENAME, 'w') as file:
        yaml.dump({'gui': gui_config}, file, sort_keys=False, default_flow_style=False)
      print(f"✅ Updated '{OUTPUT_FILENAME}' successfully.")
    else:
      print(f"⚠️  'gui' section not found in '{INPUT_FILENAME}'. Output not generated.")

  except FileNotFoundError:
    print(f"❌ Error: Input file '{INPUT_FILENAME}' not found.")
  except yaml.YAMLError as e:
    print(f"❌ Error parsing YAML file: {e}")


def start_watching():
  """
  Monitors the input file for changes and triggers the processing function.
  """
  # Store the initial modification time of the file
  last_modified_time = os.path.getmtime(INPUT_FILENAME)
  print(f"👀 Watching for changes in '{INPUT_FILENAME}'. Press Ctrl+C to stop.")

  try:
    while True:
      # Check the file's modification time every second
      time.sleep(1)
      current_modified_time = os.path.getmtime(INPUT_FILENAME)

      # If the time has changed, the file has been saved
      if current_modified_time != last_modified_time:
        print("\nFile change detected!")
        last_modified_time = current_modified_time
        process_yaml_file() # Re-run the conversion

  except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("\n🛑 Watcher stopped. Goodbye!")
  except FileNotFoundError:
    print(f"\n❌ Error: '{INPUT_FILENAME}' was deleted. Stopping watcher.")


# --- Main execution block ---
if __name__ == "__main__":
  # First, ensure the input file exists.
  if not os.path.exists(INPUT_FILENAME):
    print(f"❌ Error: The file to watch, '{INPUT_FILENAME}', does not exist.")
    print("Please create it in the same directory as this script.")
  else:
    # Run the conversion once at the start to make sure the output is up-to-date
    print("Running initial conversion...")
    process_yaml_file()
    print("-" * 20)
    # Start the live watching process
    start_watching()
