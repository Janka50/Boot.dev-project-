

#!/bin/bash
python3 main.py
cd public || exit 1
python3 -m http.server 8888
