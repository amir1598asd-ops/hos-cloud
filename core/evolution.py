from core.genome import GenomeManager


class EvolutionEngine:


    def __init__(self):

        self.genome = GenomeManager()



    def improve(self, ranking):


        for item in ranking:


            agent=item["agent"]


            score=item["score"]



            if score >= 5:

                self.genome.reward(
                    agent,
                    1
                )

            else:

                self.genome.punish(
                    agent
                )



        return self.genome.load()