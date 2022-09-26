
"""

Casos cpf;

- Falso, quando o CPF não possuir o formato 999.999.999-99;
- Falso, quando o CPF não possuir 11 caracteres numéricos;
- Falso, quando os dígitos verificadores forem inválidos;
- Verdadeiro, caso contrário.


"""

import ValidateCPF, ValidateEmail


class TestCpf(object):
    def test_cpf_valido(self):
        v = ValidateEmail
        cpf = '034.974.762-85'
        assert v.validatecpf(cpf) == True

    def test_sem_pontuacao(self):
        v = ValidateCPF
        cpf = '03497476285'
        assert v.validatecpf(cpf) == False
    
    def test_pontuacao_fora_de_lugar(self):
        v = ValidateCPF
        cpf = '034.974.76-285'
        assert v.validatecpf(cpf) == False

    def test_sem_hifen(self):
        v = ValidateCPF
        cpf = '034.974.76285'
        assert v.validatecpf(cpf) == False

    def test_numeros_sequenciais(self):
        v = ValidateCPF
        cpf = '123.456.789-10'
        assert v.validatecpf(cpf) == False

    def test_menos_de_11_num(self):
        v = ValidateCPF
        cpf = '034.974.762-8'
        assert v.validatecpf(cpf) == False
    def test_mais_de_11_num(self):
        v = ValidateCPF
        cpf = '034.974.762-856'
        assert v.validatecpf(cpf) == False

    def test_dig_verificadores(self):
        v = ValidateCPF
        cpf = '034.974.762-58'
        assert v.validatecpf(cpf) == False

    def test_dig_verificadores_validos(self):
        v = ValidateCPF
        cpf = '034.974.762-85'
        assert v.validatecpf(cpf) == True
    def test_caracter_invalido(self):
        v = ValidateCPF
        cpf = '034.974.762_85'
        assert v.validatecpf(cpf) == False
        cpf = '034.974.762a85'
        assert v.validatecpf(cpf) == False

    def test_num_iguais(self):
        v = ValidateCPF
        cpf = '111.111.111-11'
        assert v.validatecpf(cpf) == False

    def test_cpf_em_branco(self):
        v = ValidateCPF
        cpf = ''
        assert v.validatecpf(cpf) == False
       
class TestEmail(object):

    def test_email_valido(self):
        v = ValidateEmail
        email = 'joaopaulorm7@gmail.com'
        assert v.validatecpf(email) == True

    def test_email_em_branco():
        v = ValidateEmail
        email = ''
        assert v.validatecpf(email) == False
    def test_email_em_branco():
        v = ValidateEmail
        email = ''
        assert v.validatecpf(email) == False