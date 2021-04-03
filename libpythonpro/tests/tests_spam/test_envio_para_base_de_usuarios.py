from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
            [
                Usuario(nome='Gabriel', email='gabrielpbarcellos@gmail.com'),
                Usuario(nome='Junior', email='junior@gmail.com')
            ],
            [
                Usuario(nome='Gabriel', email='gabrielpbarcellos@gmail.com'),
            ]
    ]
)
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
        enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gabrielpbarcellos@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantástiscos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gabriel', email='gabrielpbarcellos@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'junior@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantástiscos'
    )
    enviador.enviar.assert_called_once_with(
        'junior@gmail.com',
        'gabrielpbarcellos@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantástiscos'
    )
