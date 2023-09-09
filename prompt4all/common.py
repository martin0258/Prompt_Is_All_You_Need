import socket
from typing import List, Union
__all__ = ["find_available_port"]


def find_available_port(priority: Union[int, List[int]] = None) -> int:
    """
    Find an available port on the system.

    :param priority: Optional. A port number or a list of port numbers that will be checked first.
    :return: An available port number.
    """

    def _is_port_available(port: int) -> bool:
        """
        Check if a port is available.

        :param port: A port number.
        :return: True if the port is available; False otherwise.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) != 0

    if priority is not None:
        if isinstance(priority, int):
            if _is_port_available(priority):
                return priority
        elif isinstance(priority, list):
            for port in priority:
                if _is_port_available(port):
                    return port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]
