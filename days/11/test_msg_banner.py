#!/usr/bin/env pytest

from msg_banner import msg_banner


def test_msg_banner(capfd):
    msg_banner('test')
    print(capfd.readouterr())
