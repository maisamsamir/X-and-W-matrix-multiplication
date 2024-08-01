import numpy as np

def matrix(x, w, block_size):
    num_blocks = w.shape[1] // block_size
    hb_memory = []
    vector_register2 = []
    
    for i in range(num_blocks):
        if vector_register2:
            reversed_list = vector_register2[::-1]
            if not hb_memory or hb_memory[-1] != reversed_list:  
                hb_memory.append(reversed_list.copy())
        vector_register2 = []

        for j in range(num_blocks):
            vector_register0 = x[0][j * block_size: (j + 1) * block_size]
            vector_register1 = w[j * block_size: (j + 1) * block_size, i * block_size: (i + 1) * block_size]
            block_results = [np.dot(vector_register0, vector_register1[:, col]) for col in range(vector_register1.shape[1])]
            
            if len(vector_register2) >= block_size:
                value = vector_register2[-1]
            else:
                value = 0
            
            for result in block_results:
                value = result + value
                if len(vector_register2) >= block_size:
                    vector_register2.pop()
                vector_register2.insert(0, value)
        
        reversed_list = vector_register2[::-1]
        if not hb_memory or hb_memory[-1] != reversed_list:  
            hb_memory.append(reversed_list)

    return hb_memory
x = np.random.randint(0, 10, size=(1, 4))
w = np.random.randint(0, 10, size=(4, 4))
block_size = 2
print(x)
print("")
print("")
print(w)
print("")
print("")
result = matrix(x, w, block_size)
print(result)
