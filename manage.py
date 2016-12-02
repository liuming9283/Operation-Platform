# -*- coding:utf8 -*-
# !/usr/bin/env python
import os
import sys

# 方便程序员调试，无法处理多并发等情况，只是为了调试使用，避免每次修改代码都要重启服务器，
# 实际上Django还是依赖于web服务器
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
