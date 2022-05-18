Harness Feature Flag Python SDK
========================

[![pypi](https://img.shields.io/pypi/v/harness-featureflags.svg)](https://pypi.python.org/pypi/harness-featureflags)

## Table of Contents
**[Intro](#Intro)**<br>
**[Requirements](#Requirements)**<br>
**[Quickstart](#Quickstart)**<br>
**[Further Reading](docs/further_reading.md)**<br>
**[Build Instructions](docs/build.md)**<br>


## Intro

Harness Feature Flags (FF) is a feature management solution that enables users to change the software’s functionality, without deploying new code. FF uses feature flags to hide code or behaviours without having to ship new versions of the software. A feature flag is like a powerful if statement.
* For more information, see https://harness.io/products/feature-flags/
* To read more, see https://ngdocs.harness.io/category/vjolt35atg-feature-flags
* To sign up, https://app.harness.io/auth/#/signup/

![FeatureFlags](https://github.com/harness/ff-python-server-sdk/raw/main/docs/images/ff-gui.png)

## Requirements

[Python 3.7](https://www.python.org/downloads/) or newer (python --version)<br>
[pip](https://packaging.python.org/en/latest/tutorials/installing-packages/#id12)<br>
<br>
[For Mac users](https://opensource.com/article/19/5/python-3-default-mac) if you don't already have pyenv or something similar installed for managing python version<br>


## Quickstart
The Feature Flag SDK provides a client that connects to the feature flag service, and fetches the value
of featue flags.   The following section provides an example of how to install the SDK and initalize it from
an application.
This quickstart assumes you have followed the instructions to [setup a Feature Flag project and have created a flag called `harnessappdemodarkmode` and created a server API Key](https://ngdocs.harness.io/article/1j7pdkqh7j-create-a-feature-flag#step_1_create_a_project).

### Install the SDK
Install the python SDK using pip
```python
python -m pip install harness-featureflags
```

### A Simple Example
Here is a complete example that will connect to the feature flag service and report the flag value every 10 seconds until the connection is closed.  
Any time a flag is toggled from the feature flag service you will receive the updated value.

```python
from featureflags.client import CfClient
from featureflags.config import *
from featureflags.evaluations.auth_target import Target
from featureflags.util import log
import os
import time

# API Key
apiKey = os.getenv('FF_API_KEY', "changeme")

# Flag Name
flagName = os.getenv('FF_FLAG_NAME', "harnessappdemodarkmode")

def main():    
    # Create a Feature Flag Client
    client = CfClient(apiKey)

    # Create a target (different targets can get different results based on rules.  This include a custom attribute 'location')
    target = Target(identifier='mytarget', name="FriendlyName", attributes={"location": "emea"}

    # Loop forever reporting the state of the flag
    while True:
        result = client.bool_variation(flagName, target, False)
        log.info("Flag variation %s", result)
        time.sleep(10)

    close()


if __name__ == "__main__":
    main()
```

### Running the example

```bash
$ export FF_API_KEY=<your key here>
$ python3 examples/getting_started/getting_started.py
```

### Running with docker
If you dont have the right version of python installed locally, or dont want to install the dependancies you can
use docker to quicky get started

```bash
# Install the package
docker run -v $(pwd):/app -w /app python:3.7-slim python -m pip install -t ./local  harness-featureflags

# Run the script
docker run  -e PYTHONPATH=/app/local -e FF_API_KEY=$FF_API_KEY -v $(pwd):/app -w /app python:3.7-slim python examples/getting_started/getting_started.py
```

### Additional Reading

Further examples and config options are in the further reading section:

[Further Reading](docs/further_reading.md)


-------------------------
[Harness](https://www.harness.io/) is a feature management platform that helps teams to build better software and to
test features quicker.

-------------------------
