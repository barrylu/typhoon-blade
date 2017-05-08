import os,copy
from blade import blade
import blade_util

def SRC_DIR():
    return blade.get_current_source_path()

def OUT_DIR():
    return os.path.join(blade.__build_path,blade.__current_source_path)

def BLADE_ROOT():
    return blade.ccache_mgr.blade_root_dir

def WORK_DIR():
    return os.getcwd()
