virat = [9,3,7,8]
bumrah = [2,10,6,9] 
rohit = [8,2,6,7]

def dot_product(vec_a, vec_b):
    total = 0
    for i in range(len(vec_a)):
        total += vec_a[i] * vec_b[i] 
    return total
#print(dot_product(virat, bumrah)) 
#print(dot_product(virat, rohit)) 
rajat =[9,8,7,9]
rahul = [90,80,70,90]#scale is not needed

# print(dot_product(rajat, rahul)) #2750
# print(dot_product(rajat, rajat)) #275

import math
def vector_size(vec):
    total = 0
    for x in vec:
        total += x * x
    return math.sqrt(total)
# print(f"The size of the vector[3,4] is: {vector_size([3,4])}") #5.0, sqrt(3**2 + 4**2)
# print(f"The size of the vector[3,4] is: {vector_size(rajat)}") #16.583
# print(f"The size of the vector[3,4] is: {vector_size(rahul)}") #165.58
def cosine_similarity(vec_a,vec_b):
    dot = dot_product(vec_a,vec_b)
    size_a = vector_size(vec_a)
    size_b = vector_size(vec_b)

    if size_a == 0 or size_b ==0:
        return 0
    return dot/(size_a *size_b)

# print(f"rajat.rahul: {cosine_similarity(rajat, rahul)}") #0.9999999999999999, 
# print(f"rajat.rajat: {cosine_similarity(rajat, rajat)}") # 0.9999999999999998

king = [0.8, 0.6, -0.3, 0.9, 0.2]
queen = [0.7,0.7, -0.2, 0.8, 0.3]
cricket = [-0.1, 0.2, 0.8, 0.4, 0.7]
potato = [-0.5, 0.3, 0.1, -0.6, -0.2]

# print(f"king<--->queen: {cosine_similarity(king, queen)}")   #king<--->queen: 0.9877601445152481
# print(f"king<--->potato: {cosine_similarity(king, potato)}") #king<--->potato: -0.688092138000433

def find_best_word_in_llm(requirement_vector, vocabulary):
    scores = {}
    for word_name, word_vector in vocabulary.items():
        scores[word_name] = cosine_similarity(requirement_vector, word_vector)

    return sorted(scores.items(), key = lambda x: -x[1])
vocab = {"king": king , 'queen':queen , "cricket":cricket , "potato":potato}   #[('king', 0.9970914509633633), ('queen', 0.9967751548937049), ('cricket', 0.23611704164626884), ('potato', -0.6525425140216765)]
requirement = [0.75, 0.65, -0.25, 0.85, 0.25] 
for word, score in find_best_word_in_llm(requirement, vocab):
    print(f"  {word}:{score:.3f}")
