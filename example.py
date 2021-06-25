from featureflags.evaluations.target import Target
import time

from featureflags.client import CfClient
from featureflags.util import log


def main():
    log.debug("Starting example")
    client = CfClient("7fba0ca2-32d9-4cec-9f9e-5c0fd5d1ee9d")

    target = Target('johndoe')
    result = client.bool_variation('pytest', target, False)
    log.debug("Result %s", result)
    # print(client.get_environment_id())
    # time.sleep(5)


if __name__ == "__main__":
    main()