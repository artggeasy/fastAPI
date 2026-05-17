class ContextoSimples:
    def __enter__(self):
        print("iniciar Conexão")
        return self
    def __exit__(self,exc_type, exc_val, exc_tb):
        print("fechando conexão com segurança")
        
with ContextoSimples() as cs:
    print("Execuções em Banco de Dados!")