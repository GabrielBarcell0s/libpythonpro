import pytest


from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['gabrielpbarcellos@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'gabrielpbarcellos@hotmail.com',
        'Teste Enviador',
        'Desenvolvendo em Python por partes'
    )
    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente',
    ['gabrielpbarcellos', '']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'gabrielpbarcellos@hotmail.com',
            'Teste Enviador',
            'Desenvolvendo em Python por partes'
        )
