from abc import ABC, abstractmethod

# Abstração para o serviço de notificação
class ServicoDeNotificacao(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        pass

# Implementação do serviço de e-mail
class ServicoDeEmail(ServicoDeNotificacao):
    def notificar(self, mensagem):
        print("Enviando e-mail:", mensagem)

# Implementação do serviço de SMS
class ServicoDeSMS(ServicoDeNotificacao):
    def notificar(self, mensagem):
        print("Enviando SMS:", mensagem)


class Notificador:
    def __init__(self, servico: ServicoDeNotificacao):
        self.servico = servico

    def enviar_notificacao(self, mensagem):
        self.servico.notificar(mensagem)


servico_email = ServicoDeEmail()
notificador_email = Notificador(servico_email)
notificador_email.enviar_notificacao("Olá! Este é um e-mail de teste.")

servico_sms = ServicoDeSMS()
notificador_sms = Notificador(servico_sms)
notificador_sms.enviar_notificacao("Olá! Este é um SMS de teste.")
