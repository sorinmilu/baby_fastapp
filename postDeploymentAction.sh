#!/bin/bash
MARKER_FILE=/home/site/wwwroot/.init_script_ran

if [ ! -f "$MARKER_FILE" ]; then
    echo "Running initial setup script..."
    # Place your one-time setup tasks here

    # Create the marker file after successful execution
    touch "$MARKER_FILE"
    echo "Initial setup completed."
else
    echo "Initial setup script has already been run."
fi
