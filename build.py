import copy
from distutils.dir_util import copy_tree
import os
from pathlib import Path
import subprocess
import shutil

examples_common = "examples/common"
common= "components/common"

process = subprocess.call(["git", "submodule", "update", "--init", "--recursive"],stdout=open(os.devnull, 'wb'))
process = subprocess.call(["git", "apply", "patches/button_glitch_filter_time_ms.patch"],stdout=open(os.devnull, 'wb'))

if not Path(common).exists():
    shutil.copytree(examples_common, common)



