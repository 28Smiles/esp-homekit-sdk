import copy
from distutils.dir_util import copy_tree
import os
from pathlib import Path
import subprocess
import shutil

examples_common = "examples/common"
common= "components/common"

process = subprocess.call(["git", "submodule", "update", "--init", "--recursive"],stdout=open(os.devnull, 'wb'))

shutil.copytree(examples_common, common)



