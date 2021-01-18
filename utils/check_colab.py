from google.colab import drive
from pathlib import Path

def set_datapath(default_path):
    try:
        # %tensorflow_version only exists in Colab.
        %tensorflow_version 2.x
        IS_COLAB = True
    except Exception:
        IS_COLAB = False
        datapath = Path(default_path)
        
    if IS_COLAB:
        drive.mount('/gdrive')
        datapath = Path('/gdrive/My Drive')

    return IS_COLAB