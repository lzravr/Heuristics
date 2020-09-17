class Params:
    population_size = 10
    domain_max = 5.12
    domain_min = -5.12
    _lambda = 1.5
    pa = 0.25
    step_size = 0.01
    dimension = 10
    iterations = 3000

    @classmethod
    def get_population_size(cls):
        return cls.population_size
    
    @classmethod
    def get_domain_max(cls):
        return cls.domain_max

    @classmethod
    def get_domain_min(cls):
        return cls.domain_min

    @classmethod
    def get_lambda(cls):
        return cls._lambda

    @classmethod
    def get_pa(cls):
        return cls.pa

    @classmethod
    def get_step_size(cls):
        return cls.step_size
    
    @classmethod
    def get_dimension(cls):
        return cls.dimension

    @classmethod
    def get_iterations(cls):
        return cls.iterations

    @classmethod
    def set_population_size(cls, population_size):
        cls.population_size = population_size

    @classmethod
    def set_domain_max(cls, domain_max):
        cls.domain_max = domain_max

    @classmethod
    def set_domain_min(cls, domain_min):
        cls.domain_min = domain_min

    @classmethod
    def set_lambda(cls, l):
        cls._lambda = l

    @classmethod
    def set_pa(cls, pa):
        cls.pa = pa

    @classmethod
    def set_step_size(cls, step_size):
        cls.step_size = step_size

    @classmethod
    def set_dimension(cls, dimension):
        cls.dimension = dimension

    @classmethod
    def set_iterations(cls, iterations):
        cls.iterations = iterations
