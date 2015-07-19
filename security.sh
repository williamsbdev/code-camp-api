#!/bin/bash

# this command will return places where the application shells out or dynamically executes code:
SHELL_COMMANDS=$(egrep -r --include "*.py" -e "exec\(|eval\(|subprocess|popen" .)
SHELL_COMMANDS_EXIT=$?

# DJANGO: find places where HTML encoding is turned off via the "safe" attribute:
HTML_ENCODING=$(grep -r --include "*.py" --include "*.html" -e "|safe" .)
HTML_ENCODING_EXIT=$?

# Non zero values indicate that some sort of CSRF protection is probably enabled.
# run without "| wc -l" to check CSRF-enabled endpoints and compare that list
# against all endpoints
CSRF_PROTECTION_COUNT=$(egrep -r "(?i)csrf" . | wc -l)
CSRF_PROTECTION=$(egrep -r "(?i)csrf" .)

if [[ "$SHELL_COMMANDS_EXIT" == 1 ]] && [[ "$HTML_ENCODING_EXIT" == 1 ]]; then
    echo "Security checks passed"
    exit 0
fi

echo "There is a security issue."
echo SHELL_COMMANDS $SHELL_COMMANDS
echo HTML_ENCODING $HTML_ENCODING
exit 1
