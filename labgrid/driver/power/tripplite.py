import sys
import subprocess

from ..exception import ExecutionError

OID = ".1.3.6.1.4.1.850.100.1.10.2.1.4"

def _snmp_get(host, oid):
    out = subprocess.check_output(
        "snmpget -v1 -c private -O qn {} {}".format(host, oid).split()
    ).decode('ascii')
    out_oid, value = out.strip().split(' ', 1)
    assert oid == out_oid
    if value == "2":
        return True
    elif value == "1":
        return False
    else:
        raise ExecutionError("failed to get SNMP value")


def _snmp_set(host, oid, value):
    try:
        subprocess.check_output(
            "snmpset -v1 -c private {} {} {}".format(host, oid, value).split()
        )
    except Exception as e:
        raise ExecutionError("failed to set SNMP value") from e


def set(host, index, value):
    index = int(index)
    value = 2 if value else 1
    assert 1 <= index <= 8

    _snmp_set(host, "{}.{}".format(OID, index), "int {}".format(value))


def get(host, index):
    index = int(index)
    assert 1 <= index <= 8

    return _snmp_get(host, "{}.{}".format(OID, index))
