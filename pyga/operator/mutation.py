from .operator import Operator


class Mutation(Operator):
    """
    Abstract class for mutation operators
    """
    def apply(self, selected_candidates):
        """
        Perform mutation on selected candidates.

        :param selected_candidates:
        :return:
        """
        for candidate in selected_candidates:
            candidate.data = self.mutate(candidate.data)
        return selected_candidates

    def mutate(self, data):
        """
        Perform mutation on candidate data

        :param data: mixed
        :return: mixed
        """
        raise NotImplementedError()
