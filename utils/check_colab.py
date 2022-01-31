from pathlib import Path
import os
import sys
import subprocess

def set_datapath(default_path):
    if 'google.colab' in str(get_ipython()):
        from google.colab import drive
        IS_COLAB = True
        if not os.path.isdir('/gdrive'):
            drive.mount('/gdrive')
        datapath = Path('/gdrive/My Drive')
        
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pytorch-lightning', '--quiet'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'scikit-image==0.19.*', '--quiet'])
        
    else:
        IS_COLAB = False
        datapath = Path(default_path)

    return IS_COLAB, datapath