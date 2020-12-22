# ---Defanging an IP Address---


def defangIPaddr(self, address: str) -> str:
    return address.replace(".", "[.]")
