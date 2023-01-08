from ContasBanco import ContaCorrente
import time
# Programa

contaBeatriz = ContaCorrente('Beatriz', '002.205.442-12')

contaJorge = ContaCorrente('Jorge', '002.205.432-40')

contaJorge.depositar(12000)

contaJorge.transferir(2000, contaBeatriz)

time.sleep(5)


print('-' * 20)
contaJorge.hist_transacoes()
contaJorge.consultar_saldo()

print('-' * 20)
contaBeatriz.hist_transacoes()

contaBeatriz.consultar_saldo()