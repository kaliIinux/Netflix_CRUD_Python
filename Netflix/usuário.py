class Cliente:
    def __init__(self, nome='', email='', plano='', tipo='user'):
        self.nome = nome
        self.email = email
        self.planos = ['basic', 'medium', 'premium']
        self.tipo = ['user', 'admin']
        if plano in self.planos:
            self.plano = plano