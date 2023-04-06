import random
import itertools
import time

class GeneCalculator:

    def __init__(self, plants):
        self.plants = plants
        self.plant_array = []
        self.output_genes = ""
        self.final_result = []
        self.plant_dict = {}
        self.file = ""
        self.file_best = ""

    def generate_combinations(self):
        for i in range(2, 8):
            combinations = list(itertools.combinations(self.plants, i))
            for c in combinations:
                self.plant_array = list(c)
                self.calculate_genes()
                self.plant_array.clear()
                self.output_genes = ""

        self.process_final_results()
        

    def process_final_results(self):
        for result in self.final_result:
            if ((result.count('Y') == 2 and result.count('G') == 4) or (result.count('Y') == 3 and result.count('G') == 3) or (result.count('Y') == 4 and result.count('G') == 2)):
                print("BEST FOUND")
                print(self.plant_dict.get(result), result, file=self.file_best)

    def calculate_genes(self):
        gene_weights = {
            "G": 6,
            "H": 6,
            "Y": 6,
            "X": 10,
            "W": 10
        }

        gene_totals = {
            "G": 0,
            "H": 0,
            "Y": 0,
            "X": 0,
            "W": 0
        }

        # loop through all 6 genes for each plant
        for gene_position in range(6):

            # clear values of gene_totals dict
            gene_totals = {gene: 0 for gene in gene_totals.keys()}

            # add weight to corresponding gene in gene_totals dict
            for plant_position in range(len(self.plant_array)):
                gene = self.plant_array[plant_position][gene_position]
                gene_totals[gene] += gene_weights[gene]

            # determine winning gene by getting highest score, or randomimsing between those that tie
            max_gene = 0
            max_gene_name = ""
            
            for gene in gene_totals:
                currentGene = gene_totals.get(gene)

                if (currentGene > max_gene) or ((currentGene == max_gene) and (random.uniform(0, 1) > 0.5)):
                    max_gene = currentGene
                    max_gene_name = gene
            
            # append output_genes string
            self.output_genes += max_gene_name

        # if output_genes aren't stored, store them in file   
        if self.output_genes not in self.final_result:
            self.final_result.append(self.output_genes)
            self.plant_dict.update({self.output_genes: list(self.plant_array)})
            print(self.plant_array, self.output_genes, file=self.file)

# get plants from user, split and add to array
def get_user_input():
    user_input = ""
    plants = []

    print("\nNote: Enter all plants in a list with each plant on a new line. Type 'stop' when you are finished with input\n")
    
    while True:
        user_input = input("Enter plant: ").strip()
        if user_input == 'stop':
            break
        plants.append(user_input)
    
    print()
    return plants

# main function that controls flow of execution
def main():
    start_time = time.time()

    plants = get_user_input()
    gene_calculator = GeneCalculator(plants)
    with open("output.txt", "a") as gene_calculator.file, open("best.txt", "a") as gene_calculator.file_best: 
        gene_calculator.generate_combinations()
        
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()