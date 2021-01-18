from google.colab import drive
from pathlib import Path

def set_datapath(default_path):
    if 'google.colab' in str(get_ipython()):
        IS_COLAB = True
        drive.mount('/gdrive')
        datapath = Path('/gdrive/My Drive')
    else:
        IS_COLAB = False
        datapath = Path(default_path)

    return IS_COLAB