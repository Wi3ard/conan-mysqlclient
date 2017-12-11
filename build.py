#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conan.packager import ConanMultiPackager

if __name__ == "__main__":
#    builder = ConanMultiPackager()
    builder = ConanMultiPackager(username="wi3ard", visual_versions = [14, 15], gcc_versions = ["4.8", "4.9", "5.2", "5.3"])
    builder.add_common_builds(shared_option_name="mysql-connector-c:shared", pure_c=False)
    builder.run()
