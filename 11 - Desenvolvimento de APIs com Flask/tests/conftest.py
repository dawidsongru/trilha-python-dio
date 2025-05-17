import sys
import os

# Caminho absoluto até a pasta 'src'
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dio_bank', 'src'))

# Adiciona ao sys.path se ainda não estiver
if src_path not in sys.path:
    sys.path.insert(0, src_path)
