import subprocess


comando = 'net user'

try:
    resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)

    print(resultado.stdout)
except Exception as e:
    print(e)

