t Practices for Writing Bash Scripts

------
I recently refacted a bash script. I decide to keep a few best practices in one place.Here goes:

* Use long options (```logger --priority ``` vs ```logger -p ```). If you're on cli, abbreviations make sense for efficiency. but when you're writing reusable scripts a few extra keystrokes will pay off in readability and avoid ventures into man pages in the future by you or your collaborators

* Use ``` set -o errexit``` (a.k.a. ``` set -e```) to make your script exit when acommand fails.Then add ```|| true``` to commands that you allow to fail.

* Use ``` set -o nounset``` (a.k.a. ``` set -u```) to exit when your script tries to use undeclared variables

* Use ``` set -o xtrace``` (a.k.a ``` set -x```) to trace what gets executed. Useful for debugging.

* Use ``` set -o pipefail``` in scripts to catch ``` mysqldump ``` fails in e.g. ``` mysqldump |gzip ```. The exit status of the last command that threw a non-zero exit code is returned.

* ```#!/usr/bin/env bash ``` is more portable than ``` #!/bin/bash ```

* Avoid using ``` #!/usr/bin/env bash -e ```(vs  ```set -e ```), because when someone runs your script as ```bash ./script.sh ```, the exit on error will be ignored.

* Surround your variables with ```{}```. Otherwise bash will try to access the ```$ENVIRONMENT_app ``` variable in ```/srv/$ENVIRONMENT_app```, whereas you probably intended ```/srv/${ENVIRONMENT}_app```.

* You don't need two equal signs when checking ```if [ "${NAME}" = "hereischen" ]```.

* Surround your variable with ```"``` in ```if [ "${NAME}" = "hereischen" ]```, because ```if $NAME``` isn't declared, bash will throw a syntax error (also see nounset).

* Use ```:-``` if you want to test variables that could be undeclared. For instance: ```if [ "${NAME:-}" = "hereischen" ]``` will set ```$NAME``` to be empty if it's not declared. You can also set it to noname like so ```if [ "${NAME:-noname}" = "hereischen" ]```.

* Set magic variables for current file, basename, and directory at the top of your script for convenience.

So your bash script may like this:
```shell
#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

# Set magic variables for current file & dir
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename ${__file} .sh)"
__root="$(cd "$(dirname "${__dir}")" && pwd)" # <-- change this as it depends on your app

arg1="${1:-}"
```
