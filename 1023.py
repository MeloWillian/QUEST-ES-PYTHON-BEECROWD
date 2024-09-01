import io
import sys

input = sys.stdin.read
buffer = io.StringIO()

n = 1

data = input().splitlines()
i = 0
qtt = int(data[i])
i += 1

while qtt > 0: 
    ConsumoFinal = 0
    listaPessoa = {}
    total_pessoas = 0

    for _ in range(qtt):
        A, B = map(int, data[i].split())
        i += 1
        consumo = B // A

        if consumo in listaPessoa:
            listaPessoa[consumo] = listaPessoa[consumo] + A
        else:
            listaPessoa[consumo] = A
        ConsumoFinal += B
        total_pessoas += A                

    keys = sorted(listaPessoa.keys())

    if n > 1:
        buffer.write('\n\n')
    buffer.write(f"Cidade# {n}:\n")

    buffer.write(" ".join(f"{listaPessoa[p]}-{p}" for p in keys))
    buffer.write("\n")
    
    resultado = str(ConsumoFinal / total_pessoas) + "000"
    buffer.write(f"Consumo medio: {resultado[:resultado.index('.') + 3]} m3.")
    
    n += 1
    if i < len(data):
        qtt = int(data[i])
        i += 1
    else:
        break
    
print(buffer.getvalue())